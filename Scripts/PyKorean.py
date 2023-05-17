# Importing The Modules
from time import sleep
import curses
import urllib.request
from datetime import date, datetime
from Files import print_center

# For the Time and Date
now = datetime.now()
today = date.today()
DateToday = today.strftime("%B %d")
DateTime = now.strftime("%H:%M")
DateWhole = str("At " + DateTime + " on " + DateToday + "\n")
# File Dirs
Install_File = "Installed/PyKorean.zip"
Log = "Data/InstallLog.txt"
# Program File.
PyKoreanApp = "https://github.com/ChristianHiland/PyKorean/archive/refs/tags/v0.14.zip"

def KoreanRun(stdscr):
    # Making the curser not show.
    curses.curs_set(0)
    # Making the Text and background colour.
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    # Clearing the screen and refreshing.
    stdscr.erase()
    stdscr.refresh()
    
    # Printing "Installing Programs"
    stdscr.attron(curses.color_pair(1))
    print_center("Installing PyKorean")
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()
    with open(Log, "a") as Loging:
        Loging.write(DateWhole)
        Loging.write("Starting to install 'PyKorean.zip'.\n")
    sleep(1)
    
    # Clearing the screen and refreshing.
    stdscr.erase()
    
    # Printing the 'Downloading PyKorean' and downloading PyKorean.
    stdscr.attron(curses.color_pair(1))
    print_center("Downloading 'PyKorean.zip'")
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()
    filename, headers = urllib.request.urlretrieve(PyKoreanApp, filename=Install_File)
    with open(Log, "a") as Loging:
        Loging.write(DateWhole)
        Loging.write("'PyKorean.zip' was downloaded.\n")
    sleep(0.5)

    # Clearing the screen.
    stdscr.erase()

    # Printing end.
    stdscr.attron(curses.color_pair(2))
    print_center("Downloaded 'PyKorean.zip'")
    stdscr.attroff(curses.color_pair(2))
    stdscr.refresh()
    sleep(1)

    # Clearing the screen.
    stdscr.erase()
    return