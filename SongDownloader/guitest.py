#! /usr/bin/env python3
import tkinter as tk

class UI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def display_entry(self):
        print("Song Name: %s - %s"%(self.entry1.get(),self.entry2.get()))

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command = self.quit)
        self.quitButton.grid(row = 3)
        tk.Label(self, text = 'Language:').grid(row = 0,column = 0,sticky =
                                                'W')
        self.entry1 = tk.Entry()
        self.entry1.grid(row = 0, column = 0)
        tk.Label(self, text='Song Name:').grid(row = 1,column = 0,sticky = 'W')
        self.entry2 = tk.Entry()
        self.entry2.grid(row= 1, column = 1)
        tk.Label(self, text='Singer/Movie Name:').grid(row = 2, column = 0,
                                                       sticky = 'W')
        self.entry3 = tk.Entry()
        self.entry3.grid(row= 2, column = 1)
        self.displaybutton = tk.Button(self, text = 'show', command =
                                       self.display_entry)
        self.displaybutton.grid(row=3,column =1)

ap = UI()
ap.master.title('song downloader')
ap.mainloop()
