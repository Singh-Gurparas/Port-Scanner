import socket
from colorama import Fore, Style, init
from datetime import datetime
import time

# Initialize colorama
init(autoreset=True)

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown"

def scan_ports(target, ports):
    try:
        ip = socket.gethostbyname(target)
        print(f"\n{Fore.CYAN}Target: {target}")
        print(f"IP Address: {ip}")
        print(f"Scan started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}\n")

        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            start = time.time()
            result = sock.connect_ex((target, port))
            end = time.time()
            duration = round((end - start) * 1000, 2)  # in milliseconds
            service = get_service_name(port)

            if result == 0:
                print(f"{Fore.GREEN}[OPEN] Port {port:<5} | Service: {service:<10} | Response: {duration} ms")
            else:
                print(f"{Fore.RED}[CLOSED] Port {port:<5} | Service: {service:<10} | Response: {duration} ms")
            sock.close()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Scan interrupted by user.")
    except socket.gaierror:
        print(f"{Fore.RED}[!] Could not resolve hostname.")
    except socket.error:
        print(f"{Fore.RED}[!] Could not connect to server.")

def main():
    print(f"{Fore.BLUE}🔍 Advanced Python Port Scanner 🔍{Style.RESET_ALL}")
    target = input("Enter target (IP or domain): ").strip()

    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 8080, 8443]
    scan_ports(target, common_ports)

if __name__ == "__main__":
    main()
