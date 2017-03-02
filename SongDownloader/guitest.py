#! /usr/bin/env python3
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def display_entry(self):
        print("Song Name: %s"%(self.entry1.get()))

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command = self.quit)
        self.quitButton.grid(row = 1)
        tk.Label(self, text='Song Name:').grid(row = 0,column = 0)
        self.entry1 = tk.Entry()
        self.entry1.grid(row= 0, column = 1, sticky = 'N')
        self.displaybutton = tk.Button(self, text = 'show', command =
                                       self.display_entry)
        self.displaybutton.grid(row=1,column =1)

ap = App()
ap.master.title('song downloader')
ap.mainloop()
