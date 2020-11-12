# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 19:28:47 2020

@author: Marie
"""

# Vi "tenker" på et tall mellom 0 og 100
# Spilleren gjetter et tall
# Dersom gjettet er rett så er spillet over
# Dersom gjettet er for lavt eller høyt, får spilleren beskjed
# Spilleren får gjette på nytt
# Spilleren har begrenset med gjett
from random import randint

riktig_tall = randint(0, 100)
maks_forsøk = 3

gjett = int(input("Gjett et tall mellom 0 og 100: "))
forsøk = 1
while gjett != riktig_tall and forsøk < maks_forsøk:
    if gjett < riktig_tall:
        print("For lavt!")
    else:
        print("For høyt!")
    gjett = int(input("Gjett igjen: "))
    forsøk += 1
    
if riktig_tall == gjett:
    print("Det var riktig! :D")
else:
    print(f"Du har brukt opp dine {maks_forsøk} forsøk!")
    print("GAME OVER!!")




