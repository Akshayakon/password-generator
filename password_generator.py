import secrets
import string

length = int(input("Password length: "))
chars = ""

if input("Include letters? (y/n): ").lower() == "y":
    chars += string.ascii_letters
if input("Include digits? (y/n): ").lower() == "y":
    chars += string.digits
if input("Include symbols? (y/n): ").lower() == "y":
    chars += string.punctuation

if chars:
    print("Password:", "".join(secrets.choice(chars) for _ in range(length)))
else:
    print("Pick at least one character type.")
