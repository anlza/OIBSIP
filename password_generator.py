import random
import string
import pyperclip

print("🔐 Advanced Password Generator")
print("--------------------------------")

try:
   
    length = int(input("Enter password length: "))

    if length <= 0:
        print(" Length must be positive.")
        exit()

   
    use_letters = input("Include letters? (y/n): ").lower()
    use_numbers = input("Include numbers? (y/n): ").lower()
    use_symbols = input("Include symbols? (y/n): ").lower()

    exclude_chars = input("Enter characters to exclude (optional): ")

    characters = ""

    if use_letters == "y":
        characters += string.ascii_letters
    if use_numbers == "y":
        characters += string.digits
    if use_symbols == "y":
        characters += string.punctuation

    
    characters = "".join(c for c in characters if c not in exclude_chars)

    if not characters:
        print(" No valid characters available.")
        exit()

    password = "".join(random.choice(characters) for _ in range(length))

    print("\n Generated Password:")
    print(password)

   
    strength = "Weak"

    if length >= 8 and use_letters == "y" and use_numbers == "y":
        strength = "Medium"
    if length >= 12 and use_letters == "y" and use_numbers == "y" and use_symbols == "y":
        strength = "Strong"

    print(f" Strength: {strength}")

   
    copy = input("Copy to clipboard? (y/n): ").lower()
    if copy == "y":
        pyperclip.copy(password)
        print(" Password copied to clipboard!")

except ValueError:
    print(" Invalid input. Please enter numbers only.")
except Exception as e:
    print(" Unexpected error:", e)