from helper import onderstreep

uitvoer = onderstreep("AANBIEDING")
uitvoer.append("Aardbeienijs, emmertje van 5 liter: 5 euro")
uitvoer.append("Slagroom, spuitbus van 1 liter: 2 euro")

print()

for element in uitvoer:
    print(element)

'''
Uitvoer:
AANBIEDING
==========
Aardbeienijs, emmertje van 5 liter: 5 euro
Slagroom, spuitbus van 1 liter: 2 euro
'''