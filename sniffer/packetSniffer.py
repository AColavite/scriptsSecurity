from scapy.all import *

def sniff(packages):
    if packages.haslayer(tcp): 
        ipSource = packages[IP].src
        ipDestiny = packages[IP].dst
        portSource = packages[TCP].sport
        portDestiny = packages[TCP].dport
        print(f"{ipSource} : {portSource}  {ipDestiny} : {portDestiny}")

sniff(prn=sniff, filter="tcp", iface="Wi-Fi")