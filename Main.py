# Importings Modules
import time
import curses

# Main Area
def main(stdscr):
    # Making the curser not show.
    curses.curs_set(0)
    # Making the background and text colour.
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    

    # Getting the size of the screen.
    h, w = stdscr.getmaxyx()
    # The text to show
    text = "Hello, World!"

    # Getting it where the text will show in the middle.
    x = w//2 - len(text)//2
    y = h//2

    # Starts the colour pair as in shows the colour pair.   
    stdscr.attron(curses.color_pair(1))
    # Showing the text in the middle.
    stdscr.addstr(y, x, text)
    # Turns off the colour pair.
    stdscr.attron(curses.color_pair(1))
    # The screen needs to refresh to show the text.
    stdscr.refresh()
    # Waits 3sec before closing the window
    time.sleep(3)

# Runs the main funcation.
curses.wrapper(main)