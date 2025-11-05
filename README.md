# Steam Games Parser

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple and efficient parser for retrieving game information from the Steam store.

## Description

This project provides a convenient tool for fetching up-to-date game data from the Steam platform. Currently, it allows you to quickly obtain information such as:
- Current price and discount availability
- Game ID
- Publishers and developers
- Other useful information

It is ideal for market analysis, discount tracking, and personal use.

## Functionality (CLI)

The current command-line interface (CLI) version supports:
*   Searching for games by title
*   Selecting the region and currency for price display
*   Outputting core data in a user-friendly format
*   Repeated searches without restarting the program

## GUI Version (In Development) 🚧

**Actively working on a graphical user interface version based on PyQt6.**

Planned improvements:
*   **Extended functionality** compared to the CLI version
*   **User-friendly visual interface** for comfortable interaction
*   **Improved error handling** and intuitive controls
*   **Graphical data representation**

## Installation & Launch

1.  Clone the repository:
    ```bash
    git clone https://github.com/Dargram/steam_parser
    cd steam_parser
    ```

2.  Install dependencies (for the CLI version):
    ```bash
    pip3 install requests rich
    ```

3.  Run the CLI version:
    ```bash
    python CLI_parser.py
    ```

## Usage

1.  **Enter the game title** - in any language.
2.  **Select a country** to display the price in the corresponding currency (ua, de, us).
    
    ⚠️ **Note:** Some games might be unavailable in certain regions (e.g., "Postal 2" is banned in Germany).
3.  **Get the data** - information is displayed in a convenient format.
4.  **Continue searching** or type `exit` to quit.

## Technologies

- Python 3
- Requests (for HTTP requests)
- Rich (for enhanced console display)
- PyQt6 (for the upcoming GUI version)

## License

This project is licensed under the MIT License. For more details, see the `LICENSE` file.

---

**Note:** This project is not affiliated with Valve Corporation and uses publicly available data.
