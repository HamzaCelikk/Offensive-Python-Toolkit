# 🛡️ Offensive Python Toolkit

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Cybersecurity](https://img.shields.io/badge/Field-Cybersecurity-red.svg)](#)

A powerful, lightweight collection of Python-based security tools for penetration testing and offensive security research. This toolkit focuses on automation, speed, and simplicity.

---

## 🛠️ Included Tools

### 1. 📡 Network Scanner (`network_scanner.py`)
A fast, multi-threaded port scanner designed to identify open services and grab banners for service identification.
- **Features**: 
  - Multi-threaded scanning (ThreadPoolExecutor)
  - Banner grabbing
  - Customizable port ranges

### 2. 🌐 Web Fuzzer (`web_fuzzer.py`)
A high-speed directory and file brute-forcer for web applications.
- **Features**: 
  - Wordlist-based discovery
  - Threaded execution for maximum performance
  - Status code filtering

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

### Network Scanner
```bash
python network_scanner.py
# Input Target IP when prompted
```

### Web Fuzzer
```bash
python web_fuzzer.py
# Input Target URL and Wordlist Path when prompted
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
