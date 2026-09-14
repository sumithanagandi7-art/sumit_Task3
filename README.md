# Advanced Secure Password Generator

A desktop graphical user interface (GUI) application built with Python and Tkinter to help you generate highly secure and customizable passwords.

## Features

- **Customizable Length**: Choose a password length anywhere from 8 to 128 characters.
- **Character Selection**: Toggle the inclusion of uppercase letters, lowercase letters, numbers, and symbols.
- **Ambiguous Character Filter**: Option to exclude easily confused characters (like `0`, `O`, `1`, `l`, and `I`).
- **Strength Indicator**: Get real-time feedback on your generated password's strength (Weak, Medium, Strong).
- **Clipboard Integration**: Automatically copies the generated password to your clipboard, along with a manual "Copy to Clipboard" button.
- **Generation History**: Keeps track of the last 5 passwords you've generated during your session.

## Prerequisites

- Python 3.x installed on your machine.

## Installation and Setup

1. **Clone or Download the Repository**
   Ensure you have the project files (specifically `password_generator.py` and `requirements.txt`).

2. **Install Dependencies**
   The application requires the `pyperclip` library for clipboard operations. Install it via pip:
   ```bash
   pip install -r requirements.txt
   ```
   *(Alternatively, you can just run `pip install pyperclip`)*

## Usage

1. Run the Python script from your terminal or command prompt:
   ```bash
   python password_generator.py
   ```
2. The graphical interface will open.
3. Select your desired password length using the slider.
4. Check or uncheck the character types you want to include.
5. (Optional) Check the box to exclude ambiguous characters if you want to avoid confusing letters and numbers.
6. Click **Generate Password**. 
7. Your password will be displayed, its strength will be calculated, and it will be automatically copied to your clipboard!

## License

Feel free to use and modify this code for your personal or educational projects!
