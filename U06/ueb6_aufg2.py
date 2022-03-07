class Zaehler:
    aktueller_stand = 0
    
    def ausgabe(self):
        print(self.aktueller_stand)
        
    def increment(self):
        self.aktueller_stand = self.aktueller_stand + 1

    def decrement(self):
        self.aktueller_stand = self.aktueller_stand - 1
        
class SchnellerZaehler(Zaehler):
    def increment(self):
        self.aktueller_stand = self.aktueller_stand + 5
        
class ResetZaehler(SchnellerZaehler):
    def reset(self):
        self.aktueller_stand = 0
        
z1 = Zaehler()
z2 = Zaehler()
z3 = Zaehler()
z4 = Zaehler()
z5 = Zaehler()

zaehlerObjects = [z1, z2, z3, z4, z5]
sumOfAllObjects = 0
    
for i in range(5):
    zaehlerObjects[i].increment()
    sumOfAllObjects += zaehlerObjects[i].aktueller_stand
#Erwartung: 1 + 1 + 1 + 1 + 1 = 5
print('errechnete Summe:')
print(sumOfAllObjects)

z6 = Zaehler()
z7 = SchnellerZaehler()
z8 = ResetZaehler()
zaehlerObjectsInheritance = [z6, z7, z8]
sumOfAllObjectsInheritance = 0

for i in range(2):
    for j in range(3):
        zaehlerObjectsInheritance[j].increment()
        if (i==1):
            sumOfAllObjectsInheritance += zaehlerObjectsInheritance[j].aktueller_stand
# Erwartung: (1+1) + (5+5) + (5+5) = 22
print('\nerrechnete Summe (Vorteil Vererbung):')
print(sumOfAllObjectsInheritance)
    