# GUI-Port-Scanner

A graphical user interface (GUI) application for scanning ports on a target IP or URL.

## Description

The GUI Port Scanner is a Python program that allows users to scan ports within a specified range on a given target IP or URL. The program provides a user-friendly interface where users can enter the target and ports range, and it displays the open ports.

## Dependencies

This program requires the following dependencies:

- Python 3.x
- tkinter module
- socket module

## Installation

To install the necessary dependencies, run the following command:

pip install -r requirements.txt

## Usage

1. Run the program by executing the `gui_port_scanner.py` file.
2. Enter the target IP or URL in the provided input field.
3. Enter the ports range in the format `start_port-end_port`. For example, `1-100` indicates ports from 1 to 100.
4. Click the "Scan" button to initiate the port scanning process.
5. The program will display the open ports in the output text area.

## Example

In this example, the user entered the target as `example.com` and the ports range as `1-100`. The program identified the open ports and displayed the results in the output text area.

Port 22 is open.
Port 80 is open.
Port 443 is open.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
