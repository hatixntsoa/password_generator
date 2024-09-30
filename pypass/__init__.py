from .app.cli.pypass_cli import main as cli_main
from .app.gui.desktop.pypass_gui import main as gui_main
from .app.gui.web.pypass_web import main as web_main
from .app.cli.pypass_cli import PasswordGenerator

__all__ = ["cli_main", "gui_main", "web_main", "PasswordGenerator"]