from domains.Engine import Engine
import curses

screen = curses.initscr()
e = Engine(screen)
e.start_engine()
