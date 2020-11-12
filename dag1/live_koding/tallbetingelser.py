# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:45:24 2020

@author: Marie
"""

tall = float(input("Gi meg et tall:"))

if tall > 0:
    print("Tallet er positivt")
elif tall < 0:
    print("Tallet er negativt")
else:
    print("Tallet er null!")
    
if tall == 3:
    print("Tallet er tre!")