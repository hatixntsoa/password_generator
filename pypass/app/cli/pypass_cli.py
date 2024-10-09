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
__version__ = "0.3.1"


class PasswordGenerator:
    """Manages password generation, evaluation, and storage."""

    def __init__(self) -> None:
        """
        Initializes the PasswordGenerator class.

        - Sets the default file path for password storage by calling the `__get_passwords_file_path` method.
        - Initializes the `db_manager` object to manage password storage in the database.
        - Sets a default password length of 12 characters.
        - Initializes an empty set `exclude_set` for storing excluded characters.

        :param: None
        :return: None
        """
        self.file_path = self.__get_passwords_file_path()
        self.db_manager = PasswordDatabase()
        self.password_length = 12
        self.exclude_set = set()

    def __get_passwords_file_path(self) -> str:
        """
        Determines and returns the file path where passwords are stored in a markdown file.

        This method constructs the file path to the passwords file using the current directory 
        and appends the relative path to the "passwords.md" file located two levels above the 
        current script directory.

        :param: None
        :return: Returns the absolute path to the passwords markdown file as a string.
        """
        current_dir = dir(abs(__file__))
        return jn(current_dir, "..", "..", "passwords", "passwords.md")

    @staticmethod
    def _get_version() -> str:
        """
        Retrieves the installed version of the 'pypass-tool' package, or returns the hardcoded version.

        This method checks the installed version of the 'pypass-tool' package using the `version` method 
        from `importlib.metadata`. If the package is not installed, it returns a hardcoded default version 
        specified in `__version__`.

        :param: None
        :return: The package version as a string.
        """
        try:
            return version('pypass-tool')
        except PackageNotFoundError:
            return __version__
        
    def set_password_length(self, length: int) -> None:
        """
        Sets the desired length of the generated passwords.

        This method allows setting the password length, which will determine the number of characters 
        in the generated passwords.

        :param length: An integer representing the desired password length.
        :return: None
        """
        self.password_length = length

    def exclude_characters(self, exclude: Optional[str]) -> None:
        """
        Sets characters to be excluded from the password generation process.

        This method allows users to provide characters that should be excluded when generating 
        a password. The excluded characters are stored in `exclude_set`.

        :param exclude: A string of characters to be excluded (or None).
        :return: None
        """
        if exclude:
            self.exclude_set = set(exclude)

    @staticmethod
    def evaluate_strength(password: str) -> str:
        """
        Evaluates the strength of a given password based on its length.

        This method categorizes the strength of a password as "Very Weak", "Weak", "Moderate", 
        or "Strong" based on its character count.

        :param password: The password string to be evaluated.
        :return: A string representing the strength of the password.
        """
        if len(password) < 8:
            return "Very Weak"
        elif len(password) < 12:
            return "Weak"
        elif len(password) < 16:
            return "Moderate"
        else:
            return "Strong"

    def generate_password(self) -> str:
        """
        Generates a random password with the specified length and excluded characters.

        This method creates a password using a combination of letters, digits, and punctuation.
        If any characters are set to be excluded, they are removed from the pool of possible characters.

        :return: A randomly generated password string.
        """
        alphabet = string.ascii_letters + string.digits + string.punctuation
        if self.exclude_set:
            alphabet = ''.join(char for char in alphabet if char not in self.exclude_set)
        return ''.join(secrets.choice(alphabet) for _ in range(self.password_length))

    @staticmethod
    def __input_with_default(prompt: str, default_value: str) -> str:
        """
        Prompts the user for input, returning a default value if no input is provided.

        This method displays a prompt to the user. If the user enters an empty string, 
        the provided default value is returned instead.

        :param prompt: The prompt message to display to the user.
        :param default_value: The default value to return if the user provides no input.
        :return: The user input or the default value.
        """
        value = input(prompt).strip()
        return value if value else default_value

    def __save_password_to_file(self, password: str, name: str, author: str, description: str, strength: str) -> None:
        """
        Saves the generated password in a markdown file.

        This method stores password information, including the password itself, the creation date, 
        the owner's name, a description, and its strength, in a markdown file at the specified file path.

        :param password: The password string to save.
        :param name: The name associated with the password.
        :param author: The owner or author of the password.
        :param description: A description of the password.
        :param strength: The evaluated strength of the password.
        """
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

    def _show_passwords(self) -> None:
        """
        Fetches and displays stored passwords from the database.

        This method retrieves password entries from the database and prints them in a 
        formatted manner, showing details such as the password name, description, owner, 
        creation date, strength, and the actual password.
        """
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

    def _prompt_save_password(self, password: str) -> None:
        """
        Prompts the user to save the generated password and store it in a file or database.

        This method asks the user for optional details (name, owner, description) and then 
        allows the password to be saved either in a markdown file or in a database, based on 
        the user's input.

        :param password: The password string to save.
        """
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

    def _copy_to_clipboard(self, password: str) -> None:
        """
        Copies the generated password to the clipboard.

        This method uses the `pyperclip` library to copy the password string 
        to the system's clipboard.

        :param password: The password string to copy.
        :return: None
        """
        pyperclip.copy(password)
        print("Copied to clipboard!\n")


def main() -> None:
    """
    Main function to handle password generation and management.

    This method parses command-line arguments, generates a password (if requested), 
    displays stored passwords (if requested), and handles saving or copying passwords.
    """
    manager = PasswordGenerator()

    parser = argparse.ArgumentParser(description="Generate or manage passwords.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password")
    parser.add_argument("-e", "--exclude", type=str, help="Characters to exclude (no spaces)")
    parser.add_argument("--show", action="store_true", help="Show stored passwords")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + manager._get_version())

    args = parser.parse_args()

    if args.show:
        manager._show_passwords()
        return

    # Set the password length and excluded characters
    manager.set_password_length(args.length)
    manager.exclude_characters(args.exclude)
    password = manager.generate_password()

    print(f"Generated random password: {bold}{light_blue}{password}{reset}")

    copy_choice = input("\nCopy to clipboard? (y/n): ").strip().lower()
    if copy_choice == 'y':
        manager._copy_to_clipboard(password)
        manager._prompt_save_password(password)


if __name__ == "__main__":
    main()
