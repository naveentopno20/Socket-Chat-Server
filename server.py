import socket
import threading

HOST = '127.0.0.1'
PORT = 4000

clients = {}
lock = threading.Lock()

def broadcast(msg, sender=None):
    with lock:
        for user, conn in clients.items():
            if user != sender:
                try:
                    conn.sendall((msg + '\n').encode())
                except:
                    pass

def handle_client(conn, addr):
    username = None
    conn.sendall(b"INFO Welcome! Please login with: LOGIN <username>\n")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode().strip()
            if not message:
                continue

            if message.upper().startswith("LOGIN "):
                username = message.split(" ", 1)[1].strip()
                with lock:
                    clients[username] = conn
                conn.sendall(b"OK\n")
                broadcast(f"INFO {username} joined the chat!", sender=username)
                print(f"[+] {username} logged in from {addr}")
                continue

            if username is None:
                conn.sendall(b"ERR Please login first using LOGIN <username>\n")
                continue

            if message.upper().startswith("MSG "):
                msg_text = message[4:].strip()
                broadcast(f"{username}: {msg_text}", sender=username)
                conn.sendall(b"OK\n")

            elif message.upper() == "WHO":
                with lock:
                    online = ", ".join(clients.keys())
                conn.sendall(f"INFO Online: {online}\n".encode())

            elif message.upper().startswith("DM "):
                parts = message.split(" ", 2)
                if len(parts) < 3:
                    conn.sendall(b"ERR Usage: DM <user> <message>\n")
                    continue
                target, dm_text = parts[1], parts[2]
                with lock:
                    if target in clients:
                        clients[target].sendall(f"[DM from {username}] {dm_text}\n".encode())
                        conn.sendall(b"OK\n")
                    else:
                        conn.sendall(b"ERR User not found.\n")

            elif message.upper() == "PING":
                conn.sendall(b"PONG\n")

            elif message.upper() == "LOGOUT":
                conn.sendall(b"Disconnected.\n")
                break

            else:
                conn.sendall(b"ERR Unknown command.\n")

    except Exception as e:
        if "10054" not in str(e):
            print(f"[!] Error with {addr}: {e}")

    finally:
        if username:
            with lock:
                if username in clients:
                    del clients[username]
            broadcast(f"INFO {username} has left the chat.")
        conn.close()
        print(f"[-] Connection closed: {addr}")

def start_server():
    print(f"[SERVER] Matrix Chat Server running on port {PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()
