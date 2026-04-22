import hashlib

def crack_hash(target_hash, wordlist_path, hash_type="md5"):
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                word = line.strip()
                if hash_type == "md5":
                    hashed_word = hashlib.md5(word.encode()).hexdigest()
                elif hash_type == "sha1":
                    hashed_word = hashlib.sha1(word.encode()).hexdigest()
                else:
                    print("[-] Unsupported hash type")
                    return

                if hashed_word == target_hash:
                    print(f"\n[+] Password Found: {word}")
                    return word
        print("\n[-] Password not found in wordlist.")
    except FileNotFoundError:
        print("[-] Wordlist not found!")

def main():
    print("--- Simple Hash Cracker ---")
    target = input("Enter Hash: ").strip().lower()
    w_path = input("Enter Wordlist Path: ").strip()
    h_type = input("Enter Hash Type (md5/sha1): ").strip().lower()
    
    crack_hash(target, w_path, h_type)

if __name__ == "__main__":
    main()
