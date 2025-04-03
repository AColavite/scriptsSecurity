import socket

def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((target, port))
        print(f"[+] Port {port} is open")
        s.close()
    except:
        pass # PortIsClosed

def scan(target, ports):
    print(f"Scanning {target}. . .")
    for port in ports:
        scan_port(target, port)

target_ip = input("Enter target IP: ")
ports = range(1, 1025) #Scanning1024ports
scan(target_ip, ports)
