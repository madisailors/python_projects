import tkinter as tk
from tkinter import *
import tkinter.filedialog

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #setting title of GUI window
        self.master.title("File Transfer")

        #creating button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20)
        #positioning source button in GUI using grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #creating entry for source directory selection
        self.source_dir = Entry(width=75)
        #positioning entry in GUI using tkinter grid.
        #padx and pady are the same as the button to ensure they line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #creating button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #creating entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #positioning in GUI
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))
        
    #creating function to select source directory
    def sourceDir(self):
        selectedSourceDir = tkinter.filedialog.askdirectory()
        #the .delete(0, end) will clear content inside entry widget
        #allowing the path to be inserted into the entry widget properly
        self.source_dir.delete(0, END)
        #the .insert method will insert user selection into source_dir entry
        self.source_dir.insert(0, selectSourceDir)

        #creating a button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)

    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)

        self.desDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

