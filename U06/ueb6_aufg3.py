class Flugzeug:
    def __init__(self, firma="Lufthansa", breite=10):
        self._hersteller = firma 
        self.__spannweite = breite
    
    def getHersteller(self):
        return self._hersteller
    
    def setHersteller(self, firma):
        self._hersteller = hersteller
        
    def getSpannweite(self):
        return self.__spannweite
    
    def setSpannweite(self, neueSpannweite):
        self.__spannweite = neueSpannweite
    
    def starte(self):
        print("Ich heb' ab!")
        
    def lande(self):
        print("I'm back!")
    
class Segelflugzeug(Flugzeug):
    def __init__(self, gleitzahl=0.3, firma="Lufthansa", breite=10):
        self.__gleitzahl = gleitzahl
        self._hersteller = firma 
        self.__spannweite = breite
        
    def getGleitzahl(self):
        return self.__gleitzahl
    
    def setGLeitzahl(self, neueGleitzahl):
        self.__gleitzahl = neueGleitzahl
    
    def starte(self):
        print("Ich heb' ab - bin aber ein Segelflugzeug!")
        
    def lande(self):
        print("I'm back and i'm the Segelflugzeug!")
    
    
class Propellerflugzeug(Flugzeug):
    def __init__(self, gleitzahl=0.3):
        self.__anzahlRotoren = gleitzahl
        
    def getGleitzahl(self):
        return self.__gleitzahl
    
    def setGLeitzahl(self, neueGleitzahl):
        self.__gleitzahl = neueGleitzahl
    
    def starte(self):
        print("Ich heb' ab - bin aber ein Segelflugzeug!")
        
    def lande(self):
        print("I'm back and i'm the Segelflugzeug!")
        
erstesFlugzeug = Flugzeug()
print(erstesFlugzeug.getHersteller())

erstesSegelflugzeug = Segelflugzeug()
print(erstesSegelflugzeug.getHersteller())