import secrets
import string
import argparse

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Generate the password using the provided length
    password = generate_password(args.length)
    print(f"Generated random password: {password}")

if __name__ == "__main__":
    main()
