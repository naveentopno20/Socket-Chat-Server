#!/usr/bin/env python3
import socket
import threading
import sys
import os

GREEN = "\033[92m"
DARK_GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = "\033[1m"

HOST = "localhost"
PORT = 4000

def matrix_title():
    os.system("cls" if os.name == "nt" else "clear")
    print(GREEN + BOLD)
    print("╔════════════════════════════════════════════════════════════╗")
    print("║                 MATRIX CHAT CLIENT (PYTHON)                ║")
    print("╚════════════════════════════════════════════════════════════╝" + RESET)
    print(DARK_GREEN + f"Connected to Matrix Chat Server on port {PORT}" + RESET)
    print(DARK_GREEN + "Type: LOGIN <username>  MSG <text>  WHO  DM <user> <text>  PING" + RESET)
    print(DARK_GREEN + "Type /quit to exit\n" + RESET)

def recv_messages(sock):
    buffer = b""
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                print(RESET + "\n[Disconnected from server]", flush=True)
                break
            buffer += data
            # split on \n to handle \r\n or \n endings
            while b"\n" in buffer:
                line, buffer = buffer.split(b"\n", 1)
                try:
                    msg = line.decode(errors="ignore").rstrip('\r')
                except:
                    msg = line.decode('utf-8', errors='ignore')
                if not msg:
                    continue
                # print instantly without buffering
                if msg.startswith("INFO"):
                    print(DARK_GREEN + msg + RESET, flush=True)
                elif msg.startswith("ERR"):
                    print("\033[91m" + msg + RESET, flush=True)
                else:
                    print(GREEN + msg + RESET, flush=True)
    except Exception as e:
        print("\n[recv error]", e, flush=True)
    finally:
        try:
            sock.close()
        except:
            pass
        os._exit(0)


def main():
    matrix_title()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        try:
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        except Exception:
            pass
    except Exception as e:
        print("\033[91m[!] Could not connect:\033[0m", e)
        sys.exit(1)

    t = threading.Thread(target=recv_messages, args=(sock,))
    t.start()

    try:
        while True:
            line = input(DARK_GREEN + ">> " + RESET)
            if line.strip().lower() in ("/quit", "exit", "logout"):
                try:
                    sock.sendall(b"LOGOUT\r\n")
                except:
                    pass
                print(RESET + "Disconnected.")
                break
            # always send CRLF
            try:
                sock.sendall((line.strip() + "\r\n").encode("utf-8"))
            except Exception as e:
                print("\n[send error]", e)
                break
    except KeyboardInterrupt:
        print("\nExiting.")
    finally:
        try:
            sock.close()
        except:
            pass

if __name__ == "__main__":
    main()
