import requests
from concurrent.futures import ThreadPoolExecutor

def scan_subdomain(subdomain, domain):
    url = f"http://{subdomain}.{domain}"
    try:
        requests.get(url, timeout=2)
        print(f"[+] Discovered: {url}")
    except requests.ConnectionError:
        pass
    except Exception:
        pass

def main():
    target_domain = input("Target Domain (e.g., google.com): ")
    wordlist_path = input("Subdomain wordlist path: ")
    
    try:
        with open(wordlist_path, "r") as f:
            subdomains = [line.strip() for line in f]
    except FileNotFoundError:
        print("[-] Wordlist not found!")
        return

    print(f"\n[*] Scanning {len(subdomains)} subdomains for {target_domain}...\n")
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        for sub in subdomains:
            executor.submit(scan_subdomain, sub, target_domain)

if __name__ == "__main__":
    main()
