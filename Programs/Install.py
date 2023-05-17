# Importing The Modules
from time import sleep
import curses
import json
from Files import print_center
from Programs import InfoRun

def Install(stdscr):
    with open("Program.json", "r") as ProgramsInstall:
        Data = json.load(ProgramsInstall)

        # Making the curser not show.
        curses.curs_set(0)
        # Making the Text and background colour.
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

        # Printing "Installing Programs"
        stdscr.attron(curses.color_pair(1))
        print_center("Checking the programs to install.")
        stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        # Checking the JSON.
        if Data['Programs']['All'].lower() == str("y"):
            InfoRun(stdscr)
        else:
            SetupInstall()
            curses.wrapper(main)

        sleep(1)
        # Clearing the screen.
        stdscr.erase()
