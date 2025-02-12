import os
import random
import string
import pyperclip

ASCII_ART = """
8888888888888888888888888888888888888888888888888888888888888888888888
8888888888888888888888888888888888888888888888888888888888888888888888
888888888888888888888888888888P""  ""988888888888888888888888888888888
888888888888888888888P"88888P          988888"988888888888888888888888
888888888888888888888  "9888            888P"  88888888888888888888888
88888888888888888888888bo "9  d8o  o8b  P" od8888888888888888888888888
88888888888888888888888888bob 98"  "8P dod8888888888888888888888888888
88888888888888888888888888888    db    8888888888888888888888888888888
8888888888888888888888888888888      888888888888888888888888888888888
8888888888888888888888888888P"9bo  odP"9888888888888888888888888888888
8888888888888888888888888P" od88888888bo "9888888888888888888888888888
88888888888888888888888   d88888888888888b   8888888888888888888888888
888888888888888888888888oo8888888888888888oo88888888888888888888888888
8888888888888888888888888888888888888888888888888888888888888888888888
"""

def welcome_screen():
    """Displays a welcome screen with ASCII art and some nice formatting."""
    print("\n" + "="*70)
    print(" "*15 + "WELCOME TO THE RANDOM PASSWORD GENERATOR")
    print("-"*70)
    print(ASCII_ART)
    print("-"*70)
    print(" "*12 +"This tool lets you generate random passwords!")
    print(" "*17 + "Program created by: Benjamin Barish")
    print("="*70)

def get_user_preferences():
    """Collects the password preferences from the user with validation."""
    while True:
        try:
            # Validate password length
            length = int(input("\nEnter the desired password length: "))
            if length <= 0:
                print("Password length must be a positive integer greater than zero.")
                continue  # Re-prompt the user
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

    # Validate preference inputs (y/n)
    while True:
        use_uppercase = input("Include uppercase letters? (y/n): ").lower()
        if use_uppercase not in ["y", "n"]:
            print("Please enter 'y' or 'n'.")
            continue
        break
    
    while True:
        use_lowercase = input("Include lowercase letters? (y/n): ").lower()
        if use_lowercase not in ["y", "n"]:
            print("Please enter 'y' or 'n'.")
            continue
        break
    
    while True:
        use_numbers = input("Include numbers? (y/n): ").lower()
        if use_numbers not in ["y", "n"]:
            print("Please enter 'y' or 'n'.")
            continue
        break
    
    while True:
        use_special_chars = input("Include special characters? (y/n): ").lower()
        if use_special_chars not in ["y", "n"]:
            print("Please enter 'y' or 'n'.")
            continue
        break

    # Return all preferences
    return length, use_uppercase == "y", use_lowercase == "y", use_numbers == "y", use_special_chars == "y"

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    # Define the character sets based on user preferences
    character_set = ""
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_numbers:
        character_set += string.digits
    if use_special_chars:
        character_set += string.punctuation

    # Generate the password
    password = "".join(random.choice(character_set) for _ in range(length))
    return password

def main():
    # Check if the welcome message has been displayed before
    flag_file = "welcome_shown.flag"
    if not os.path.exists(flag_file):
        welcome_screen()  # Display the welcome screen with ASCII art and description
        with open(flag_file, 'w') as file:
            file.write("Welcome shown")  # Create the flag file

    while True:
        # Get user preferences and generate password
        length, use_uppercase, use_lowercase, use_numbers, use_special_chars = get_user_preferences()

        # Generate the password
        password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)

        # Display the password
        print("\nGenerated Password:", password, "\n")

        # Copy password to clipboard
        pyperclip.copy(password)
        print("Password copied to clipboard.")

        # Ask the user if they want to generate another password
        another_run = input("\nWould you like to generate another password? (y/n): ").lower()
        if another_run != "y":
            print("\nExiting the password generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
