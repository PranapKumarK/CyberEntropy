import math
import getpass
import string

def calculate_entropy(password: str) -> float:
    """
    Calculates Shannon entropy for a password.
    Entropy = Length * log2(CharacterSetSize)
    """
    if not password:
        return 0.0

    charset_size = 0
    feedback = []

    if any(c.islower() for c in password):
        charset_size += 26
    else:
        feedback.append("Add lowercase letters")

    if any(c.isupper() for c in password):
        charset_size += 26
    else:
        feedback.append("Add uppercase letters")

    if any(c.isdigit() for c in password):
        charset_size += 10
    else:
        feedback.append("Add digits")

    if any(c in string.punctuation for c in password):
        charset_size += 32
    else:
        feedback.append("Add special characters (e.g., !@#$%)")

    if charset_size == 0:
        return 0.0, feedback

    entropy = len(password) * math.log2(charset_size)
    return entropy, feedback

def evaluate_strength(entropy: float) -> str:
    """
    Returns a qualitative strength rating based on entropy.
    """
    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Moderate"
    else:
        return "Strong"

def main():
    MIN_ENTROPY = 30  # bits

    print("=== Password Strength Checker ===")
    password = getpass.getpass("Enter a password: ")  # hides input for privacy

    entropy, feedback = calculate_entropy(password)
    strength = evaluate_strength(entropy)

    print(f"\nPassword Entropy: {entropy:.2f} bits")
    print(f"Password Strength: {strength}")

    if entropy < MIN_ENTROPY or feedback:
        print("\nSuggestions to improve your password:")
        if feedback:
            for tip in feedback:
                print(f" - {tip}")
        if len(password) < 12:
            print(" - Increase password length (12+ characters recommended)")

    else:
        print("Your password is strong and secure ✅")

if __name__ == "__main__":
    main()
