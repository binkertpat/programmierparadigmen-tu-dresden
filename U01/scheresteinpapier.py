import random

user=input("Schere, Stein oder Papier?")
pcoptions=['Schere', 'Stein', 'Papier']
pc=random.choice(liste)

if user == pc:
    print("Unentschieden!")
elif user == 'Schere' and pc == 'Papier':
    print("Sie haben gewonnen!")
elif user == 'Papier' and pc == 'Schere':
    print("PC hat gewonnen!")
elif user == 'Stein' and pc == 'Papier':
    print("PC hat gewonnen!")
elif user == 'Papier' and pc == 'Stein':
    print("Sie haben gewonnen!")