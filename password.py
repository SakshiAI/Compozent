import random
import string

def generate_password(length=12, include_digits= True,include_special_chars=True,include_uppercase=True,complexity="medium"):
    characters = string.ascii_lowercase

    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    if include_uppercase:
        characters += string.ascii_uppercase
    if complexity == "easy":
        characters += string.ascii_lowercase
    elif complexity == "medium":
        characters += string.digits + string.ascii_uppercase
    elif complexity == "hard":
        characters += string.digits + string.punctuation + string.ascii_uppercase

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    # Prompt the user for password customization options
    length = int(input("Enter the length of the password: "))
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower()
    complexity = input("Choose complexity (easy/medium/hard): ").lower()

    # Generate and print the password
    password = generate_password(length, include_digits, include_special_chars, include_uppercase ,complexity)
    print("Generated Password:", password)

