from curses import wrapper
import curses


def main(stdscr):
    stdscr.clear()
    while True:
        c = stdscr.getch()
        if c == ord('p'):
            print('p')
        elif c == ord('q'):
            print('q')
            break  # Exit the while loop
        elif c == curses.KEY_HOME:
            x = y = 0
