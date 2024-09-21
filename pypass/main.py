import sys
import os
from os.path import join as jn, abspath, dirname
import pkg_resources

# Determine if the script is being run as standalone or as a package
is_standalone = __name__ == "__main__"

# Import based on execution context
if is_standalone:
    from app.cli.pypass_cli import main as cli_main
    from app.gui.desktop.pypass_gui import main as desktop_main
    from app.gui.web.pypass_web import main as web_main
else:
    from pypass.app.cli.pypass_cli import main as cli_main
    from pypass.app.gui.desktop.pypass_gui import main as desktop_main
    from pypass.app.gui.web.pypass_web import main as web_main

def create_file_if_not_exists(file_path):
    # Create the file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("")

def main():
    # Define the base path for the passwords directory
    base_path = abspath(jn(dirname(__file__), 'passwords'))
    
    # For package execution, also get the installation directory
    package_base_path = pkg_resources.resource_filename('pypass', 'passwords')

    # Define the path for password files
    passwords_md_path = jn(base_path, 'passwords.md')
    passwords_db_path = jn(base_path, 'passwords.db')
    
    # Define paths for package execution
    package_passwords_md_path = jn(package_base_path, 'passwords.md')
    package_passwords_db_path = jn(package_base_path, 'passwords.db')

    # Check and create password files if not exist
    if is_standalone:
        # Ensure the passwords directory exists for standalone execution
        if not os.path.exists(base_path):
            os.makedirs(base_path)
            print(f"Created directory: {base_path}")

        create_file_if_not_exists(passwords_md_path)
        create_file_if_not_exists(passwords_db_path)
    else:
        # Ensure the package passwords directory exists
        if not os.path.exists(package_base_path):
            os.makedirs(package_base_path)
            print(f"Created package directory: {package_base_path}")

        create_file_if_not_exists(package_passwords_md_path)
        create_file_if_not_exists(package_passwords_db_path)

    # Command-line argument handling
    if len(sys.argv) == 1:
        # No arguments, default to CLI 
        cli_main()  
        return

    command = sys.argv[1].lower()

    if command == 'cli':
        cli_main()
    elif command == 'desktop':
        desktop_main()
    elif command == 'web':
        web_main()
    else:
        print(f"Unknown command: {command}")
        print("Commands: cli, desktop, web")

if __name__ == "__main__":
    main()