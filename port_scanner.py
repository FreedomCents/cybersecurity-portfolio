import socket

def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Port {port}: OPEN")

if __name__ == "__main__":
    target_host = input("Enter target host (e.g., 127.0.0.1): ")
    start = int(input("Enter start port (e.g., 20): "))
    end = int(input("Enter end port (e.g., 1024): "))
    scan_ports(target_host, start, end)
