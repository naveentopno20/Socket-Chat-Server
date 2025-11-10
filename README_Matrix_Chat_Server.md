# 🧠 Matrix-Style Socket Chat Server (Python)

## 👨‍💻 Overview
This project is a **Matrix-inspired Socket Chat Server** built in Python.  
It allows multiple clients to connect, login, and communicate in real-time using TCP sockets.  
The terminal UI is designed with a **futuristic green Matrix theme**, giving it a hacker-style appearance.  

---

## ⚙️ Tech Stack
- **Language:** Python 3  
- **Libraries:** `socket`, `threading`, `os`  
- **Environment:** Works on PowerShell / CMD (Windows)  
- **Port Used:** `4000`

---

## 🚀 How to Run

### 🖥️ 1. Start the Server
Open a PowerShell terminal in the project folder and run:
```bash
python server.py
```
✅ You’ll see:
```
[SERVER] Matrix Chat Server running on port 4000
```

---

### 💻 2. Start Client 1
Open another PowerShell window:
```bash
python client.py
```
You’ll see:
```
Connected to Matrix Chat Server on port 4000
Type commands like LOGIN <username>, MSG <text>, WHO, DM <user> <text>
Press Ctrl + C or type /quit to exit
```

Now login:
```bash
LOGIN Naman
```

---

### 💻 3. Start Client 2
Open one more PowerShell window:
```bash
python client.py
```
Then login:
```bash
LOGIN Yudi
```

---

## 💬 Available Commands
| Command | Description | Example |
|----------|--------------|----------|
| `LOGIN <username>` | Login with a unique username | `LOGIN Naman` |
| `MSG <text>` | Broadcast message to everyone | `MSG Hello all!` |
| `DM <user> <text>` | Send private message | `DM Yudi Hey there!` |
| `WHO` | List online users | `WHO` |
| `PING` | Check server response | `PING` |
| `LOGOUT` | Disconnect gracefully | `LOGOUT` |

---

## 🧩 Features
- Multi-client real-time chat  
- Matrix-style green neon interface  
- Private (DM) and broadcast messaging  
- Command-based message handling  
- Thread-safe and stable socket communication  
- Graceful user logout handling  
- Works locally on port 4000  

---

## 🧱 Project Structure
```
Matrix_Style_Socket_Chat_Server/
│
├── server.py      # Main server script (handles all clients)
├── client.py      # Matrix-style client interface
├── README.md      # Project documentation
└── requirements.txt  # (Optional, if needed for Python version info)
```

---

## 📸 Sample Output

**Client 1 (Naman):**
```
LOGIN Naman
OK
MSG Hello from Naman!
INFO Yudi joined the chat!
Yudi: Hey Naman!
```

**Client 2 (Yudi):**
```
LOGIN Yudi
OK
MSG Hey Naman!
INFO Online: Naman, Yudi
```

---

## 🎥 Screen Recording
A short demo video (1–2 minutes) showing:  
- Server running locally  
- Two clients chatting in real time  
- Commands like `LOGIN`, `MSG`, `WHO`, `DM`, and `LOGOUT`  

📎 **Watch the recording here:**  
👉 [Matrix Chat Server - Screen Recording (Google Drive)](https://drive.google.com/file/d/1YnZUoYvCdNs1VDu0zAkHuSuBma1dIet1/view?usp=drivesdk)

---

## 🧠 Notes
- You can open multiple PowerShell terminals to simulate multiple users.  
- Make sure to **run the server first** before connecting clients.  
- This project is ideal for demonstrating socket programming, threading, and basic real-time communication.

---

## 🏁 Author
**Developed by:** *Naveen Topno*  
**Project Title:** Matrix-Style Socket Chat Server  
**Course:** MCA / Python Networking Assignment  
**Date:** November 2025  
