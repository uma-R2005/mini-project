import re
import math
import time
import csv
import logging
import getpass
from datetime import datetime

# ---------------- Logging ----------------
logging.basicConfig(filename="trainer.log", level=logging.INFO,
                    format="%(asctime)s - %(message)s")

# ---------------- Dictionary ----------------
COMMON_WORDS = [
    "password", "admin", "welcome", "qwerty", "letmein", "monkey", "dragon",
    "football", "baseball", "login", "abc123", "iloveyou", "sunshine",
    "princess", "hello", "freedom", "whatever", "qazwsx", "trustno1"
]

# ---------------- Password Scoring ----------------
def score_pwd(password):
    logging.info("Called score_pwd")

    length = len(password)
    score = 0
    reasons = []

    # length score
    if length >= 8:
        score += 2
        reasons.append("+2 for length ≥ 8")
    else:
        reasons.append("0 points: length < 8 (too short)")

    if length >= 12:
        score += 2
        reasons.append("+2 for length ≥ 12")
    if length >= 16:
        score += 2
        reasons.append("+2 for length ≥ 16")

    # complexity
    if re.search(r"[a-z]", password):
        score += 1
        reasons.append("+1 for lowercase letter")
    else:
        reasons.append("0 points: missing lowercase letter")

    if re.search(r"[A-Z]", password):
        score += 1
        reasons.append("+1 for uppercase letter")
    else:
        reasons.append("0 points: missing uppercase letter")

    if re.search(r"[0-9]", password):
        score += 1
        reasons.append("+1 for digit")
    else:
        reasons.append("0 points: missing digit")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
        reasons.append("+1 for special character")
    else:
        reasons.append("0 points: missing special character")

    # dictionary penalty
    lowered = password.lower()
    if any(word in lowered for word in COMMON_WORDS):
        score -= 2
        reasons.append("-2 for containing dictionary word")

    # keep score between 0–10
    score = max(0, min(10, score))

    # entropy calculation
    pool = 0
    if re.search(r"[a-z]", password):
        pool += 26
    if re.search(r"[A-Z]", password):
        pool += 26
    if re.search(r"[0-9]", password):
        pool += 10
    if re.search(r"[^a-zA-Z0-9]", password):
        pool += 32
    entropy = length * math.log2(pool) if pool else 0

    # strength label
    if score < 4:
        strength = "Weak"
    elif score < 8:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, entropy, strength, reasons

# ---------------- Memory Phase ----------------
def memory_phase():
    print("\nRemember the password you entered.")
    print("⏳ You have 2 minutes to keep it in mind...")
    time.sleep(120)  # wait full 2 minutes silently

# ---------------- Recall Phase ----------------
def recall_phase(original_pwd):
    print("\nTime’s up! Now re-enter your password to check memory:")
    attempt = getpass.getpass("Enter password again: ")
    return attempt == original_pwd

# ---------------- Save Results ----------------
def save_results(password, score, result, entropy, strength):
    with open("trainer_results.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            password, score, entropy, strength, result
        ])

# ---------------- Main ----------------
def main():
    # user input hidden
    user_pwd = getpass.getpass("Enter a password to test: ")
    score, entropy, strength, reasons = score_pwd(user_pwd)

    print(f"\nPassword Score: {score}/10")
    print(f"Entropy: {entropy:.2f} bits → Strength: {strength}")
    print("\nReasoning:")
    for r in reasons:
        print(" -", r)

    # memory + recall
    memory_phase()
    result = recall_phase(user_pwd)

    # save results
    save_results(user_pwd, score, "Success" if result else "Fail", entropy, strength)
    if result:
        print("✅ Correct! Good memory.")
    else:
        print("❌ Incorrect. Try again.")
    print("Done. Check trainer.log and trainer_results.csv for logs.")

if __name__ == "__main__":
    main()
