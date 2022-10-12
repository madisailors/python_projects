#Python ver: 3.10.8
#
#Author: Madi Sailors
#
#Purpose: phonebook demo. Demonstrating Tkinter, GUI module,
#         using Tkinter parent child relationships.
#
#Tested OS: This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk

#being sure to import other modules, so we have access to them
from tkinter import messagebox #right place?
import phonebook_gui
import phonebook_func

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self,master,**args,**kwargs):
        Frame.__init__(self,master,**args,**kwargs)

        #define master frame config
        self.master = master
        self.master.minsize(500,300) #(height,width)
        self.master.maxsize(500,300)
        #this CenterWindow method will center our app on user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title('Tkinter PhonebookDemo')
        self.master.configure(bg='lightgray')
        #this protocol method is a tkinter built-in method to catch
        #if the user clicks upper corner 'x' on windows OS
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        #load in the GUI widgets from a separate module,
        #keeping code organized
        phonebook_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

    
