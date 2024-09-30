from .cli.pypass_cli import main as cli_main
from .gui.desktop.pypass_gui import main as gui_main
from .gui.web.pypass_web import main as web_main

__all__ = ["cli_main", "gui_main", "web_main"]