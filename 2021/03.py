file = open('03input.txt', 'r')
lines = file.read().splitlines()

numberOfColumns = int(len(lines[0]))
report = int(len(lines))

print("Délka řádku je " + str(numberOfColumns) + " prvků.\nDiagnostický report má " + str(report) + " řádků.")

#naplneni registru poly polí
registr = []

for i in range(numberOfColumns):
    temp = []
    for j in range(report):
        temp.append(lines[j][i])
    registr.append(temp)

#výpočet četnosti prvků
i = 0
j = 0
temp = []

for i in range(int(len(registr))):
    temp = registr[i]
    #print(registr[i])
    nula = sum(1 for item in temp if item==("0"))
    jednicka = sum(1 for item in temp if item==("1"))
    #print(nula)
    #print(jednicka)

    if(nula > jednicka):
        registr[i] = 0
    else:
        registr[i] = 1

print("Výsledek registru:" + str(registr))

binarniCislo0 = ""
binarniCislo1 = ""

for o in registr:
    if (registr[o] ==0):
        binarniCislo0 = binarniCislo0 + "0"
        binarniCislo1 = binarniCislo1 + "1"
    else:
        binarniCislo0 = binarniCislo0 + "1"
        binarniCislo1 = binarniCislo1 + "0"

print("binar0 " + str(binarniCislo0))
print("binra1 " + str(binarniCislo1))

vysledek = int(binarniCislo0, 2) * int(binarniCislo1, 2)
print(vysledek)