# Importing The Modules.
import time
import curses
import json

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
    OSINFO = input("Do you want to install JSON Maker? [Y/N]: ")
    Data = {
        "Programs": {
            "All": AllPro,
            "JSON": OSINFO
        },
        "Self": {
            "Runned": "Yes"
        }
    }
    with open("Program.json", "w") as write_file:
        json.dump(Data, write_file, indent=4)