# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:53:26 2017

@author: Vašek
"""

heslo = input('zadej své heslo > ')

MALA = 'qwertzuiopasdfghjklyxcvbnm'
VELKA = MALA.upper()
SPEC = '!@#$%^&*{}()-.,_§ůú=%\\|€¶ŧ←↓→øþ~đ+-" \'`; '
CISLA = '0134456789'

if len(heslo) < 8:
     print('heslo je příliš krátké')
     exit(1)

jeMALA = False
jeVELKA = False
jeSPEC = False
jeCISLA = False

for znak in heslo:
    if znak in MALA:
        jeMALA = True
    if znak in VELKA:
        jeVELKA = True
    if znak in SPEC:
        jeSPEC = True
    if znak in CISLA:
        jeCISLA = True
        

if jeMALA + jeVELKA + jeSPEC + jeCISLA >=3:
    print('heslo je v pořádku')
    exit(0)
else:
    print('heslo je jednoduché')
    exit(3)