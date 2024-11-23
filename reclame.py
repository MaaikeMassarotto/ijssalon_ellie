from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1-korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting:.2f} euro." # het :.2f gedeelte heb ik opgezocht op het internet, om er mooi 3.60 van te maken ipv 3.6
    return uitvoer
# Voorbeeld:
print(aanbieding_1("aardbei", 4, 0.1))


inkomsten_per_dag = [220, 430, 125, 160, 205 ,90 ,345]
btw = 0.09

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for nr in inkomsten:
        totaal += nr
    bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden"
    return uitvoer
# Voorbeeld:
print(inkomsten_totaal(inkomsten_per_dag, btw))


def laag_en_hoog(mijn_lijst):
    hoogste = max(mijn_lijst)
    laagste = min(mijn_lijst)    
    uitvoer = hoogste, laagste
    return uitvoer
# Voorbeeld:
print(laag_en_hoog(inkomsten_per_dag))


def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    aantal = len(mijn_lijst)  
    gemiddelde = totaal / aantal
    uitvoer = f"De gemiddelde inkomsten deze week zijn {gemiddelde:.2f} euro."
    return uitvoer
# Voorbeeld:
print(gemiddelde(inkomsten_per_dag))


def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
# Voorbeeld:
print(meervoudig(invoer_lijst=[10, 5, 3, 2, 1, 2, 9]))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
# Voorbeeld:
print(combinatie(invoer_lijst_2=[5, 9]))
