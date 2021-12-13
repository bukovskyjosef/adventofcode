file = open('03input.txt', 'r')
lines = file.read().splitlines()

#metoda vratVyssiCetnost() vrátí větší z hodnot 0,1 na zadané pozici ve stringu
#@pole seznam hodnot k proházení
#@pozice kterou pozici počítáme
def vratVyssiCetnost(pole, pozice):
    nula = 0
    jednicka = 0
    for i in range(len(pole)):
        if (pole[i][pozice] == "1"):
            jednicka += 1
        elif (pole[i][pozice]=="0"):
            nula += 1
        else:
            print("error, zadaná hodnota není ani jednička ani nula")
    if nula > jednicka:
        zjistenaHodnota = 0
    elif nula == jednicka:
        zjistenaHodnota = 1
    else:
        zjistenaHodnota = 1
    return zjistenaHodnota

# metoda vratNizsiCetnost() vrátí menší z hodnot 0,1 na zadané pozici ve stringu
# @pole seznam hodnot k proházení
# @pozice kterou pozici počítáme
def vratNizsiCetnost(pole, pozice):
    nula = 0
    jednicka = 0
    for i in range(len(pole)):
        if (pole[i][pozice] == "1"):
            jednicka += 1
        elif (pole[i][pozice]=="0"):
            nula += 1
        else:
            print("error, zadaná hodnota není ani jednička ani nula")
    if nula < jednicka:
        zjistenaHodnota = 0
    elif nula == jednicka:
        zjistenaHodnota = 0
    else:
        zjistenaHodnota = 1
    return zjistenaHodnota

# metoda filtruj() vytvori nove pole, ktere obsahuje pouze polozky ze vstupniho pole,
# ktere maji na n-te pozici hodnotu definovanou podminkou
# @lines vstupni pole
# @podminka hodnota pro porovnani
# @pozice porovnavana pozice
def filtruj(lines, podminka, pozice):
    filtrovanePole=[]
    for i in range(len(lines)):
        if (lines[i][pozice] == str(podminka)):
            filtrovanePole.append(lines[i])
    return filtrovanePole

pozice = 0
for i in range(len(lines[0])):
    if len(lines)>1:
        lines = filtruj(lines,vratVyssiCetnost(lines,pozice),i)
    pozice += 1

binarniCislo0 = str(lines[0])
print("binarniCislo0 = " + str(binarniCislo0) + " = " + str(int(binarniCislo0, 2)))

pozice = 0
file = open('03input.txt', 'r')
lines = file.read().splitlines()

for j in range(len(lines[0])):
    if len(lines)>1:
        lines = filtruj(lines,vratNizsiCetnost(lines,pozice),j)
    pozice += 1

binarniCislo1 = str(lines[0])
print("binarniCislo1 = " + str(binarniCislo1) + " = " + str(int(binarniCislo1, 2)))

vysledek = int(binarniCislo0, 2) * int(binarniCislo1, 2)
print("Výsledek: " + str(int(binarniCislo0, 2)) + " * " + str(int(binarniCislo1, 2)) + " = " + str(vysledek))

#3654234 too high