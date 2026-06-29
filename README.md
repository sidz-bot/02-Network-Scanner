# 🌐 Network Scanner

A beginner-friendly ARP Network Scanner built with Python and Scapy.

This project is part of my Cybersecurity Portfolio, where I build practical cybersecurity tools from scratch to improve my networking, Python, and security skills.

---

## 📌 Features

- Scan a local network using ARP
- Discover active devices
- Display IP and MAC addresses
- Built using Scapy
- Beginner-friendly code structure

---

## 🛠️ Technologies Used

- Python 3
- Scapy

---

## 📂 Project Structure

```
02-Network-Scanner/
│
├── scanner.py
├── requirements.txt
├── README.md
├── .gitignore
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/sidz-bot/02-Network-Scanner.git
```

Move into the project folder:

```bash
cd 02-Network-Scanner
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows (Git Bash)

```bash
source .venv/Scripts/activate
```

### Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Usage

Run the scanner:

```bash
python scanner.py
```

Example input:

```
192.168.1.0/24
```

Example output:

```
========================================
      Network Scanner
========================================

Devices Found

IP Address : 192.168.1.1
MAC Address: XX:XX:XX:XX:XX:XX

IP Address : 192.168.1.7
MAC Address: XX:XX:XX:XX:XX:XX
```

---

## 📚 Concepts Learned

- Computer Networks
- IPv4 Addressing
- MAC Addressing
- ARP (Address Resolution Protocol)
- Ethernet Frames
- Layer 2 Communication
- Scapy
- Python Networking

---

## 🎯 Future Improvements

- Better output formatting
- Colored terminal output
- Save scan results to CSV
- Save scan results to JSON
- Device vendor lookup
- Error handling
- Command-line arguments
- Scan progress indicator

---

## ⚠️ Note

This tool is intended **only for educational purposes** and should only be used on networks you own or have explicit permission to scan.

---

## 👨‍💻 Author

**Siddharth Lambore**

GitHub: https://github.com/sidz-bot

---

## 📄 License

This project is licensed under the MIT License.