def bruchdivision():
   bruch1 = {}
   bruch2 = {}
   bruch3 = {}
   bruch1["zaehler"] = int(input("Zaehler1: "))
   bruch1["nenner"] = int(input("Nenner1: "))
   bruch2["zaehler"] = int(input("Zaehler2: "))
   bruch2["nenner"] = int(input("Nenner2: "))
   bruch3["zaehler"] = int(input("Zaehler3: "))
   bruch3["nenner"] = int(input("Nenner3: "))
   ausgabe(multiplikation(bruch3, kehrwert(multiplikation(bruch1, kehrwert(bruch2)))))
   pass
   
def kehrwert(bruch):
    #bruch["zaehler"], bruch["nenner"] = bruch["nenner"], bruch["zaehler"]
    #return bruch
    
    return {"zaehler":bruch["nenner"], "nenner":bruch["zaehler"]}

def multiplikation(bruch1, bruch2):
    return {"zaehler":bruch1["zaehler"] * bruch2["zaehler"], "nenner":bruch1["nenner"] * bruch2["nenner"]}
    

def ausgabe(ergebnis):
    print(str(ergebnis["zaehler"]) + " / " + str(ergebnis["nenner"]))
    print(ergebnis["zaehler"] / ergebnis["nenner"])

bruchdivision()

