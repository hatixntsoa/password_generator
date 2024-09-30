import secrets
import string
import argparse
import pyperclip
import os
from datetime import datetime
from importlib.metadata import version, PackageNotFoundError
from typing import Optional

# Database import
from sys import path
from os.path import abspath as abs, join as jn, dirname as dir
path.append(abs(jn(dir(__file__), '..', '..')))

from database.connect import PasswordDatabase

# ANSI escape codes for styling
light_blue = "\033[94m"
reset = "\033[0m"
bold = "\033[1m"

# Hardcoded version when run standalone
__version__ = "0.2.7"


class PasswordGenerator:
    """Manages password generation, evaluation, and storage."""

    def __init__(self) -> None:
        """Initialize PasswordManager."""
        self.file_path = self.__get_passwords_file_path()
        self.db_manager = PasswordDatabase()
        self.password_length = 12
        self.exclude_set = set()

    def __get_passwords_file_path(self) -> str:
        """Get the path to the markdown file where passwords are stored."""
        current_dir = dir(abs(__file__))
        return jn(current_dir, "..", "..", "passwords", "passwords.md")

    @staticmethod
    def __get_version() -> str:
        """Get the installed package version or return the hardcoded version."""
        try:
            return version('pypass-tool')
        except PackageNotFoundError:
            return __version__
        
    def set_password_length(self, length: int) -> None:
        """Set the desired length for the generated passwords."""
        self.password_length = length

    def exclude_characters(self, exclude: Optional[str]) -> None:
        """Set characters to be excluded from the generated passwords."""
        if exclude:
            self.exclude_set = set(exclude)

    @staticmethod
    def evaluate_strength(password: str) -> str:
        """Evaluate password strength based on length."""
        if len(password) < 8:
            return "Very Weak"
        elif len(password) < 12:
            return "Weak"
        elif len(password) < 16:
            return "Moderate"
        else:
            return "Strong"
        
    def generate_password(self) -> str:
        """Generate a random password with the specified length and excluded characters."""
        alphabet = string.ascii_letters + string.digits + string.punctuation
        if self.exclude_set:
            alphabet = ''.join(char for char in alphabet if char not in self.exclude_set)
        return ''.join(secrets.choice(alphabet) for _ in range(self.password_length))

    @staticmethod
    def __input_with_default(prompt: str, default_value: str) -> str:
        """Prompt the user for input, return default value if input is empty."""
        value = input(prompt).strip()
        return value if value else default_value

    def __save_password_to_file(self, password: str, name: str, author: str, description: str, strength: str) -> None:
        """Save the generated password in a markdown file."""
        os.makedirs(dir(self.file_path), exist_ok=True)

        with open(self.file_path, 'a') as file:
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
            file.write(f"{markdown_content.replace('                ', '')}\n")


    def __show_passwords(self) -> None:
        """Fetch and display stored passwords from the database."""
        passwords = self.db_manager.fetch_passwords()
        if not passwords:
            print("No passwords found in the database.")
            return

        print("\nStored Passwords:")
        for pw in passwords:
            name, creation_date, owner, description, strength, password = pw[1:]
            print(f"\nName       : {name}")
            print(f"Description: {description}")
            print(f"Owner      : {owner}")
            print(f"Creation   : {creation_date}")
            print(f"Strength   : {strength}")
            print(f"Password   : {bold}{light_blue}{password}{reset}\n")

    def __prompt_save_password(self, password: str) -> None:
        """Prompt user to save the password and optionally save it to a file or database."""
        name = self.__input_with_default("Password Name (skippable): ", datetime.now().strftime("Password %m-%d-%Y_%H:%M"))
        author = self.__input_with_default("Password Owner (skippable): ", "PyPass Tool")
        description = self.__input_with_default("Password Description (skippable): ", "A random password")

        strength = self.evaluate_strength(password)

        save_prompt = input("\nSave in markdown? (y/n): ").strip().lower()
        if save_prompt == 'y':
            self.__save_password_to_file(password, name, author, description, strength)

        save_db_prompt = input("Save in database? (y/n): ").strip().lower()
        if save_db_prompt == 'y':
            current_time = datetime.now().strftime("%m-%d-%Y %H:%M")
            self.db_manager.insert_password(name, current_time, author, description, strength, password)

    def __copy_to_clipboard(self, password: str) -> None:
        """Copy the generated password to the clipboard."""
        pyperclip.copy(password)
        print("Copied to clipboard!\n")


def main() -> None:
    """Main function to handle password generation and management."""
    manager = PasswordGenerator()

    parser = argparse.ArgumentParser(description="Generate or manage passwords.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")
    parser.add_argument("-e", "--exclude", type=str, help="Characters to exclude (no spaces)")
    parser.add_argument("--show", action="store_true", help="Show stored passwords")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + manager.__get_version())

    args = parser.parse_args()

    if args.show:
        manager.__show_passwords()
        return

    # Set the password length and excluded characters
    manager.set_password_length(args.length)
    manager.exclude_characters(args.exclude)
    password = manager.generate_password()

    print(f"Generated random password: {bold}{light_blue}{password}{reset}")

    copy_choice = input("\nCopy to clipboard? (y/n): ").strip().lower()
    if copy_choice == 'y':
        manager.__copy_to_clipboard(password)
        manager.__prompt_save_password(password)


if __name__ == "__main__":
    main()