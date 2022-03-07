"""
zaehler1=int(input("Zaehler1: "))
nenner1=int(input("Nenner1: "))
zaehler2=int(input("Zaehler2: "))
nenner2=int(input("Nenner2: "))
zaehler3=int(input("Zaehler3: "))
nenner3=int(input("Nenner3: "))

print(((zaehler1/nenner1)*(nenner2/zaehler2))*((nenner3/zaehler3)))
"""
"""
liste=[]
i=1
while i<=50:
    i=i+1
    liste.append(4)

for l in liste:
        print(l)
print('Ende')
"""
"""
import random
liste=[]
i=1
while i<=50:
    i=i+1
    liste.append(random.randint(1,1000))
    
for l in liste:
        print(l)
print('Ende')
"""
"""
m=int(input())
liste=[]
i=1
while i<=m:
    i=i+1
    liste.append(4)

for l in liste:
        print(l)
print('Ende')
"""
"""
import random
m=int(input())
liste=[]
i=1
while i<=m:
    i=i+1
    liste.append(random.randint(0,20))

for l in liste:
        print(l)
print('Ende')
"""
"""
user=input("Schere, Stein oder Papier?")
import random
liste=['Schere', 'Stein', 'Papier']
pc=random.choice(liste)
if user==pc:
    print("Unentschieden")
elif user=='Schere' and pc=='Papier':
    print("Sie haben gewonnen")
elif user=='Papier' and pc=='Schere':
    print("PC hat gewonnen")
elif user=='Stein' and pc=='Papier':
    print("PC hat gewonnen")
elif user=='Papier' and pc=='Stein':
    print("Sie haben gewonnen")
"""

user=int(input("Rate eine Zahl zwischen 1 und 10: "))
import random
pc=random.randint(1,10)

while pc!=user:
    if pc<user:
        print("Die gesuchte Zahl ist kleiner!")
        user=int(input("Probier es nochmal: "))
    elif pc>user:
        print("Die gesuchte Zahl ist größer!")
        user=int(input("Probier es nochmal: "))
print("Richtig!")