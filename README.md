# 🛡️ Offensive Python Toolkit

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cybersecurity](https://img.shields.io/badge/Field-Cybersecurity-red.svg)](#)

A powerful, lightweight collection of Python-based security tools for penetration testing and offensive security research. This toolkit focuses on automation, speed, and simplicity.

---

## 🛠️ Included Tools

### 🌟 Interactive Menu (`main.py`)
An all-in-one, beautifully styled command-line interface to easily select and run any tool in the toolkit without typing manual commands.

### 1. 📡 Network Scanner (`network_scanner.py`)
A fast, multi-threaded port scanner designed to identify open services and grab banners for service identification.

### 2. 🌐 Web Fuzzer (`web_fuzzer.py`)
A high-speed directory and file brute-forcer for web applications.

### 3. ⌨️ Keylogger (`keylogger.py`)
A stealthy keystroke logger that records all inputs to a local file.
- **Features**: 
  - Captures special keys
  - Local logging (`key_log.txt`)
  - Background-ready listener

### 4. 🔍 Subdomain Scanner (`subdomain_scanner.py`)
A multi-threaded tool to discover subdomains for a target domain.
- **Features**: 
  - Rapid DNS/HTTP discovery
  - Customizable wordlists
  - Efficient concurrency

### 5. 🔑 Hash Cracker (`hash_cracker.py`)
A dictionary-based cracker for MD5 and SHA1 hashes.
- **Features**: 
  - Supports MD5 & SHA1
  - Fast dictionary attacks
  - Easy-to-use interface

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

## 📖 Usage Examples

### 🌟 All-in-One Interactive Menu (Recommended)
Run the main script to access a beautifully styled interactive menu where you can easily launch all tools:
```bash
python main.py
```

### Individual Tools Usage

#### Network Scanner
```bash
python network_scanner.py
```

### Web Fuzzer
```bash
python web_fuzzer.py
```

### Keylogger
```bash
python keylogger.py
```

### Subdomain Scanner
```bash
python subdomain_scanner.py
```

### Hash Cracker
```bash
python hash_cracker.py
```

---

## ⚠️ Disclaimer
> [!IMPORTANT]
> This toolkit is for **educational purposes** and **authorized penetration testing** only. Use it responsibly and only on systems you have explicit permission to test. The author is not responsible for any misuse of these tools.

---

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request to add more tools or improve existing ones.

---

**Developed with ❤️ by [Hamza Çelik](https://github.com/HamzaCelikk)**
