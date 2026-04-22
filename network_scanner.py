import socket
from concurrent.futures import ThreadPoolExecutor

target = input("Target IP: ")
ports = range(1, 1025)

def scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        
        if result == 0:
            try:
                banner = s.recv(1024).decode().strip()
            except:
                banner = "No banner"
            print(f"[+] Port {port} OPEN | {banner}")
        
        s.close()
    except:
        pass

print(f"\nScanning {target}...\n")

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan, ports)