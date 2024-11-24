from helper import *

def presenteer(mijn_dict, totaal):
    for key, value in mijn_dict.items():
        print(f"{key} : {value} euro.")
    print("========================")
    print(f"Totaal : {totaal} euro.")

# Voorbeeld:
# presenteer(mijn_dict = {'vis' : 10, 'vlees' : 25, 'overig' : 15}, totaal=50)
'''
Uitvoer: 
vis : 10 euro.
vlees : 25 euro.
overig : 15 euro.
========================
Totaal : 50 euro.
'''