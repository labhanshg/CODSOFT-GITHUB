import random
import string

def generate_password(length):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length should be at least 1.")
        else:
            # Generate and display the password
            password = generate_password(length)
            print("Generated Password: ", password)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()