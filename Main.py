# Importings Modules
from time import sleep
import curses
import os
import json
from Scripts import print_center
from Scripts import Install
from Scripts import SetupInstall

# Main Area
def main(stdscr):
    # Making the curser not show.
    curses.curs_set(0)
    # Making the Text and background colour.
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Printing "Starting The Programs."
    stdscr.attron(curses.color_pair(1))
    print_center("Installing The Programs")
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()
    sleep(1)

    # Clearing the screen.
    stdscr.erase()

    # Running the Install file.
    Install(stdscr)

    # Printing "Programs Started." 
    stdscr.attron(curses.color_pair(2))
    print_center("Programs Installed")
    stdscr.attron(curses.color_pair(2))
    stdscr.refresh()
    sleep(2)

# Checks if the user had ran the program before
with open("Program.json", "r") as checkRun:
    Data = json.load(checkRun)
    if Data['Self']['Runned'].lower() == str("yes"):
        curses.wrapper(main)
    else:
        SetupInstall()
        curses.wrapper(main)
