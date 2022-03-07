from random import randint

class Flugzeug:
    def __init__(self, firma="Lufthansa", breite=10):
        __hersteller = firma 
        __spannweite = breite
    
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
    def __init__(self, gleitzahl = 0.3, firma="Lufthansa", breite=10):
        self.__gleitzahl = gleitzahl
        self._hersteller = firma 
        self.__spannweite = breite
        
    def getGleitzahl(self):
        return self.__gleitzahl
    
    def setGleitzahl(self, neueGleitzahl):
        self.__gleitzahl = neueGleitzahl
    
    def starte(self):
        print("Ich heb' ab - bin aber ein Segelflugzeug!")
        
    def lande(self):
        print("I'm back and i'm the Segelflugzeug!")
    
    
class Propellerflugzeug(Flugzeug):
    def __init__(self, anzahlRotoren = 4, firma = "Lufthansa", breite = 10):
        self.__anzahlRotoren = anzahlRotoren
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
        
    def getAnzahlSitze(self):
        return self.__anzahlSitze
    
    def setAnzahlSitze(self, neueAnzahlSitze):
        self.__anzahlSitze = neueAnzahlSitze
    
    def erbitteLanderlaubnis(self, flughafencode):
        print("Sie dürfen am Flughafen " + flughafencode + "landen.")
        return True
        
    def lande(self, flughafencode):
        print("Ich lande am Flughafen " + flughafencode + ".")
        return True
    
class Concorde(Passagierjet):
    def __init__(self, serienNr = 123456):
        self.__seriennummer = serienNr
        
    def getSeriennummer(self):
        return self.__seriennummer
    
    def setSerienummer(self, neueSeriennummer):
        self.__seriennummer = neueSeriennummer
    
    def lande(self):
        print("I'm back and i'm the Concorde!")
    
class Fluggesellschaft():
    def __init__(self, name = "Lufthansa", rufzeichen = "Erstmal ein Gut-Flug in die Runde"):
        self.__name = name
        self.__rufzeichen = rufzeichen
        self.__flugzeuge = []
        
    def getName(self):
        return self.__name

    def teste(self, anzahl = 10, maxAnzahl = 30):
        optionsFlugzeuge = [Concorde(), Passagierjet(), Kampfjet(), Jet(), Propellerflugzeug(), Segelflugzeug()]
        
        for i in range(randint(anzahl, maxAnzahl)):
            self.__flugzeuge.append(optionsFlugzeuge[randint(0,5)])
        
        print("Fluggesellschaft " + self.__name + ":")
        for i in range(len(self.__flugzeuge)):
            print("   " + str(i) + ": " + type(self.__flugzeuge[i]).__name__)
        
    def wartung(self):
        wartungsDaten = {"Sitze der Passierjets": 0, "Anzahl der Raketen": 0, "Anzahl der Rotoren": 0}
        for i in range(len(self.__flugzeuge)):
            if(isinstance(self.__flugzeuge[i], Kampfjet)):
                wartungsDaten["Anzahl der Raketen"] += self.__flugzeuge[i].getAnzahlRaketen()
            elif(isinstance(self.__flugzeuge[i], Propellerflugzeug)):
                wartungsDaten["Anzahl der Rotoren"] += self.__flugzeuge[i].getAnzahlRotoren()
            elif((isinstance(self.__flugzeuge[i], Passagierjet)) and (not isinstance(self.__flugzeuge[i], Concorde))):
                wartungsDaten["Sitze der Passierjets"] += self.__flugzeuge[i].getAnzahlSitze()
                
        print("\nWartungsdaten:")
        print("   Anzahl der Raketen:     " + str(wartungsDaten["Anzahl der Raketen"]))
        print("   Anzahl der Rotoren:     " + str(wartungsDaten["Anzahl der Rotoren"]))
        print("   Sitze der Passierjets:  " + str(wartungsDaten["Sitze der Passierjets"]))
        print("\n")
         
EasyJet = Fluggesellschaft("EasyJet")
print(">> " + EasyJet.getName() + "\n")
EasyJet.teste()
EasyJet.wartung()

Ryanair = Fluggesellschaft("RyanAir")
print(">> " + Ryanair.getName() + "\n")
Ryanair.teste()
Ryanair.wartung()
                
