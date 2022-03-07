def binIchEinPalindromWhile(wort):
    x = 0
    y = len(wort) - 1
    while (y > x):
        if (wort[x] != wort[y]):
            return "Kein Palindrom"
        x = x + 1
        y = y - 1       
    return "Palindrom"

def binIchEinPalindromFor(wort):
    for i in range(0,int(len(wort)/2)):
        if wort[i] == wort[len(wort)-i-1]:
            return "Palindrom"
        else:
            return "Kein Palindrom"
        
def ausgabe():
    print(binIchEinPalindromFor(list(str(input("Gebe ein Wort ein: ")))))

ausgabe()
