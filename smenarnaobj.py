#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:21:49 2018

@author: lov35174
"""


import tkinter as tk
from tkinter import Label, LabelFrame, Radiobutton, IntVar, Entry, StringVar


class Application(tk.Tk):
    name = 'Směnárna'

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.config(borderwidth = 5)
        ######Štítek
        self.stitek=Label(self, text=u'Směnárna')
        self.stitek.pack()
        
        
        #####ESC
        self.bind("<Escape>", self.quit)
        
        
        ######Transakce
        self.transFrame = LabelFrame(self, text='Transakce')
        self.transFrame.pack(anchor='w')
        
        self.transVar = StringVar()
        self.transVar.set('nakup')
        
        self.nakupRadb = Radiobutton(self.transFrame, text="Nákup", variable=self.transVar, value='nakup')
        self.prodejRadb = Radiobutton(self.transFrame, text="Prodej", variable=self.transVar, value='prodej')
        self.nakupRadb.pack(anchor='w')
        self.prodejRadb.pack(anchor='w')
        
        
        
        ######Měna
        
        self.nactilistek('listek.txt')
        
        self.menaFrame = LabelFrame(self, text='Měna')
        self.menaFrame.pack(anchor='w')
        
        self.menaVar = IntVar()
        self.menaVar.set(0)
        
        self.eurRadb = Radiobutton(self.menaFrame, text="EUR", variable=self.menaVar, value=0) 
        self.gbpRadb = Radiobutton(self.menaFrame, text="GBP", variable=self.menaVar, value=1)
        self.usdRadb = Radiobutton(self.menaFrame, text="USD", variable=self.menaVar, value=2) 
        self.jpyRadb = Radiobutton(self.menaFrame, text="JPY", variable=self.menaVar, value=3)
        self.idrRadb = Radiobutton(self.menaFrame, text="IDR", variable=self.menaVar, value=4)
        self.eurRadb.pack(anchor='w')
        self.gbpRadb.pack(anchor='w')
        self.usdRadb.pack(anchor='w')
        self.jpyRadb.pack(anchor='w')
        self.idrRadb.pack(anchor='w')
        
        
        ######Kurz
        self.kurzokFrame = LabelFrame(self, text='Kurz')
        self.kurzokFrame.pack(anchor='w')
        
        self.mnozVar = tk.StringVar()
        self.mnozVar.set('')
        self.kurzVar = tk.StringVar()
        self.kurzVar.set('')
        
        self.mnozLabel = Label(self.kurzokFrame, text=u'Množství:')
        self.mnozLabel.pack(anchor='w')
        
        self.mnozEntry = Entry(self.kurzokFrame, state='readonly', textvariable=self.mnozVar)
        self.mnozEntry.pack(anchor='e')
        
        self.kurzLabel = Label(self.kurzokFrame, text=u'Kurz:')
        self.kurzLabel.pack(anchor='w')
        
        self.kurzEntry = Entry(self.kurzokFrame, state='readonly', textvariable=self.kurzVar)
        self.kurzEntry.pack(anchor='w')
        
        
        
        ######Výpočet
        self.vypocetFrame = LabelFrame(self, text='Výpočet')
        self.vypocetFrame.pack(anchor='w')
        
        self.vstupEntry = Entry(self.vypocetFrame)
        self.vstupEntry.pack(anchor='w')
        
        self.vypButton = tk.Button(self.vypocetFrame, text='Výpočet', command=None)
        self.vypButton.pack(anchor='e')
        
        vyst= tk.StringVar()
        vyst.set('')
        
        self.vystEntry = Entry(self.vypocetFrame, state='readonly', textvariable=vyst)
        self.vystEntry.pack(anchor='w')
   
    def nactilistek(self, filename):
        self.listek = dict()
        with open(filename, 'r') as f:
            while True:
                radek = f.readline()
                if radek == '':
                    break
                radek = radek.replace(',', '.')
                mena, mnoz, nakup, prodej = radek.split()
                self.listek[mena] = dict()
                self.listek[mena]['mnoz'] = int(mnoz)
                self.listek[mena]['nakup'] = float(nakup)
                self.listek[mena]['prodej'] = float(prodej)
            print(self.listek)
    
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()