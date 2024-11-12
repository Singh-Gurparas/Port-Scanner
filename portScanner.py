import socket

# Function to scan a specific port
def scan_port(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)  # Set timeout for each attempt
    result = scanner.connect_ex((ip, port))  # 0 if port is open, error code otherwise
    scanner.close()
    return result == 0

# Function to scan a range of ports
def port_scanner(ip, start_port, end_port):
    print(f"Scanning IP: {ip} from port {start_port} to {end_port}")
    
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(ip, port):
            print(f"Port {port} is open")
            open_ports.append(port)
        else:
            print(f"Port {port} is closed")
    
    print("\nOpen Ports:", open_ports)

# User input for target IP and port range
ip_address = input("Enter IP address to scan: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

# Run the port scanner
port_scanner(ip_address, start_port, end_port)
