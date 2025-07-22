import random
import string
def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice(string.punctuation))
    
    remaining_length = length - len(password)
    password.extend(random.choice(chars) for _ in range(remaining_length))
    random.shuffle(password)

    return ''.join(password)

def get_user_input():
    print("--- PASSWORD GENERATOR ---")

    try:
        length = int(input("Enter password length (8-128): "))
        if length < 8 or length > 128:
            print("Length must be between 8 and 128. Using default 12.")
            length = 12
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    return length, use_uppercase, use_digits, use_special

def main():
    length, use_uppercase, use_digits, use_special = get_user_input()
    password = generate_password(length, use_uppercase, use_digits, use_special)
    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
