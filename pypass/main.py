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
    from database.connect import PasswordDatabase
else:
    from pypass.app.cli.pypass_cli import main as cli_main
    from pypass.app.gui.web.pypass_web import main as web_main
    from pypass.app.gui.desktop.pypass_gui import main as gui_main
    from pypass.database.connect import PasswordDatabase


class PasswordFileManager:
    """Manages the creation and verification of password-related files and directories."""

    def __init__(self, base_path: str) -> None:
        """Initialize PasswordFileManager with the base path for password files."""
        self.base_path = base_path
        self.passwords_md_path = jn(base_path, 'passwords.md')
        self.passwords_db_path = jn(base_path, 'passwords.db')
        self.ensure_directories()

    def ensure_directories(self) -> None:
        """Ensure the base directory exists."""
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
            print(f"Created directory: {self.base_path}")

    def create_file_if_not_exists(self, file_path: str) -> None:
        """Create a file if it does not already exist."""
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write("")

    def setup_files(self) -> None:
        """Check and create necessary password files."""
        self.create_file_if_not_exists(self.passwords_md_path)
        self.create_file_if_not_exists(self.passwords_db_path)


class PasswordManagerApp:
    """Main application class for managing password operations."""

    def __init__(self) -> None:
        """Initialize the PasswordManagerApp."""
        self.base_path = self.get_base_path()
        self.db_manager = PasswordDatabase()
        self.file_manager = PasswordFileManager(self.base_path)

    def get_base_path(self) -> str:
        """Determine the base path for the application."""
        if is_standalone:
            return abspath(jn(dirname(__file__), 'passwords'))
        else:
            try:
                return pkg_resources.resource_filename('pypass', 'passwords')
            except Exception:
                return abspath(jn(dirname(__file__), 'passwords'))

    def setup(self) -> None:
        """Set up the application by ensuring files and tables are created."""
        self.file_manager.setup_files()
        self.db_manager.create_table()

    def run_cli(self) -> None:
        """Run the CLI version of the app."""
        cli_main()

    def run_web(self) -> None:
        """Run the web version of the app."""
        web_main()

    def run_gui(self) -> None:
        """Run the GUI version of the app."""
        gui_main()

    def handle_command(self) -> None:
        """Handle the user's command-line input."""
        if len(sys.argv) < 2:
            self.run_cli()
            return

        command = sys.argv[1].lower()

        if command == 'web':
            self.run_web()
        elif command == 'gui':
            self.run_gui()
        else:
            self.run_cli()


def main() -> None:
    """Main entry point for the password manager app."""
    app = PasswordManagerApp()
    app.setup()
    app.handle_command()


if __name__ == "__main__":
    main()
