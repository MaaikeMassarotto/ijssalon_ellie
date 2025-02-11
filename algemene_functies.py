def mijn_functie1(a):
    return a * a
# print(mijn_functie1(5)) # 25

def mijn_functie2(a, b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a + b)
    uitvoer_lijst.append(a - b)
    uitvoer_lijst.append(a * b)
    uitvoer_lijst.append(a / b)
    return uitvoer_lijst
# print(mijn_functie2(5, 2)) # [7, 3, 10, 2.5] 