def decoreer(tekst = ""):
    lengte = len(tekst) + 4
    print() # empty line
    print(lengte * "*") # print 4 stars
    print(f"* {tekst} *") # print tekst in the middle
    print(lengte * "*") # print 4 stars
    print() # empty line