import socket
import threading
import re

# configurar server proxy
HOST = "0.0.0.0"
PORT = 8080
BLACKLIST = [
    r"union.*select", # SQL Injection
    r"cmd=.*",  # Execução de comandos remotos
    r"/etc/passwd"  # Tentativas de acessar arquivos do sistema
    r"<script>",    # XSS
]

def handle_client(client_socket):
    request = client_socket.recv(1024).decode("utf-8")
    print(f"\n[+] Receiving request: \n{request}")

    # Verifica se requisição contém padrao bloqueado
    for pattern in BLACKLIST:
        if re.search(pattern, request, re.IGNORECASE):
            print(f"[!] Requisição bloqueada: {pattern}")
            client_socket.send(b"HTTP/1.1 403 Forbidden\r\n\r\nBlocked by security filter!")
            client_socket.close()
            return

    # Caso passe, repassa p servidor real
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(("www.google.com", 80))
    server_socket.send(request.encode("utf-8"))

    response = server_socket.recv(4096)
    client_socket.send(response)

    client_socket.close()
    server_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(HOST, PORT)
    server.listen(5)
    print(f"[*] Proxy rodando em {HOST}:{PORT}")

    while True:
        client.socket, addr = server.accept()
        print(f"[*] Conexão recebida em {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()