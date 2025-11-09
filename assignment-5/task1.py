import json
import os
import base64
import hashlib
import hmac
import secrets
from getpass import getpass

USERS_FILE = "users.json"
PBKDF2_ITERATIONS = 200_000
HASH_NAME = "sha256"
SALT_BYTES = 16
DKLEN = 32  # derived key length in bytes

def _load_users(path=USERS_FILE):
    if not os.path.exists(path):
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def _save_users(users, path=USERS_FILE):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2)

def hash_password(password):
    """
    Hash a password using PBKDF2-HMAC (sha256) with a random salt.
    Returns a dict containing base64-encoded salt, iterations and derived key.
    """
    if not isinstance(password, str):
        raise TypeError("password must be a string")
    salt = secrets.token_bytes(SALT_BYTES)
    dk = hashlib.pbkdf2_hmac(HASH_NAME, password.encode("utf-8"), salt, PBKDF2_ITERATIONS, dklen=DKLEN)
    return {
        "salt": base64.b64encode(salt).decode("ascii"),
        "iterations": PBKDF2_ITERATIONS,
        "hash": base64.b64encode(dk).decode("ascii"),
        "algo": f"pbkdf2_{HASH_NAME}"
    }

def verify_password(stored_entry, password):
    """
    Verify a password against a stored entry produced by hash_password.
    Uses hmac.compare_digest for constant-time comparison.
    """
    if not stored_entry or "salt" not in stored_entry:
        return False
    salt = base64.b64decode(stored_entry["salt"])
    iterations = int(stored_entry.get("iterations", PBKDF2_ITERATIONS))
    expected = base64.b64decode(stored_entry["hash"])
    dk = hashlib.pbkdf2_hmac(HASH_NAME, password.encode("utf-8"), salt, iterations, dklen=len(expected))
    return hmac.compare_digest(dk, expected)

def register_user(username, password):
    users = _load_users()
    if username in users:
        raise ValueError("username already exists")
    users[username] = hash_password(password)
    _save_users(users)

def authenticate_user(username, password):
    users = _load_users()
    entry = users.get(username)
    if not entry:
        return False
    return verify_password(entry, password)

def cli_register():
    print("=== Register ===")
    username = input("Username: ").strip()
    if not username:
        print("Username required.")
        return
    pwd = getpass("Password: ")
    pwd2 = getpass("Confirm password: ")
    if pwd != pwd2:
        print("Passwords do not match.")
        return
    try:
        register_user(username, pwd)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("Registered successfully.")

def cli_login():
    print("=== Login ===")
    username = input("Username: ").strip()
    pwd = getpass("Password: ")
    ok = authenticate_user(username, pwd)
    if ok:
        print("Login successful.")
    else:
        print("Invalid credentials.")

def main():
    while True:
        print("\n1) Register\n2) Login\n3) Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            cli_register()
        elif choice == "2":
            cli_login()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()