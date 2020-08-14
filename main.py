#!/usr/bin/env python3

import curses
import praw
import os

reddit = praw.Reddit("bot")

def main(win):
	win.nodelay(True)
	key=""
	win.clear()
	win.addstr("Detected key:")
	while 1:
		try:
			key = win.getkey()
			win.clear()
			win.addstr(str(key))
			if key == "q":
				win.clear()
				win.addstr("you dun fucked up")
		except Exception as e:
			# No input
			pass

curses.wrapper(main)