# Importings Modules
from time import sleep
import curses
import os
from Files import print_center
from Programs import InfoRun

# Main Area
def main(stdscr):
    # Making the curser not show.
    curses.curs_set(0)
    # Making the Text and background colour.
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)

    # Printing "Starting The Programs."
    stdscr.attron(curses.color_pair(1))
    print_center("Installing The Programs")
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()
    sleep(2)

    # Clearing the screen.
    stdscr.erase()

    # Running the InfoRun
    InfoRun(stdscr)

    # Printing "Programs Started." 
    stdscr.attron(curses.color_pair(1))
    print_center("Programs Installed")
    stdscr.attron(curses.color_pair(1))
    stdscr.refresh()
    sleep(2)

# Runs the main funcation.
curses.wrapper(main)