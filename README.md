# Password Strength Checker

A simple Python tool that evaluates the strength of a password using **Shannon entropy** and provides suggestions to improve weak passwords. It hides user input for privacy and gives qualitative feedback based on password complexity.


## Features

- Calculates password entropy based on:
  - Lowercase letters
  - Uppercase letters
  - Digits
  - Special characters
- Provides a **strength rating**: Very Weak, Weak, Moderate, Strong
- Gives **tips to improve weak passwords**
- Supports hidden password input using `getpass`


## How It Works

1. The script calculates entropy using the formula:  
```

Entropy = Length * log2(CharacterSetSize)

````
- `CharacterSetSize` depends on which types of characters are included in the password.
2. Provides feedback for missing character types or short passwords.
3. Evaluates strength:
- Very Weak: Entropy < 28 bits
- Weak: Entropy < 36 bits
- Moderate: Entropy < 60 bits
- Strong: Entropy ≥ 60 bits


## Usage

1. Clone the repository or download the `Password_Evaluator.py` file.
2. Run the script in your terminal or command prompt:
```bash
Password_Evaluator.py
````
3. Enter your password when prompted (input will be hidden).
4. Review the entropy, strength, and improvement suggestions.


## Example

=== Password Strength Checker ===

Enter a password: ********

Password Entropy: 45.17 bits
Password Strength: Moderate

Suggestions to improve your password:
 - Add special characters (e.g., !@#$%)
 - Increase password length (12+ characters recommended)
 
## Requirements

* Python 3.x
* Standard libraries: `math`, `getpass`, `string` (no external packages needed)

## License

This project is open-source and free to use.
