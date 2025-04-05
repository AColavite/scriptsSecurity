import getpass
import os
import bcrypt # type: ignore
import hashlib
from dotenv import load_dotenv # type: ignore

def require_authentication(Input_password=None):
    stored_hash = os.getenv("ADMIN_PASSWORD_BCRYPT")

    if not stored_hash:
        print("Error: ADMIN_PASSWORD_BCRYPT not defined on .env")
        exit(1)

    if not Input_password is None or Input_password.strip():
        import getpass
        Input_password = getpass.getpass("Enter ADMIN password")

    if not Input_password:
        print("Error: No password provided")
        exit(1)
             
    if not bcrypt.checkpw(Input_password.encode(), stored_hash.strip().encode()):
        print("Autenticação falhou. Senha incorreta.")
        exit(1)
        