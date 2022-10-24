import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime
import os.path
from os.path import join

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #setting title of GUI window
        self.master.title("File Transfer")

        #creating button to select files from source directory
        self.sourceDir_btn = Button(self.master, text="Select Source", width=20, command=self.sourceDir)
        #positioning source button in GUI using grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30, 0))

        #creating entry for source directory selection
        self.source_dir = Entry(width=75)
        #positioning entry in GUI using tkinter grid.
        #padx and pady are the same as the button to ensure they line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        #creating button to select destination of files from destination directory
        self.destDir_btn = Button(self.master, text="Select Destination", width=20, command=self.destDir)
        self.destDir_btn.grid(row=1, column=0, padx=(20, 10), pady=(15, 10))

        #creating entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #positioning in GUI
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #creating a button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        self.desDir_btn = Button(self.master, text="Select Destination", width=20, command=self.destDir)

        #creating button to transfer files
        self.transfer_btn= Button(self.master, text="Transfer Files", width=20, command=self.transferFiles)
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        #creating an exit button
        self.exit_btn = Button(self.master, text="Exit", width=20, command=self.exit_program)
        #positioning exit button
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))
        
    #creating function to select source directory
    def sourceDir(self):
        selectedSourceDir = tkinter.filedialog.askdirectory()
        #the .delete(0, end) will clear content inside entry widget
        #allowing the path to be inserted into the entry widget properly
        self.source_dir.delete(0, END)
        #the .insert method will insert user selection into source_dir entry
        self.source_dir.insert(0, selectedSourceDir)  
       

    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)

        
    def transferFiles(self):
        #gets source directory
        source = self.source_dir.get()
        #gets distination directory
        destination = self.destination_dir.get()
        #gets a list of files in the source directory
        source_files = os.listdir(source)

        #using current time
        init_time_now = datetime.now()
        datetime.timedelta(hours=24)
        absolute_path = ("C:\Users\madis\OneDrive\Documents\GitHub\python_projects\Customer Destination")
        relative_path = 
        print(os.path.join(absolute_path, relative_path)
        modified_time = os.path.getmtime(absolute_path)
        print(modified_time)
        
        #runs through each file in the source directory
        for i in source_files:
            #moves each file from the source to the destination
            shutil.move(source + '/' + i, destination)
            print(i + ' was successfully transferred.')
        

    def exit_program(self):
        #root is the main GUI window, the tkinter destroy method tells
        #python to terminate root.mainloop all widgets inside GUI window
        root.destroy()



        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

