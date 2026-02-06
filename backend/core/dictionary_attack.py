import hashlib
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WORDLIST_PATH = os.path.join(BASE_DIR, "..", "wordlists", "common_passwords.txt")

def generate_hash(password, algorithm):
    password = password.encode("utf-8")

    if algorithm == "MD5":
        return hashlib.md5(password).hexdigest()
    elif algorithm == "SHA-1":
        return hashlib.sha1(password).hexdigest()
    elif algorithm == "SHA-256":
        return hashlib.sha256(password).hexdigest()
    else:
        return None

def dictionary_attack(target_hash, algorithm):
    if not os.path.exists(WORDLIST_PATH):
        return {
            "status": "error",
            "message": "Wordlist file not found"
        }

    start_time = time.time()
    attempts = 0

    with open(WORDLIST_PATH, "r", errors="ignore") as file:
        for line in file:
            password = line.strip()
            if not password:
                continue

            attempts += 1
            hashed = generate_hash(password, algorithm)

            if hashed == target_hash:
                return {
                    "status": "success",
                    "password": password,
                    "attempts": attempts,
                    "time": round(time.time() - start_time, 2)
                }

    return {
        "status": "failed",
        "message": "Password not found in wordlist",
        "attempts": attempts,
        "time": round(time.time() - start_time, 2)
    }
