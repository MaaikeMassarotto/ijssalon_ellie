import csv
from helper import *
from presentatie import *


inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}

totale_inkomsten = som(inkomsten.values())

# Voorbeeld: 
# print(totale_inkomsten)
'''
Uitvoer: 
5250
'''

presenteer(inkomsten, totale_inkomsten)
'''
Uitvoer:
Aardbeien-ijs-totaal : 1000 euro.
Vanille-ijs-totaal : 2000 euro.
Chocolade-ijs-totaal : 1500 euro.
Waterijsjes-totaal : 750 euro.
========================
Totaal : 5250 euro.
'''

with open('boekhouding.csv', 'w', newline='') as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value]) 