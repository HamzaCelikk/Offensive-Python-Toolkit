import os
import sys

# Color codes
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_banner():
    banner = f"""{Colors.FAIL}{Colors.BOLD}
   ____  __  __               _           
  / __ \/ _|/ _|             (_)          
 | |  | | |_| |_ ___ _ __  ___ ___   _____ 
 | |  | |  _|  _/ _ \ '_ \/ __| \ \ / / _ \\
 | |__| | | | ||  __/ | | \__ \ |\ V /  __/
  \____/|_| |_| \___|_| |_|___/_| \_/ \___|
{Colors.ENDC}
{Colors.OKCYAN}        Python Offensive Toolkit        {Colors.ENDC}
{Colors.OKBLUE}    Created for Educational Purposes    {Colors.ENDC}
"""
    print(banner)

def main_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_banner()
        print(f"{Colors.OKGREEN}[1]{Colors.ENDC} Network Scanner      ({Colors.WARNING}network_scanner.py{Colors.ENDC})")
        print(f"{Colors.OKGREEN}[2]{Colors.ENDC} Web Directory Fuzzer ({Colors.WARNING}web_fuzzer.py{Colors.ENDC})")
        print(f"{Colors.OKGREEN}[3]{Colors.ENDC} Hash Cracker         ({Colors.WARNING}hash_cracker.py{Colors.ENDC})")
        print(f"{Colors.OKGREEN}[4]{Colors.ENDC} Keylogger            ({Colors.WARNING}keylogger.py{Colors.ENDC})")
        print(f"{Colors.OKGREEN}[5]{Colors.ENDC} Subdomain Scanner    ({Colors.WARNING}subdomain_scanner.py{Colors.ENDC})")
        print(f"{Colors.FAIL}[99]{Colors.ENDC} Exit")
        print("-" * 50)
        
        try:
            choice = input(f"\n{Colors.BOLD}Select an option > {Colors.ENDC}")
            
            print("\n")
            if choice == '1':
                os.system('python network_scanner.py')
                input(f"\n{Colors.OKBLUE}Press Enter to return to main menu...{Colors.ENDC}")
            elif choice == '2':
                os.system('python web_fuzzer.py')
                input(f"\n{Colors.OKBLUE}Press Enter to return to main menu...{Colors.ENDC}")
            elif choice == '3':
                os.system('python hash_cracker.py')
                input(f"\n{Colors.OKBLUE}Press Enter to return to main menu...{Colors.ENDC}")
            elif choice == '4':
                os.system('python keylogger.py')
                input(f"\n{Colors.OKBLUE}Press Enter to return to main menu...{Colors.ENDC}")
            elif choice == '5':
                os.system('python subdomain_scanner.py')
                input(f"\n{Colors.OKBLUE}Press Enter to return to main menu...{Colors.ENDC}")
            elif choice == '99' or choice.lower() == 'q':
                print(f"{Colors.FAIL}Exiting...{Colors.ENDC}")
                sys.exit(0)
            else:
                print(f"{Colors.FAIL}Invalid option. Please try again.{Colors.ENDC}")
                input(f"{Colors.OKBLUE}Press Enter to continue...{Colors.ENDC}")
        except KeyboardInterrupt:
            print(f"\n{Colors.FAIL}Exiting...{Colors.ENDC}")
            sys.exit(0)

if __name__ == "__main__":
    # Ensure ANSI escape sequences work on Windows cmd/powershell
    if os.name == 'nt':
        os.system('color')
    main_menu()
