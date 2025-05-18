import socket
from colorama import Fore, init
from datetime import datetime
import time

# Initialize colorama with autoreset to avoid manual resets
init(autoreset=True)

# Banner display
def banner():
    print(Fore.RED + r"""
██████╗  ██████╗ ██████╗ ████████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝     ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝   ██║█████╗  ██████  ██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██║   ██║██╔██═╝    ██║╚════╝      ██  ██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  █     ██║            ██  ╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝ ╚═╝    ╚═╝        ████╚═╝   ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  ╝                                                                                           
    """)
    print(Fore.CYAN + "The Ultimate Python Port Scanner\n")

# Get service name from port
def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown"

# Port scanning logic
def scan_ports(target, ports):
    try:
        ip = socket.gethostbyname(target)
        print(Fore.YELLOW + "📌 Target Information")
        print(Fore.GREEN + f"{'Target:'.ljust(15)} {target}")
        print(f"{'IP Address:'.ljust(15)} {ip}")
        print(f"{'Scan started:'.ljust(15)} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        print(Fore.YELLOW + "🔎 Port Scan Results")
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            start = time.time()
            result = sock.connect_ex((target, port))
            end = time.time()
            duration = round((end - start) * 1000, 2)  # ms
            service = get_service_name(port)

            if result == 0:
                print(f"{Fore.GREEN}[OPEN]   Port {str(port).ljust(5)} | Service: {service.ljust(15)} | Response: {duration} ms")
            else:
                print(f"{Fore.RED}[CLOSED] Port {str(port).ljust(5)} | Service: {service.ljust(15)} | Response: {duration} ms")
            sock.close()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] Scan interrupted by user.")
    except socket.gaierror:
        print(f"{Fore.RED}[!] Could not resolve hostname.")
    except socket.error:
        print(f"{Fore.RED}[!] Could not connect to server.")

# Main entry
def main():
    banner()
    target = input(Fore.CYAN + "Enter target (IP or domain): ").strip()

    # Common ports (customize as needed)
    common_ports = [
        21, 22, 23, 25, 53, 80, 110, 139,
        143, 443, 445, 3306, 3389, 8080, 8443
    ]
    scan_ports(target, common_ports)

if __name__ == "__main__":
    main()
