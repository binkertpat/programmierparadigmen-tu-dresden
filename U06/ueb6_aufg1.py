class Zaehler:
    aktueller_stand = 0
    
    def ausgabe(self):
        print(self.aktueller_stand)
        
    def increment(self):
        self.aktueller_stand = self.aktueller_stand + 1

    def decrement(self):
        self.aktueller_stand = self.aktueller_stand - 1
        
a = Zaehler()
b = Zaehler()
c = Zaehler()

a.increment()
a.increment()
a.increment()
a.increment()
a.increment()
a.increment()
a.increment()
a.ausgabe()

b.increment()
b.decrement()
b.ausgabe()

c.increment()
c.decrement()
c.decrement()
c.ausgabe()