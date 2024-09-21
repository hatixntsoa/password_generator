# PyPass Tool

<p align="center">
 <img height="150" src="https://raw.githubusercontent.com/h471x/password_generator/master/imgs/pypass.png"/>
</p>

<div align="center">

<p>

``pypass-tool`` is a Python-based password management utility that allows users to generate random passwords and store them inside a file for easy recall. It will check for password strength and provide options to adjust the length of the password and exclude specific characters. Users can choose to generate passwords using the command line (CLI), a web browser, or a desktop app.

</p>

</div>

## Features

- **Command-Line Interface (CLI)**: Default interface for generating and managing passwords from the terminal.
- **Desktop GUI**: Simple graphical interface using Tkinter for generating passwords on your desktop.
- **Web Interface**: Web-based interface built with Flask for managing passwords through a browser.

## Project Structure

```
.
├── imgs
│   └── pypass.png
│
├── LICENSE.md
├── pypass
│   ├── app
│   │   ├── cli
│   │   │   ├── __init__.py
│   │   │   └── pypass_cli.py
│   │   ├── gui
│   │   │   ├── desktop
│   │   │   │   ├── __init__.py
│   │   │   │   └── pypass_gui.py
│   │   │   ├── __init__.py
│   │   │   └── web
│   │   │       ├── content.py
│   │   │       ├── __init__.py
│   │   │       └── pypass_web.py
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── database
│   │   │   ├── connect.py
│   │   │   └── __init__.py
│   │   ├── passwords
│   │   │   ├── passwords.db
│   │   │   └── passwords.md
│   └── __init__.py
├── README.md
├── requirements.txt
└── setup.py
```

## Installation

1. Clone the repository and navigate to the project directory:

  ```bash
  git clone https://github.com/h471x/password_generator.git
  cd password_generator
  ```

2. Build the package:

  ```bash
  python setup.py sdist bdist_wheel
  ```

3. Install the package:

  ```bash
  pip install dist/pypass_tool-*.whl
  ```

## Usage

Once the package is installed, you can use the `pypass` command with different interfaces:

- **CLI Mode** (default):
  
  ```bash
  pypass
  ```

- **Desktop GUI Mode**:
  
  ```bash
  pypass gui
  ```

- **Web Interface Mode**:
  
  ```bash
  pypass web
  ```

  Open your browser and navigate to `http://127.0.0.1:5000`.

## Development

To modify or extend the functionality, ensure you have the required dependencies installed. You can add new features to the CLI, desktop, or web interface as per the structure.

### Dependencies

The required dependencies for the project are listed in `setup.py`:

- **Flask** (for the web interface)
- **Tkinter** (for the desktop GUI; included with Python)

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Contributing

Feel free to fork this repository, open issues, or submit pull requests with improvements or bug fixes.