# 🛡️ Offensive Python Toolkit

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cybersecurity](https://img.shields.io/badge/Field-Cybersecurity-red.svg)](#)

A powerful, lightweight collection of Python-based security tools for penetration testing and offensive security research. This toolkit focuses on automation, speed, and simplicity.

---

## 🚀 Getting Started

### Prerequisites
Ensure you have Python 3.8 or higher installed on your system.

### Installation
Clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/HamzaCelikk/Offensive-Python-Toolkit.git
cd Offensive-Python-Toolkit
pip install -r requirements.txt
```

---

## 🌟 The Offensive Toolkit Menu (Recommended)

The easiest and most powerful way to use this toolkit is through the **Interactive Command-Line Menu**. It provides a beautifully styled, user-friendly interface to launch any tool without typing manual commands.

**To launch the menu, simply run:**
```bash
python main.py
```

### 💻 Menu Preview
```text
   ____  __  __               _           
  / __ \/ _|/ _|             (_)          
 | |  | | |_| |_ ___ _ __  ___ ___   _____ 
 | |  | |  _|  _/ _ \ '_ \/ __| \ \ / / _ \
 | |__| | | | ||  __/ | | \__ \ |\ V /  __/
  \____/|_| |_| \___|_| |_|___/_| \_/ \___|

        Python Offensive Toolkit        
    Created for Educational Purposes    

[1] Network Scanner      (network_scanner.py)
[2] Web Directory Fuzzer (web_fuzzer.py)
[3] Hash Cracker         (hash_cracker.py)
[4] Keylogger            (keylogger.py)
[5] Subdomain Scanner    (subdomain_scanner.py)
[99] Exit
```

---

<details>
<summary><b>🛠️ Click here to see details of individual tools & standalone usage</b></summary>

<br>

### 1. 📡 Network Scanner (`network_scanner.py`)
A fast, multi-threaded port scanner designed to identify open services and grab banners for service identification.
*Standalone usage: `python network_scanner.py`*

### 2. 🌐 Web Fuzzer (`web_fuzzer.py`)
A high-speed directory and file brute-forcer for web applications.
*Standalone usage: `python web_fuzzer.py`*

### 3. ⌨️ Keylogger (`keylogger.py`)
A stealthy keystroke logger that records all inputs to a local file.
- **Features**: Captures special keys, Local logging (`key_log.txt`), Background-ready listener
*Standalone usage: `python keylogger.py`*

### 4. 🔍 Subdomain Scanner (`subdomain_scanner.py`)
A multi-threaded tool to discover subdomains for a target domain.
- **Features**: Rapid DNS/HTTP discovery, Customizable wordlists, Efficient concurrency
*Standalone usage: `python subdomain_scanner.py`*

### 5. 🔑 Hash Cracker (`hash_cracker.py`)
A dictionary-based cracker for MD5 and SHA1 hashes.
- **Features**: Supports MD5 & SHA1, Fast dictionary attacks, Easy-to-use interface
*Standalone usage: `python hash_cracker.py`*

</details>

---

## ⚠️ Disclaimer
> [!IMPORTANT]
> This toolkit is for **educational purposes** and **authorized penetration testing** only. Use it responsibly and only on systems you have explicit permission to test. The author is not responsible for any misuse of these tools.

---

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request to add more tools or improve existing ones.

---

**Developed with ❤️ by [Hamza Çelik](https://github.com/HamzaCelikk)**
