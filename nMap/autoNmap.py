import nmap

def scan(target, ports="1-1000"):
    nm = nmap.PortsScanner()
    nm.scan(target, ports, arguments="-sv")

    for host in nm.all_hosts():
        print(f"host: `{host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                print(f"port: {port}, State: {nm[host][proto][port]['state']}")

target_ip = input("Enter target ip:")
scan(target_ip)