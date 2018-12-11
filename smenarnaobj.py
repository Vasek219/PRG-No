#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:21:49 2018

@author: lov35174
"""


import tkinter as tk
from tkinter import Label, LabelFrame, Radiobutton, IntVar, Entry


class Application(tk.Tk):
    name = 'Směnárna'

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        
        ######Štítek
        self.stitek=Label(self, text=u'Směnárna')
        self.stitek.pack()
        
        
        #####ESC
        self.bind("<Escape>", self.quit)
        
        
        ######Transakce
        self.trans = LabelFrame(self, text='Transakce')
        self.trans.pack(anchor='w')
        
        v = IntVar()
        v.set(0)
        
        self.nakup = Radiobutton(self.trans, text="Nákup", variable=v, value=1)
        self.prodej = Radiobutton(self.trans, text="Prodej", variable=v, value=2)
        self.nakup.pack(anchor='w')
        self.prodej.pack(anchor='w')
        
               
        ######Měna
        self.mena = LabelFrame(self, text='Měna')
        self.mena.pack(anchor='w')
        
        c = IntVar()
        c.set(0)
        
        self.eur = Radiobutton(self.mena, text="EUR", variable=c, value=1) 
        self.gbp = Radiobutton(self.mena, text="GBP", variable=c, value=2)
        self.usd = Radiobutton(self.mena, text="USD", variable=c, value=3) 
        self.jpy = Radiobutton(self.mena, text="JPY", variable=c, value=4)
        self.idr = Radiobutton(self.mena, text="IDR", variable=c, value=5)
        self.eur.pack(anchor='w')
        self.gbp.pack(anchor='w')
        self.usd.pack(anchor='w')
        self.jpy.pack(anchor='w')
        self.idr.pack(anchor='w')
        
        
        ######Kurz
        self.kurzok = LabelFrame(self, text='Kurz')
        self.kurzok.pack(anchor='w')
        
        mnozstvi = tk.StringVar()
        mnozstvi.set('')
        kurzvar = tk.StringVar()
        kurzvar.set('')
        
        self.lblmnoz = Label(self.kurzok, text=u'Množství:')
        self.lblmnoz.pack(anchor='w')
        
        self.mnoz = Entry(self.kurzok, state='readonly', textvariable=mnozstvi)
        self.mnoz.pack(anchor='e')
        
        self.lblkurz = Label(self.kurzok, text=u'Kurz:')
        self.lblkurz.pack(anchor='w')
        
        self.kurz = Entry(self.kurzok, state='readonly', textvariable=kurzvar)
        self.kurz.pack(anchor='w')
        
        
        
        ######Výpočet
        self.vypocet = LabelFrame(self, text='Výpočet')
        self.vypocet.pack(anchor='w')
        
        self.vstup = Entry(self.vypocet)
        self.vstup.pack(anchor='w')
        
        self.btnvyp = tk.Button(self.vypocet, text='Výpočet', command=None)
        self.btnvyp.pack(anchor='e')
        
        vyst= tk.StringVar()
        vyst.set('')
        
        self.entryvyst = Entry(self.vypocet, state='readonly', textvariable=vyst)
        self.entryvyst.pack(anchor='w')
   
    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()