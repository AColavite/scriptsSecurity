import bcrypt # type: ignore
import getpass

def generate_hashBcrypt():
    senha = getpass.getpass("Enter the password to generate the hash (bcrypt): ")
    generatedHash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
    print(f"\nGenerated hash (bcrypt) : \n{generatedHash.decode()}")

if __name__ == "__main__":
    generate_hashBcrypt()
    