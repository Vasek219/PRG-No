#!/usr/bin/env python3
# Soubor:  smenarna.py
# Datum:   08.01.2019 10:09
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
####################################################
import tkinter as tk
from tkinter import LabelFrame, Radiobutton, Entry


class Application(tk.Tk):
    name = 'Směnárna'
    name = 'Foo'

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.config(borderwidth=10)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Směnárna")
        self.lbl.pack()

        self.transakceVar = tk.StringVar()
        self.transakceVar.trace('w', self.vypocet)

        self.transakceFrame = LabelFrame(self, text="Transakce",
                                         padx=5, pady=5)
        self.transakceFrame.pack(anchor=tk.W)
        self.menaFrame = LabelFrame(self, text="Měna", padx=5, pady=5)
        self.menaFrame.pack()
        self.kurzFrame = LabelFrame(self, text="Kurz", padx=5, pady=5)
        self.kurzFrame.pack()

        Radiobutton(self.transakceFrame, text="Nákup",
                    variable=self.transakceVar, value='nakup').pack()
        Radiobutton(self.transakceFrame, text="Prodej",
                    variable=self.transakceVar, value='prodej').pack()
        self.transakceVar.set('nakup')   # vyberu nákup

        self.nactilistek('listek.txt')

        self.mnozstviEdit = Entry(self.kurzFrame, state='readonly')
        self.mnozstviEdit.pack()

        self.btn = tk.Button(self, text='Konec', command=self.quit)
        self.btn.pack(anchor=tk.E)

    def nactilistek(self, filename):
        self.listek = dict()
        with open(filename, 'r') as f:
            while True:
                radek = f.readline()
                if radek == '':
                    break
                radek = radek.replace(',', '.')
                mena, mnozstvi, nakup, prodej = radek.split()
                self.listek[mena] = dict()
                self.listek[mena]['mnozstvi'] = int(mnozstvi)
                self.listek[mena]['nakup'] = float(nakup)
                self.listek[mena]['prodej'] = float(prodej)
            print(self.listek)

    def vypocet(self):
        pass

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()
