import requests
from concurrent.futures import ThreadPoolExecutor

target = input("Target URL (örn: http://example.com): ").rstrip("/")
wordlist_file = input("Wordlist path: ")

threads = 20

def scan(path):
    url = f"{target}/{path}"
    try:
        r = requests.get(url, timeout=3)
        if r.status_code < 400:
            print(f"[+] {r.status_code} -> {url}")
    except:
        pass

with open(wordlist_file, "r") as f:
    paths = [line.strip() for line in f]

print(f"\nScanning {len(paths)} paths...\n")

with ThreadPoolExecutor(max_workers=threads) as executor:
    executor.map(scan, paths)