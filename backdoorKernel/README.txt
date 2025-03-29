🔥 Backdoor Script - Remote Shell Access

A lightweight Python-based backdoor script that enables remote shell access to a target system. Designed for penetration testing and cybersecurity research.

⚠️ Legal Disclaimer:

This script is intended for educational purposes and authorized security testing only. Unauthorized use is illegal and could lead to legal consequences. The author takes no responsibility for misuse.

📌 Features

Establishes a reverse shell connection to an attacker-controlled machine.

Executes system commands remotely.

Supports directory navigation (cd command).

Error handling for stability.

⚙️ How It Works

The script connects to the specified attacker IP and port.

It sends a confirmation message upon successful connection.

It continuously listens for and executes received commands:

cd <dir>: Change directory.

Any other command: Executes in shell and returns output.

q: Terminates the connection.

.

🛡 Security Considerations

Use only in controlled environments (CTFs, labs, and authorized penetration tests).

Ensure the target has granted explicit permission.

Encrypt communications for stealth and security.


Made by AColavite.
Open Code.
