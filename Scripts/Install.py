# Importing The Modules
from time import sleep
import curses
import json
from os import system, mkdir
from Files import print_center
from Scripts import JSONRun, KoreanRun

def Install(stdscr):
    with open("Program.json", "r") as ProgramsInstall:
        Data = json.load(ProgramsInstall)

        # Making the curser not show.
        curses.curs_set(0)
        # Making the Text and background colour.
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

         # Making the folder, and printing the current progress.
        stdscr.attron(curses.color_pair(1))
        print_center("Running 'FolderMake.sh'")
        stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        system("./FolderMake.sh")
        sleep(2)
        stdscr.erase()
        stdscr.refresh()

        # Printing "Installing Programs"
        stdscr.attron(curses.color_pair(1))
        print_center("Checking the programs to install.")
        stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        sleep(2)

        # Checking the JSON.
        if Data['Programs']['All'].lower() == str("y"):
            JSONPath = Data['Paths']['JSON']
            PyKoreanPath = Data['Paths']['PyKorean']
            mkdir(JSONPath)
            mddir(PyKoreanPath)

            # Installing JSON Maker Info.
            JSONRun(stdscr, JSONPath)
            # Installing PyKorean.
            KoreanRun(stdscr, PyKoreanPath)
            # Printing end.
            stdscr.attron(curses.color_pair(2))
            print_center("Unzipping Files")
            stdscr.attroff(curses.color_pair(2))
            stdscr.refresh()
            # Unzipping the files.
            UnzipCMD = str("./Unzip.sh" + " " + JSONPath + " " + PyKoreanPath)
            system(UnzipCMD)
            # Clearing the screen and refreshing.
            stdscr.erase()
            stdscr.refresh()
            sleep(2)
        else:
            print("This was not runned!")
        # Clearing the screen.
        stdscr.erase()
    return
