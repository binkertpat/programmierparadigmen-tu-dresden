def bruchaddition():
    bruch1 = {}
    bruch2 = {}
    bruch1["zaehler"] = int(input("Zaehler1: "))
    bruch1["nenner"] = int(input("Nenner1: "))
    bruch2["zaehler"] = int(input("Zaehler2: "))
    bruch2["nenner"] = int(input("Nenner2: "))
    ausgabe(summe(hauptnenner(bruch1, bruch2), hauptnenner(bruch2, bruch1)))

def hauptnenner(bruch1, bruch2):
    return multiplikation(bruch1,{"zaehler": bruch2["nenner"],"nenner": bruch2["nenner"]})
    
def summe(bruch1, bruch2):
    return {"zaehler": bruch1["zaehler"] + bruch2["zaehler"], "nenner": bruch1["nenner"]}

def multiplikation(bruch1, bruch2):
    return {"zaehler": bruch1["zaehler"] * bruch2["zaehler"], "nenner": bruch1["nenner"] * bruch2["nenner"]}

def ausgabe(ergebnis):
    print(str(ergebnis["zaehler"]) + " / " + str(ergebnis["nenner"]))
    print(ergebnis["zaehler"] / ergebnis["nenner"])
    pass

bruchaddition()


