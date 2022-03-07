class Flugzeug:
    def __init__(self, firma="Lufthansa", breite=10):
        self.__hersteller = firma 
        self.__spannweite = breite
    
    def getHersteller(self):
        return self.__hersteller
    
    def setHersteller(self, firma):
        self.__hersteller = hersteller
        
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
    def __init__(self, anzahlRotoren=4, firma="Lufthansa", breite=10):
        self.__anzahlRotoren = gleitzahl
        self._hersteller = firma 
        self.__spannweite = breite
        
    def getAnzahlRotoren(self):
        return self.__anzahlRotoren
    
    def setAnzahlRotoroen(self, neueAnzahlRotoren):
        self.__anzahlRotoren = neueAnzahlRotoren
    
    def starte(self):
        print("Ich heb' ab - bin aber ein Propellerflugzeug!")
        
    def lande(self):
        print("I'm back and i'm the Propellerflugzeug!")
        
class Jet(Flugzeug):
    def __init__(self, triebwerke = 4, firma = "Lufthansa", breite = 10):
        self.__anzahlTriebwerke = triebwerke
        self._hersteller = firma 
        self.__spannweite = breite
        
    def getAnzahlTriebwerke(self):
        return self.__anzahlTriebwerke
    
    def setAnzahlTriebwerke(self, neueAnzahlTriebwerke):
        self.__anzahlTriebwerke = neueAnzahlTriebwerke
    
    def starte(self):
        print("Ich heb' ab - bin aber ein Jet!")
        
    def lande(self):
        print("I'm back and i'm the Jet!")


class Kampfjet(Jet):
    def __init__(self, raketen = 100, triebwerke = 4, firma = "Lufthansa", breite = 10):
        self.__anzahlRaketen = raketen
        self.__anzahlTriebwerke = triebwerke
        self._hersteller = firma 
        self.__spannweite = breite
        
    def getAnzahlRaketen(self):
        return self.__anzahlRaketen
    
    def setAnzahlRaketen(self, neueAnzahlRaketen):
        self.__anzahlRaketen = neueAnzahlRaketen
    
    def starte(self):
        print("Ich heb' ab - bin aber ein Kampfjet!")
        
    def lande(self):
        print("I'm back and i'm the Kampfjet!")
        
    def loeseSchleuderSitzAus():
        print("I believe i can fly...")
        
class Passagierjet(Jet):
    def __init__(self, sitze = 250, triebwerke = 4, firma = "Lufthansa", breite = 10):
        self.__anzahlSitze = sitze
        self.__anzahlTriebwerke = triebwerke
        self._hersteller = firma 
        self.__spannweite = breite
        
    def getAnzahLSitze(self):
        return self.__anzahlRaketen
    
    def setAnzahlSitze(self, neueAnzahlSitze):
        self.__anzahlSitze = neueAnzahlSitze
    
    def erbitteLanderlaubnis(self, flughafencode):
        print("Sie dürfen am Flughafen " + flughafencode + "landen.")
        return True
        
    def lande(self, flughafencode):
        print("Ich lande am Flughafen " + flughafencode + ".")
        return True
    
class Concorde(Passagierjet):
    def __init__(self, serienNr):
        self.__seriennummer = serienNr
        
    def getSeriennummer(self):
        return self.__seriennummer
    
    def setSerienummer(self, neueSeriennummer):
        self.__seriennummer = neueSeriennummer
    
    def lande(self):
        print("I'm back and i'm the Concorde!")
    