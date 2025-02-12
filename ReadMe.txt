Random Password Generator

## Overview
The Random Password Generator is a Python-based tool that allows users to generate secure and random passwords based on their preferred length and character types. It includes options for uppercase letters, lowercase letters, numbers, and special characters. This tool is designed to help users create strong passwords for their accounts and systems.

## Features
- Generate random passwords with custom length.
- Include uppercase letters, lowercase letters, numbers, and special characters based on user preferences.
- Password is copied to the clipboard after generation for easy use.
- User-friendly command-line interface (CLI).
- The welcome screen is shown only once on the first run.
- Option to generate multiple passwords in a single session.

## Requirements
- Python 3.6 or higher
- **pyperclip** library for clipboard functionality (Install using `pip install pyperclip`)

## Installation
1. **Clone the repository** (if using a version control system like Git):
    ```bash git clone https://github.com/bbarish19/Random-Password-Generator.git```

2. **Download the files** directly to your system.

3. **Install Python** (if you don't already have it installed):
    - [Download Python](https://www.python.org/downloads/)

4. **Install required dependencies**:
    Open a terminal and run:
    ```bash pip install pyperclip```

## Usage
1. Open the folder where the `RandPassGen.py` file is located.
2. Run the script via the command line:
    ```bash
    python RandPassGen.py
    ```
3. The tool will display a welcome screen with an ASCII art logo and program description (this is shown only once during the first run).
4. The program will prompt you for the desired password length and whether to include uppercase letters, lowercase letters, numbers, and special characters.
5. A random password will be generated based on your inputs, and it will be copied to your clipboard.
6. You will be asked if you want to generate another password. Enter `y` to generate a new password or `n` to exit the program.
