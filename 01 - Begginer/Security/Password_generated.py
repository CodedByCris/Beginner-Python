import string
import random

def generate_password(length):
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer.")
    
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        number = int(input('Enter the number of characters for the password: '))
        print(generate_password(number))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()