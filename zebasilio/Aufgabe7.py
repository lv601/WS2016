# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 19:43:22 2016

@author: jose
"""

menu = [("Vorspeisen", ""), ("Suppe", "Tagessuppe von vorvorgestern",2.3), ("Suppe deluxe", "Für die grosse Geldbörse", 1300.5)]
print(30 * "*" + " Menu " + 30 * "*" + "\nVorspeisen:\n")
print('{:<15}''{:<30}''{:<10} €'.format(menu[1][0],menu[1][1],menu[1][2]))
print('{:<15}''{:<30}''{:<10} €'.format(menu[2][0],menu[2][1],menu[2][2]))
print("\n" + 60 * "*" + "\n")



#****************************** Menu ******************************
#Vorspeisen:

#Suppe          Tagessuppe von vorvorgestern  2.3        €
#Suppe deluxe   Für die grosse Geldbörse      1300.5     €

#************************************************************



