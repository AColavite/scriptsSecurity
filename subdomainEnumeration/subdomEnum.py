import dns.resolver
import sys

def enumerate_subdomains(domain):
    subdomains_found = []

    subdomain_array = ['www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk', 'ns2', 'cpanel']

    for subdom in subdomain_array:
        try:
            full_subdomain = f"{subdom}.{domain}"
            answers = dns.resolver.resolve(full_subdomain, 'A')  

            if answers:
                subdomains_found.append(full_subdomain)
                print(f"[+] Subdomínio encontrado: {full_subdomain}")

        except dns.resolver.NXDOMAIN:
            pass 
        except dns.resolver.NoAnswer:
            pass  
        except dns.resolver.LifetimeTimeout:
            print(f"[!] Tempo limite ao consultar {full_subdomain}")
        except KeyboardInterrupt:
            print("\n[!] Interrupção pelo usuário. Saindo...")
            sys.exit(0)

    return subdomains_found

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <domínio>")
        sys.exit(1)

    domain = sys.argv[1]
    print(f"Iniciando enumeração de subdomínios para {domain}...\n")
    found = enumerate_subdomains(domain)

    if found:
        print("\n[+] Enumeração concluída. Subdomínios encontrados:")
        for sub in found:
            print(f" - {sub}")
    else:
        print("\n[-] Nenhum subdomínio encontrado.")
