class Person:
    def __init__(self, name, geburtstag):
        self._name = name
        self._geburtstag = geburtstag
    
    def print(self):
        return self._name + " " + self._geburtstag
    
    def getGeburtstag(self):
        return self._geburtstag
    
    def setGeburtstag(self, datum):
        self._geburtstag = datum
        
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
        
class Angestellte(Person):
    def __init__(self, name, geburtstag, gehalt):
        super().__init__(name, geburtstag)
        self.__gehalt = gehalt

    def getGehalt(self, istChef):
        if (istChef == True):
            return self.__gehalt
        
    def setGehalt(self, istChef, gehalt):
        if (istChef == True):
            self.__gehalt = gehalt
            
    def print(self):
        return self.getName() + self.getGeburtstag() + self.getGehalt()
    
class Kunde(Person):
    def __init__(self, name, geburtstag, treueKunde):
        super().__init__(name, geburtstag)
        self.__treueKunde = treueKunde
        self.__konten = []

    def getTreueKunde(self, istAngestellter = True):
        if (istAngestellter == True):
            return self.__treueKunde
        
    def setTreueKunde(self, treuekunde, istAngestellter):
        if ((istAngestellter == True) and (treuekunde == True)):
            self.__treueKunde = True
            
    def setKonten(self, konto):
        self.__konten.append(konto)
        
    def print(self):
        return self.getName() + "; " + self.getGeburtstag() + "; " + str(self.getTreueKunde())
    
class Betrag():
    def __init__(self, wert, wahrungszeichen = "$", wechselkurs = 1.0):
        self.__wert = wert
        self.__wahrungszeichen = wahrungszeichen
        self.__wechselkurs = wechselkurs
        self.__konten = []
        
    def negativerWert(self):
        if (self.__wert < 0.0):
            True
        else:
            False
            
    def berecheBetragMitZins(self, zins):
        self.__wert = self.__wert + (self.__wert * zins)
        
    def setWert(self, wert):
        self.__wert = wert
        
    def getWert(self):
        return self.__wert
    
    def setWaehrungszeichen(self, zeichen):
        self.__wahrungszeichen = zeichen
        
    def getWaehrungszeichen(self):
        return self.__wahrungszeichen
    
    def getWechselkurs(self):
        return self.__wechselkurs
    
    def setWechselkurs(self, kurs):
        self.__wechselkurs = kurs
        
    def setKonten(self, konto):
        self.__konten.append(konto)
            
    def printBetrag(self):
        return str(self.__wert) + self.__wahrungszeichen 
        
        
class Euro(Betrag):
    def umrechnungZuDollar(self):
        setWert(self.getWert() * self.getWechselkurs())
        
class Dollar(Betrag):
    def umrechnungZuEuro(self):
        setWert(self.getWert() * self.getWechselkurs())

class Bank():
    def __init__(self, vermoegen, bankleitzahl = "WELADED1STB"):
        self.__vermoegen = vermoegen
        self.__bankleitzahl = bankleitzahl
        self.__konten = []

    def stelleNeueLeuteEin(self):
        pass
    
    def schließeNeuenVertragAb(self):
        pass
    
    def getVermoegen(self, istBankangestellter):
        if(istBankangestellter):
            return self.__vermoegen

    def getBankleitzahl(self):
        return self.__bankleitzahl
    
    def setVermoegen(self, istBankangestellter, wert):
        if(istBankangestellter):
            self.__vermoegen = wert
            
    def setKonten(self, konto):
        self.__konten.append(konto)
            
    def setBankleitzahl(self, blz):
        self.__bankleitzahl = blz

class Konto():
    def __init__(self, kontostand, kontonummer, sinssatz):
        self.__kontostand = kontostand
        self.__kontonummer = kontonummer
        self._sinssatz = sinssatz
    
    def einzahlen(self, betrag):
        self.__kontostand += betrag
        
    def abheben(self, betrag):
        self.__kontostand -= betrag
        
    def verzinsen(self, betrag):
        return betrag + (betrag * self._zinssatz)
    
    def umbuchen(self, kontonummer, wert):
        self.__kontostand -= wert
        return [kontonummer, wert]
        
    def getKontostand(self):
        return self.__kontostand

    def getKontonummer(self):
        return self.__kontonummer
    
    def setKontostand(self, wert):
        self.__kontostand = wert
        
    def setKontonummer(self, kontonummer):
        self.__kontonummer = kontonummer
        
    def print(self):
        return self.__kontonummer + str(self.__kontostand)
    
    
class Sparkonto(Konto):
    def abheben(self, betrag):
        if ((self.getKontostand() - betrag) >= 0):
            self.setKontostand(self.getKontostand() - betrag)
            return True
        
    def umbuchen(self, iban, betrag):
        if ((self.getKontostand() - betrag) >= 0):
            self.setKontostand(self.getKontostand() - betrag)
            return True
    
    def print(self):
        print("Ich bin ein Sparkonto.")
    
class Girokonto(Konto):
    def print(self):
        print("Ich bin ein Girokonto")
        