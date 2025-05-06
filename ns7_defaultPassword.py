import random
import string

def generate_password(length):

    if length < 8:
        print("Password length should be at least 8 for better security.")
        return None
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 8:
                print("Password length should be at least 8. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    if password:
        print(f"\nGenerated Password: {password}")
        print("Keep it secure and don't share it with anyone!")

if __name__ == "__main__":
    main()
