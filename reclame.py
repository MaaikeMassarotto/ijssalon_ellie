from algemene_functies import mijn_functie2

def aanbieding1(smaak, prijs, korting):
    korting *= prijs # korting is nu het bedrag dat eraf gaat
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs - korting} euro."
    return uitvoer
# print(aanbieding1("aardbei", 4, 0.1)) # Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak aardbei, van 4 euro voor 3.6 euro.

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal += bedrag
        btw_bedrag = totaal * btw
        uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
    return uitvoer
# print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09)) # Het totaal van alle inkomsten van deze week is 1575 euro, waarover 141.75 euro btw betaald dient te worden.

def laag_en_hoog(mijn_lijst):
    uitvoer = []
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    uitvoer.append(laagste)
    uitvoer.append(hoogste)
    return uitvoer 
# print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))    # [90, 430]

def gemiddelde(mijn_lijst):
    totaal = 0
    aantal = len(mijn_lijst)
    for element in mijn_lijst:
        totaal += element
    gemiddelde = totaal / aantal
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde:.2f} euro."
# print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))   # De gemiddelde inkomsten deze week zijn 225.00 euro.

def meervoudig(invoer_lijst):
    tijdelijk = laag_en_hoog(invoer_lijst)
    uitvoer = [tijdelijk[0], tijdelijk[1]]
    return uitvoer
#print(meervoudig([10, 5, 3, 2, 1, 2, 9]))   # [1, 10]

def combinatie(invoer_lijst2):
    korte_lijst = laag_en_hoog(invoer_lijst2)
    uitvoer = mijn_functie2(korte_lijst[0], korte_lijst[1]) 
    return uitvoer
#print(combinatie([10, 5, 3, 2, 1, 2, 9]))    # [11, -9, 10, 0.1]