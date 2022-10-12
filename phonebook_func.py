import os
from tkinter import *
import tkinter as tk
import sqlite3

import phonebook_main
import phonebook_gui

def center_window(self, w, h): #pass in tkinter frame(master) reference
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to center app to users screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo
