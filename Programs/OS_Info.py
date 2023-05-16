import os
import platform
from time import sleep
import curses
from Files import print_center

def InfoRun(stdscr):
    # Starting
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.erase()
    stdscr.refresh()

    # Making the folder, and printing the current progress.
    stdscr.attron(curses.color_pair(1))
    print_center("Making Data Folder")
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()
    os.system("mkdir Data")
    sleep(1)
    stdscr.erase()
    stdscr.refresh()

    # Making the files, and putting the data in.
    stdscr.attron(curses.color_pair(1))
    print_center("Making Data Folder")
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()
    os.system("./DONTRUN.sh")
    sleep(1)
    stdscr.erase()
    stdscr.refresh()