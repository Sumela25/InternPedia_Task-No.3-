import secrets
import string
import pyperclip

# Function to generate a secure random password
def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")
    
    # Create the character pool based on user preferences
    char_pool = ''
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    # If no character type is selected
    if not char_pool:
        raise ValueError("No character types selected. Please select at least one type (uppercase, lowercase, digits, symbols).")

    # Generate the password
    password = ''.join(secrets.choice(char_pool) for _ in range(length))
    return password

# Function to generate multiple passwords
def generate_multiple_passwords(count, length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    if count <= 0:
        raise ValueError("The count must be greater than 0.")
    
    passwords = []
    for _ in range(count):
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        passwords.append(password)
    return passwords

# Function to display passwords in a user-friendly format
def display_passwords(passwords):
    print("\nGenerated Passwords:")
    for i, password in enumerate(passwords, 1):
        print(f"{i}: {password}")

# Function to copy the password to clipboard
def copy_to_clipboard(password):
    pyperclip.copy(password)
    print("\nPassword copied to clipboard!")

# Main function
def main():
    try:
        # Input from user
        length = int(input("Enter password length: "))
        count = int(input("How many passwords do you want to generate? "))
        
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        
        # Generate passwords
        passwords = generate_multiple_passwords(count, length, use_uppercase, use_lowercase, use_digits, use_symbols)
        
        # Display passwords
        display_passwords(passwords)
        
        # Option to copy one of the passwords to clipboard
        copy_choice = input("\nDo you want to copy one of the passwords to clipboard? (y/n): ").strip().lower()
        if copy_choice == 'y':
            password_index = int(input("Enter the password number to copy: ")) - 1
            if 0 <= password_index < len(passwords):
                copy_to_clipboard(passwords[password_index])
            else:
                print("Invalid password number.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
