import json
import os

FILE_NAME = "diary.enc"

def save_encrypted(fernet, data: dict):
    encrypted = fernet.encrypt(json.dumps(data).encode())
    with open(FILE_NAME, "wb") as f:
        f.write(encrypted)

def load_encrypted(fernet):
    if not os.path.exists(FILE_NAME):
        return {"entries": []}

    with open(FILE_NAME, "rb") as f:
        encrypted = f.read()

    decrypted = fernet.decrypt(encrypted)
    return json.loads(decrypted.decode())