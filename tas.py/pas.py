import random
import string
def generate_password(length):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = lower_case + upper_case + digits + special_characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        if length < 8:
            print("It's recommended to have a password of at least 8 characters for better security.")
    except ValueError:
        print("Please enter a valid number for the password length.")
        return
    password = generate_password(length)
    print(f"Generated password: {password}")
if __name__ == "__main__":
    main()