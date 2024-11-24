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