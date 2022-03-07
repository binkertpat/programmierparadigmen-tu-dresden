def binIchEinPalindrom(wort):
    if len(wort) < 2:
        return True
    elif wort[0] != wort[-1]:
        return False
    wort.pop(0)
    wort.pop(-1)
    return binIchEinPalindrom(wort)

def ausgabe():
    if binIchEinPalindrom(list(input(str("Gebe ein Wort ein: ")))):
        print("Palindrom")
    else:
        print("Kein Palindrom")

ausgabe()