import hashlib
import itertools
import string

target_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd6a6df7f98c8b64711"

charset = string.ascii_lowercase # a-z
max_length = 5 # Max length of password

def brute_force_attack(target_hash, charset, max_length):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempt = ''.join(attempt)
            hashed_attempt = hashlib.sha256(attempt.encode()).hexdigest()
            if hashed_attempt == target_hash:
                return attempt # Encontramo a braba (senha)
    return None

# Exec # 
password = brute_force_attack(target_hash, charset, max_length)

if password:
    print(f"Password found: {password}")

else:
    print("Senha não encontrada dentro do definido")
        