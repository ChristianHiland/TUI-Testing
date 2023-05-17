# Importing The Modules
from time import sleep
import curses
import json
from os import system
from Files import print_center
from Scripts import JSONRun, PyKorean

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
        sleep(1)

        # Checking the JSON.
        if Data['Programs']['All'].lower() == str("y"):
            # Installing JSON Maker Info.
            JSONRun(stdscr)
            # Installing PyKorean.
            JSONRun(stdscr)
            PyKorean(stdscr)
            # Unzipping the files.
            UnzipFile = str("./Unzip.sh" + " " + Data['Programs']['All'])
            system(UnzipFile)
        else:
            print("This was not runned!")
        # Clearing the screen.
        stdscr.erase()
