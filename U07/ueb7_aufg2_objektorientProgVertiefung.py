class Fahrzeug():
    def __init__(self, kennzeichen = "XX-YY 123", anzSitzplaetze = 5, grundpreis = 0, preisProKM = 0):
        self.__kennzeichen = kennzeichen
        self.__anzSitzplaetze = anzSitzplaetze
        self.__grundpreis = grundpreis
        self.__preisProKM = preisProKM
        self.__kilometerstand = 0.0
        self.__tagesfahrstrecke = 0.0
        self.__tageseinnahmen = 0.0
        
    def berechneFahrpreis(self, strecke):
        self.__kilometerstand += strecke
        self.__tagesfahrstrecke += strecke
        self.__tageseinnahmen += (strecke * self.__preisProKM) + self.__grundpreis
        
        return "     Fahrpreis: " + str((strecke * self.__preisProKM) + self.__grundpreis)
    
    def getKennzeichen(self):
        return self.__kennzeichen
    
    def getGrundpreis(self):
        return self.__grundpreis
    
    def getPreisProKm(self):
        return self.__preisProKM
    
    def setKilometerstand(self, stand):
        self.__kilometerstand = stand
        
    def getTagesfahrstrecke(self):
        return self.__tagesfahrstrecke
    
    def setTagesfahrstrecke(self, stand):
        self.__tagesfahrstrecke = stand
        
    def getKilometerstand(self):
        return self.__kilometerstand
    
class Rikscha(Fahrzeug):
    def __init__(self, kennzeichen):
        super().__init__(kennzeichen, 3, 2.7, 0.5)
        
class Auto(Fahrzeug):
    def __init__(self, kennzeichen, anzSitzplaetze, tankVolumen, verbrauchAuf100km):
        super().__init__(kennzeichen, anzSitzplaetze, 5.8, 1.6)
        self.__tankinhalt = 0.0
        self.__tankVolumen = tankVolumen
        self.__verbrauchAuf100km = verbrauchAuf100km
    
    def berechneFahrpreis(self, strecke):
        self.setKilometerstand(self.getKilometerstand() + strecke)
        self.setTagesfahrstrecke(self.getTagesfahrstrecke() + strecke)
        
        print("     Alter Tankinhalt: " + str(self.__tankinhalt))
        verbrauch = (self.__verbrauchAuf100km * strecke) / 100
        if (verbrauch < self.__tankinhalt):
            self.__tankinhalt -= verbrauch
        else:
            self.__tankinhalt = 0.0
        print("     Neuer Tankinhalt: " + str(self.__tankinhalt))
        
        return "Fahrpreis: " + str((strecke * self.getPreisProKm()) + self.getGrundpreis())
    
    def volltanken(self):
        tankdifferenz = self.__tankVolumen - self.__tankinhalt
        self.__tankinhalt = self.__tankVolumen
        return "Getankte Liter: " + str(tankdifferenz)
    
class Fahrzeugverwaltung():
    def __init__(self, fahrzeuge = []):
        self.__fahrzeuge = []
        for i in range(len(fahrzeuge)):
            self.__fahrzeuge.append(fahrzeuge[i])
    
    def gesamtGefahreneStrecke(self):
        gesamtstrecke = 0.0
        for i in range(len(fahrzeuge)):
            gesamtstrecke += self.__fahrzeuge[i].getTagesfahrstrecke()
            
    # getankte Benzinmenge: Auto benötigt ein Attribut für den Tagesverbrauch → beim Tanken
    # Aktualisierung des Attributes Gesamteinnahmen bei Berechnung des Fahrpreises
    # weiterhin sind die jeweiligen getMethoden in der Klasse Fahrzeugverwaltung notwendig
    
    def sortiereKennzeichenEin(self):
        kennzeichenliste = ["AAA", "AAB", "AAC", "CCB", "CCC"]
        neuesKennzeichen = "BBA" #fahrzeug.getKennzeichen()
        i = 0
        gefunden = False
        while i < len(kennzeichenliste):
        #while i < len(self.__fahrzeuge):
            #aktKenn = self.__fahrzeuge.getKennzeichen(i)
            aktKenn = kennzeichenliste[i]
            j = 0
            while j < len(neuesKennzeichen):
                if(ord(neuesKennzeichen[j]) > ord(aktKenn[j])):
                    i = i + 1
                    break
                
                if(ord(neuesKennzeichen[j]) == ord(aktKenn[j])):
                    j = j + 1
                    continue
                
                kennzeichenliste.insert(i, neuesKennzeichen)
                gefunden = True
                break
            
            if(gefunden):
                break
        print(kennzeichenliste)
        
print(">>Testfahrzeug mit Initiliasierung 0.0:")
testFahrzeug = Fahrzeug()
print(testFahrzeug.berechneFahrpreis(10))

print("\nTestrikscha mit Initilisierung aus Aufgabenstellung und 10km Strecke:")
testRikscha = Rikscha("halloIbims")
print(testRikscha.berechneFahrpreis(10))

print("\nTestauto mit Initilisierung mit 60 Liter Tank und 6 Liter Verbrauch/100km:")
testAuto = Auto("halloIbims", 5, 60, 6)
print("     " + str(testAuto.volltanken()))
print("     " + str(testAuto.berechneFahrpreis(100)))

europcar = Fahrzeugverwaltung()
europcar.sortiereKennzeichenEin()
