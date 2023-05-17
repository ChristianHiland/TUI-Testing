# Importing The Modules.
import platform
from time import sleep
import curses
from Files import print_center
from datetime import date, datetime
import urllib.request

# Vars

# For the Time and Date
now = datetime.now()
today = date.today()
DateToday = today.strftime("%B %d")
DateTime = now.strftime("%H:%M")
DateWhole = str("At " + DateTime + " on " + DateToday + "\n")
# Files Dirs
Install_File = "Installed/JSON.zip"
Log = "Data/InstallLog.txt"
# Program File.
JSONProgram = "https://github.com/ChristianHiland/Form-Testing/archive/refs/tags/v0.01.0.zip"

def JSONRun(stdscr):
    # Starting
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
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
    print_center("Adding Files to the 'Data' folder")
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()
    os.system("./DONTRUN.sh")
    with open(Log, "a") as Loging:
        Loging.write(DateWhole)
        Loging.write("'Data' folder was made.\n")
        Loging.write(DateWhole)
        Loging.write("'InstallLog.txt' file was made.\n")
    sleep(1)
    stdscr.erase()
    stdscr.refresh()
    
    # Downloading The Program.
    stdscr.attron(curses.color_pair(2))
    print_center("Downloading 'JSON.zip'")
    stdscr.attroff(curses.color_pair(2))
    stdscr.refresh()
    filename, headers = urllib.request.urlretrieve(JSONProgram, filename=Install_File)
    with open(Log, "a") as Loging:
        Loging.write(DateWhole)
        Loging.write("'JSON.zip' was downloaded.\n")
    sleep(1)
    stdscr.erase()
    stdscr.refresh()