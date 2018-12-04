#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 09:57:50 2018

@author: lov35174
"""
#from os.path import basename, splitext
import tkinter as tk
# from tkinter import ttk
from tkinter import Canvas, Scale, HORIZONTAL, Entry


class Application(tk.Tk):
    name = 'Míchání barev'

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        
        self.bind("<Escape>", self.quit)
        
        self.lbl = tk.Label(self, text="Hello World")
        self.lbl.pack()
        
        self.rScale = Scale(from_=0, to =255, orient=HORIZONTAL, fg='red', length=200, label='Červená', command=self.change)
        self.rScale.pack()
        
        self.gScale = Scale(from_=0, to =255, orient=HORIZONTAL, fg='green', length=200, label='Zelená', command=self.change)
        self.gScale.pack()
        
        self.bScale = Scale(from_=0, to =255, orient=HORIZONTAL, fg='blue', length=200, label='Modrá', command=self.change)
        self.bScale.pack()
        
        self.canvas = Canvas(self, width=200, height=200, bg="#000000")
        self.canvas.pack()
        
        self.frame = tk.Frame(self)
        self.frame.pack()
        
        self.entry = Entry(self.frame,width=7)
        self.entry.pack(side=tk.LEFT)
        
        self.btnClipBoard = tk.Button(self.frame, text='Kopírovat', command=self.toClipBoard)
        self.btnClipBoard.pack(side=tk.LEFT)
                
        self.btn = tk.Button(self, text='Quit', command=self.quit)
        self.btn.pack()
    
    def change(self, event=None):
        r = self.rScale.get()
        g = self.gScale.get()
        b = self.bScale.get()
        color = '#{:02x}{:02x}{:02x}'.format(r,g,b)
        print(color)
        self.entry.delete(0,tk.END)
        self.entry.insert(0,color)
        self.canvas.config(bg=color)
    
    def toClipBoard(self, event=None):
        clip = self.entry.get()
        self.clipboard_clear()
        self.clipboard_append(clip)
        self.update()
    
    def quit(self, event=None):
        super().quit()


app = Application()
app.lbl.config(text="Míchání barev")
app.mainloop()