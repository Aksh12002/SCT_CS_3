# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"


def header(title):
    print(BOLD + CYAN)
    print("╔" + "═" * 46 + "╗")
    print(f"║ {title.center(44)} ║")
    print("╚" + "═" * 46 + "╝")
    print(RESET)


def section(title):
    print(BOLD + BLUE + f"\n▶ {title}" + RESET)


def success(msg):
    print(GREEN + "✔ " + msg + RESET)


def warning(msg):
    print(YELLOW + "⚠ " + msg + RESET)


def error(msg):
    print(RED + "✖ " + msg + RESET)


def strength_bar(level):
    bars = {
        "Very Weak": (1, RED),
        "Weak": (2, RED),
        "Medium": (3, YELLOW),
        "Strong": (4, GREEN),
        "Very Strong": (5, GREEN),
    }
    filled, color = bars[level]
    return color + "█" * filled + "░" * (5 - filled) + RESET

from password_checker import evaluate_password
import getpass


def main():
    header("PASSWORD STRENGTH CHECKER")

    while True:
        password = getpass.getpass(CYAN + "Enter password (hidden): " + RESET)

        if not password:
            error("Password cannot be empty")
            continue

        result = evaluate_password(password)

        section("Analysis Result")

        print("Strength :", BOLD + result["strength"] + RESET,
              strength_bar(result["strength"]))
        print("Entropy  :", f"{result['entropy']} bits")
        print("Crack Time:", result["crack_time"])
        print("Usage    :", result["recommendation"])

        if result.get("reason"):
            section("Security Issues")
            for r in result["reason"]:
                warning(r)

        if result.get("suggestion"):
            section("Suggested Strong Password")
            success(result["suggestion"])

        print("\n" + "-" * 50)
        choice = input("Check another password? (y/n): ").lower()
        if choice != "y":
            print("\n" + GREEN + "✔ Exiting Password Checker" + RESET)
            break


if __name__ == "__main__":
    main()
