note = float(input("Gib deine Prüfungsnote mit Punkt als Komma ein:"))
augenfarbe = int(input("Bewerte deine Augenfarbe → 1 für dunkel und 0 für hell:"))
hunger = int(input("Hast du gerade Hunger? → 1 für ja und 0 für nein:"))
augen = int(input("Ist das Wetter gerade schön? → 1 für schön und 0 für nicht schön:"))

if augenfarbe == 1 and hunger == 0:
    note = note * 1.1
elif augenfarbe == 1 and hunger == 1:
    note = note * 0.9
elif augenfarbe == 0 and hunger == 1:
    note = note * 0.9
elif augenfarbe == 0 and hunger == 0:
    note = note * 1.1
elif wetter == 0:
    note = note - 1
    
print(round(note,1))