Port Scanner Script 🔍
A simple Python script to scan a list of common ports on a given target (IP address or domain). The script attempts to connect to each port and reports whether the port is open or closed. Results are saved to a text file. 📂

Features ✨
Scans a predefined list of ports.

Displays open ports and associated services. 🌐

Saves scan results to a file named ExportScan.txt. 💾

Allows for quick scanning with a 20ms timeout per port. ⏱️

Handles errors gracefully, such as target not found or interruption by the user. 🚫

Prerequisites ⚙️
Python 3.x

socket library (this is built into Python, so no external libraries are required)

Ports Scanned ⚡
The script scans the following common ports:

21 (FTP)

22 (SSH)

23 (Telnet)

25 (SMTP)

80 (HTTP)

110 (POP3)

119 (NNTP)

143 (IMAP)

443 (HTTPS)

8080 (HTTP-alt)

3389 (RDP)

Output 📊
The results are displayed in the terminal, listing the open ports along with their corresponding service names. 📜

A text file named ExportScan.txt is generated, containing the scan results. 💡

Error Handling ⚠️
If the target is not found (e.g., incorrect domain or IP), the script will print and log: # # # Target not found # # #.

If the scan is interrupted by the user, the script will gracefully exit with a message. ✋

.

Notes 📝
This script is intended for educational and personal use. Do not scan networks or systems that you do not own or have explicit permission to scan. ⚖️

Scanning can take some time depending on network speed and the number of open ports. 🕒