import secrets
import string
import argparse
import pyperclip
import os
from datetime import datetime

# import database connection
from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from database.connect import insert_password

# define ansi codes
light_blue = "\033[94m"
reset = "\033[0m"
bold = "\033[1m"

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

def evaluate_strength(password):
    if len(password) < 8:
        return "Very Weak"
    elif len(password) < 12:
        return "Weak"
    elif len(password) < 16:
        return "Moderate"
    else:
        return "Strong"

def save_password_to_file(password, name, author, description, strength):
    # Get the directory of the currently running script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the path for the passwords file relative to the current script
    file_path = os.path.join(current_dir, "..", "..", "passwords", "passwords.md")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the password to the file
    with open(file_path, 'a') as file:
        current_time = datetime.now().strftime("%m-%d-%Y %H:%M")
        markdown_content = f"""\
            - ### ``{name}``   
            **Date of Creation**: {current_time}  
            **Owner**           : {author}  
            **Description**     : {description}  
            **Strength**        : {strength}  
            
            ```markdown
            {password}
            ```\
        """
        
        # Write to file without tabulations for code readability
        file.write(f"{markdown_content.replace('            ', '')}\n")

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
    print(f"Generated random password: ")
    print(f"{bold}{light_blue}{password}{reset}")

    while True:
        copy_choice = input("\nCopy to clipboard? (y/n): ").strip().lower()
        if copy_choice == 'y':
            pyperclip.copy(password)
            print("Copied to clipboard!")
            save_prompt = input("\nSave in markdown ? (y/n): ").strip().lower()
            if save_prompt == 'y':
                name = input("\nPassword Name (skippable): ").strip()
                if not name:
                    name = datetime.now().strftime("Password %m-%d-%Y_%H:%M")
                author = input("Password Owner (skippable): ").strip()
                if not author:
                    author = "PyPass Tool"
                description = input("Password Description (skippable): ").strip()
                if not description:
                    description = "A random passord"

                strength = evaluate_strength(password)
                save_password_to_file(password, name, author, description, strength)
                
                # ask to save to the database
                save_database_prompt = input("\nSave in database ? (y/n): ").strip().lower()
                if save_database_prompt == 'y':
                    # Save to the database
                    current_time = datetime.now().strftime("%m-%d-%Y %H:%M")
                    insert_password(name, current_time, author, description, strength, password)
            break
        elif copy_choice == 'n':
            break

if __name__ == "__main__":
    main()