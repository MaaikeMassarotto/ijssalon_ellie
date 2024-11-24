def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()


def fooi_pp(bedrag, personen):
    try:
        bedrag_pp = bedrag / personen
    except:
        bedrag_pp = "??"
    return f"De fooi is {bedrag_pp} euro per persoon."
'''
# De code aanroepen:
b = int(input("Welk bedrag zit er in de fooienpot?"))
p = int(input("Over hoeveel mensen moet de pot verdeeld worden?"))

print(fooi_pp(b,p))
'''
'''
Uitvoer:
Welk bedrag zit er in de fooienpot? 34
Over hoeveel mensen moet de pot verdeeld worden? 3
De fooi is 11.333333333333334 euro per persoon.
'''


def onderstreep(tekst=""):
    lengte =len(tekst)
    uit =[]
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit


def som(inkomsten):
    totaal = 0
    for bedrag in inkomsten:
        totaal += bedrag
    som = totaal
    return som

# Voorbeeld
# print(som(inkomsten={350,25,94,180}))
'''
Uitvoer:
De totale inkomsten zijn: 649 euro.
'''
