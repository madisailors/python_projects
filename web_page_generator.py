import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        #default html button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10), pady=(10,10))

        #input button
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customHTML)
        self.btn.grid(padx=(10,10), pady=(10,10))

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    
    #defining function for text entry
    def customHTML(self):
        L1 = Label(top, text="Enter custom text or click default HTML page button")
        L1.grid(row=0, column=0, zpadx=(10,1), pady=(10,1))
        entry = Entry(top, width=75)
        entry.grid(row=1, column=1, padx=(10,10), pady=(10,10))

    #defining function to return data entry
    def get_data(self):
        L1.config(text = entry.get())


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
