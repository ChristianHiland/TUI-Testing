# Importing The Modules
from time import sleep
import curses
import json
from os import system, mkdir, path
from Scripts import print_center, MakeDir, MakeDirectory
from Scripts import JSONRun, KoreanRun, LearningWebRun

def Install(stdscr):
    with open("Program.json", "r") as ProgramsInstall:
        Data = json.load(ProgramsInstall)
        # Program Paths
        JSONPath = Data['Paths']['JSON']
        PyKoreanPath = Data['Paths']['PyKorean']
        LearningWebPath = Data['Paths']['LearningWeb']
        AllIN = Data['Programs']['All'].lower()
        JSONIN = Data['Programs']['JSON'].lower()
        PyKoreanIN = Data['Programs']['JSON'].lower()
        LearningWebIN = Data['Programs']['JSON'].lower()
        
        # Making the curser not show.
        curses.curs_set(0)
        # Making the Text and background colour.
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)

        # Check if the paths exist, if they don't then exit the program.
        if path.exists(JSONPath) == False:
            # Failed JSON
            stdscr.attron(curses.color_pair(3))
            print_center("Oops The JSON path that you entered does not exist.")
            stdscr.attroff(curses.color_pair(3))
            stdscr.erase()
            sleep(2)
            stdscr.refresh()
            MakeDirectory(MakeDir(JSONPath))

            stdscr.attron(curses.color_pair(2))
            print_center("The path was made.")
            stdscr.attroff(curses.color_pair(2))
            stdscr.erase()
            sleep(2)
            stdscr.refresh()
        if path.exists(PyKoreanPath) == False:
            # Failed PyKorean
            stdscr.attron(curses.color_pair(3))
            print_center("Oops The PyKorean path that you entered does not exist.")
            stdscr.attroff(curses.color_pair(3))
            stdscr.erase()
            sleep(2)
            stdscr.refresh()
            MakeDirectory(MakeDir(PyKoreanPath))

            # Printing saying that the folder was made
            stdscr.attron(curses.color_pair(2))
            print_center("The path was made.")
            stdscr.attroff(curses.color_pair(2))
            stdscr.erase()
            sleep(2)
            stdscr.refresh()
        if path.exists(LearningWebPath) == False:
            # Failed PyKorean
            stdscr.attron(curses.color_pair(3))
            print_center("Oops The Learning Web path that you entered does not exist.")
            stdscr.attroff(curses.color_pair(3))
            stdscr.erase()
            sleep(2)
            stdscr.refresh()
            MakeDirectory(MakeDir(LearningWebPath))

            # Printing saying that the folder was made
            stdscr.attron(curses.color_pair(2))
            print_center("The path was made.")
            stdscr.attroff(curses.color_pair(2))
            stdscr.erase()
            sleep(2)
            stdscr.refresh()
        

        # Making the folder, and printing the current progress.
        stdscr.attron(curses.color_pair(1))
        print_center("Running 'FolderMake.sh'")
        stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        system("./FolderMake.sh")
        sleep(1)
        stdscr.erase()
        stdscr.refresh()

        # Printing "Installing Programs"
        stdscr.attron(curses.color_pair(1))
        print_center("Checking the programs to install.")
        stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        sleep(2)

        # Checking the JSON.
        if Data['Programs']['All'].lower() != str("y"):
            if Data['Programs']['JSON'].lower() == str("y"):
                # Code for JSON
                JSONRun(stdscr, JSONPath)
            elif Data['Programs']['PyKorean'].lower() == str("y"):
                # Code for PyKorean
                KoreanRun(stdscr, PyKoreanPath)
            elif Data['Programs']['LearningWeb'].lower() == str("y"):
                # Code for HTML Quiz
                LearningWebRun(stdscr, LearningWebPath)
            else:
                # Code for other entries
                print("Oops you didn't put anything!")
                quit()

        elif Data['Programs']['All'].lower() == str("y"):
            JSONRun(stdscr, JSONPath)
            KoreanRun(stdscr, PyKoreanPath)
            LearningWebRun(stdscr, LearningWebPath)

        # Printing end.
        stdscr.attron(curses.color_pair(2))
        print_center("Unzipping Files")
        stdscr.attroff(curses.color_pair(2))
        stdscr.refresh()
        # Unzipping the files.
        UnzipCMD = str("./Unzip.sh" +" "+ JSONPath +" "+ PyKoreanPath +" "+ LearningWebPath +" "+ AllIN +" "+ JSONIN +" "+ PyKoreanIN +" "+ LearningWebIN)
        system(UnzipCMD)
        # Clearing the screen and refreshing.
        stdscr.erase()
        stdscr.refresh()
        sleep(2)
        # Clearing the screen.
        stdscr.erase()
    return
