import sys
import os
from os.path import join as jn, abspath, dirname
import pkg_resources

# Determine if the script is being run as standalone or as a package
is_standalone = __name__ == "__main__"

# Import based on execution context
if is_standalone:
    from app.cli.pypass_cli import main as cli_main
    from app.gui.web.pypass_web import main as web_main
    from app.gui.desktop.pypass_gui import main as gui_main
    from database.connect import create_table
else:
    from pypass.app.cli.pypass_cli import main as cli_main
    from pypass.app.gui.web.pypass_web import main as web_main
    from pypass.app.gui.desktop.pypass_gui import main as gui_main
    from pypass.database.connect import create_table

def create_file_if_not_exists(file_path):
    # Create the file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write("")

def main():
    # Define the base path for the passwords directory
    base_path = abspath(jn(dirname(__file__), 'passwords'))
    
    # Fallback to standalone path if package path retrieval fails
    try:
        package_base_path = pkg_resources.resource_filename('pypass', 'passwords')
    except Exception:
        package_base_path = base_path

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
        create_table()
    else:
        # Ensure the package passwords directory exists
        if not os.path.exists(package_base_path):
            os.makedirs(package_base_path)
            print(f"Created package directory: {package_base_path}")

        create_file_if_not_exists(package_passwords_md_path)
        create_file_if_not_exists(package_passwords_db_path)
        create_table()

    # Command-line argument handling
    if len(sys.argv) < 2:
        # no arguments, call the cli
        cli_main()
        return

    command = sys.argv[1].lower()

    if command == 'web':
        web_main()
    elif command == 'gui':
        gui_main()
    else:
        cli_main()
        return

if __name__ == "__main__":
    main()