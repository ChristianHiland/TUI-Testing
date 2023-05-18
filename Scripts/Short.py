# Importing The Modules.
import time
import curses
import json
import os

def MakeDir(directory):
    external_path = os.path.abspath(directory)
    return external_path
def MakeDirectory(directory_name):
    home_directory = os.path.expanduser("~")
    directory_path = os.path.join(home_directory, directory_name)
    os.makedirs(directory_path, exist_ok=True)
    print(f"Directory '{directory_path}' created successfully.")

def print_center(message):
    screen = curses.initscr()
    num_rows, num_cols = screen.getmaxyx()
    # Calculate center row
    middle_row = int(num_rows / 2)
    # Calculate center column, and then adjust starting position based
    # on the length of the message
    half_length_of_message = int(len(message) / 2)
    middle_column = int(num_cols / 2)
    x_position = middle_column - half_length_of_message
    # Draw the text
    screen.addstr(middle_row, x_position, message)
    screen.refresh()
# Making the JOSN.
def SetupInstall():
    print("What programs do you want to install.\n")
    AllPro = input("Do you want to install all the Programs? [Y/N]: ")
    JSONIn = "y"
    PyKoreanIn = "y"
    LearningWebIn = "y"
    if AllPro.lower() == str("n"):
        JSONIn = input("Do you want to install JSON Maker? [Y/N]: ")
        PyKoreanIn = input("Do you want to install PyKorean? [Y/N]: ")
        LearningWebIn = input("Do you want to install Learning Web? [Y/N]: ")

    # Getting the Paths.
    print("\nI don't know what options you have chosed,\nso just leave the path of the programs blank if you didn't seclect it.\n")
    print("\nWhat is the path that you want to install the JSON App? (Don't add the ~/ type the full path.)")
    JSONPath = input("Path: ")
    print("\nWhat is the path that you want to install the PyKorean App? (Don't add the ~/ type the full path.)")
    PyKoreanPath = input("Path: ")
    print("\nWhat is the path that you want to install the Learning Web App? (Don't add the ~/ type the full path.)")
    LearningWebPath = input("Path: ")

    # The Data tree.
    Data = {
        "Programs": {
            "All": AllPro,
            "JSON": JSONIn,
            "PyKorean": PyKoreanIn,
            "LearningWeb": LearningWebIn
        },
        "Self": {
            "Runned": "Yes"
        },
        "Paths": {
            "JSON": JSONPath,
            "PyKorean": PyKoreanPath,
            "LearningWeb": LearningWebPath
        }
    }
    with open("Program.json", "w") as write_file:
        json.dump(Data, write_file, indent=4)