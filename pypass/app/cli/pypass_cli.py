import secrets
import string
import argparse

def generate_password(length=12, exclude=None):
    # Define the alphabet
    alphabet = string.ascii_letters + string.digits + string.punctuation
    
    # Exclude specified characters
    if exclude:
        exclude_set = set(exclude)  # Create a set from the exclude string
        alphabet = ''.join(char for char in alphabet if char not in exclude_set)
    
    # Generate the password
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")
    parser.add_argument("-e", "--exclude", type=str, help="Characters to exclude (no spaces)")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the exclude characters, stripping spaces
    exclude_characters = args.exclude if args.exclude else ""

    # Generate the password using the provided length and excluded characters
    password = generate_password(args.length, exclude_characters)
    print(f"Generated random password: {password}")

if __name__ == "__main__":
    main()