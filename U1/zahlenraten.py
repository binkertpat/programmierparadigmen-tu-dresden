import random

user = int(input("Rate eine Zahl zwischen 1 und 10: "))
pc = random.randint(1,10)
versuche = 0

while pc != user:
    versuche = versuche + 1
    if pc<user:
        print("Die gesuchte Zahl ist kleiner!")
        user = int(input("Probier es nochmal: "))
    elif pc > user:
        print("Die gesuchte Zahl ist größer!")
        user = int(input("Probier es nochmal: "))
print("Richtig! Du hast " + str(versuche) + " Versuche benötigt.")