import re
import math

def load_common_passwords():
    with open("common_passwords.txt", "r") as f:
        return set(p.strip().lower() for p in f.readlines())


COMMON_PASSWORDS = load_common_passwords()


def calculate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"[0-9]", password): charset += 10
    if re.search(r"[^A-Za-z0-9]", password): charset += 32

    if charset == 0:
        return 0

    return round(len(password) * math.log2(charset), 2)


def estimate_crack_time(entropy):
    guesses_per_second = 1e9  # offline attack
    seconds = (2 ** entropy) / guesses_per_second

    if seconds < 60:
        return "Seconds"
    elif seconds < 3600:
        return "Minutes"
    elif seconds < 86400:
        return "Hours"
    elif seconds < 31536000:
        return "Days"
    else:
        return "Years"


def suggest_stronger_password(password):
    suggestion = password

    if not re.search(r"[A-Z]", suggestion):
        suggestion += "A"
    if not re.search(r"[a-z]", suggestion):
        suggestion += "a"
    if not re.search(r"[0-9]", suggestion):
        suggestion += "9"
    if not re.search(r"[^A-Za-z0-9]", suggestion):
        suggestion += "@"

    if len(suggestion) < 12:
        suggestion += "Xy!"

    return suggestion


def evaluate_password(password):
    feedback = []
    score = 0

    if password.lower() in COMMON_PASSWORDS:
        return {
            "strength": "Very Weak",
            "reason": ["Password found in common password list"],
            "entropy": 0,
            "crack_time": "Instant",
            "recommendation": "Not suitable for any use"
        }

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Missing uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Missing lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Missing number")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Missing special character")

    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(entropy)

    strength_map = {
        1: "Very Weak",
        2: "Weak",
        3: "Medium",
        4: "Strong",
        5: "Very Strong"
    }

    strength = strength_map.get(score, "Very Weak")

    if entropy < 40:
        recommendation = "Social Media only"
    elif entropy < 60:
        recommendation = "Email / General Use"
    else:
        recommendation = "Banking / Admin Accounts"

    return {
        "strength": strength,
        "reason": feedback,
        "entropy": entropy,
        "crack_time": crack_time,
        "recommendation": recommendation,
        "suggestion": suggest_stronger_password(password)
    }
