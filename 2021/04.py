# třída item reprezentuje položku herní matice
class Item:
    def __init__(self, _value):
        self.value = _value
        self.announced = 0

    def mark_as_announced(self):
        self.announced = 1

    def return_announced(self):
        return self.announced

    def return_value(self):
        return int(self.value)

#metoda vytvoří [] matic, kde jednotlive itemy jsou objekty tridy Item
def create_matrix_list(lines):
    matrix_list = []
    matrix = []
    for i in range(2, len(lines)):
        # pokud ma matice 5 radku, pridej ji do listu matic
        if len(matrix) == 5:
            matrix_list.append(matrix)
            matrix = []
        elif len(lines[i]) > 0:
            #pridej do matice radek objektů Item
            values_temp_list = lines[i].split()
            items_temp_list = []
            for j in range(len(values_temp_list)):
                items_temp_list.append(Item(values_temp_list[j]))
            matrix.append(items_temp_list)

    return matrix_list

# metoda má zkontrolovat, zda matice, přijatá v parametru splňuje podmínky výhry
def checkWin(matrix):

    soucetRadku = 0
    soucetSloupcu = 0

    #součet řádků
    for radek in range(len(matrix[0])):
        for item in range(len(matrix[radek])):
            if matrix[radek][item].return_announced() == 1:
                soucetRadku = soucetRadku + 1
        if soucetRadku < 5 : soucetRadku = 0

    #součet sloupců
    for sloupec in range(len(matrix[0])):
        for radek in range(len(matrix[radek])):
            if matrix[radek][sloupec].return_announced() == 1:
                soucetSloupcu = soucetSloupcu + 1
        if soucetSloupcu < 5 : soucetSloupcu = 0

    if soucetRadku >= 5 or soucetSloupcu >= 5:
        # print("soucet radku : " + str(soucetRadku))
        # print("soucetSloupcu : " + str(soucetSloupcu))
        vysledek = 1
    else:
        vysledek = 0

    return vysledek

# metoda má za úkol vypočítat z výherní matice odpoveď na zadání úkolu.
def countWinnerMatrix(matrix, announcedNumber):
    soucet = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j].return_announced() == 0:
                soucet = soucet + matrix[i][j].return_value()
    vysledek = soucet * announcedNumber

    print(vysledek)

file = open('04input.txt', 'r')
lines = file.read().splitlines()

#načtení vyhlašovaných čísel
announcedNumbers = lines[0].split(",")

# naplnění pole herních matic
matrix_list = create_matrix_list(lines)

pocetMatic = len(matrix_list)
pocetVyhernichMatic = 0
maticeCoVyhraly = []
posledniVyhleseneCislo = 0

end = 0

# zbytek kódu není v metodě ale v těle programu
# pro každé vyhlašené číslo
for announcedNumber in range(len(announcedNumbers)):
        #pro každou matici
        for matrix in range(len(matrix_list)):

            if end == 1:
                break

            #pro každý řádek v matici
            for line in range(len(matrix_list[matrix])):
                #pro každý objěkt v řádku matice
                for item in range(len(matrix_list[matrix][line])):
                    #pokud jde o právě vyhlášené číslo
                    if matrix_list[matrix][line][item].return_value() == int(announcedNumbers[announcedNumber]):
                        #označ jej za uhodnuté
                        matrix_list[matrix][line][item].mark_as_announced()
            #zkontroluj, zda je matice výherní
            if checkWin(matrix_list[matrix]):
                # když je matice výherní, tak
                # print("matrix: " + str(matrix))
                # print("announced number: " + str(announcedNumbers[announcedNumber]))
                # for radek in range(len(matrix_list[matrix])):
                #     for hodnota in range(len(matrix_list[matrix][radek])):
                #         str1 = str(matrix_list[matrix][radek][hodnota].return_value())
                #         str2 = str(matrix_list[matrix][radek][hodnota].return_announced())
                #         #print(str1, end = " ")
                #         print(str2, end=" ")
                #     print()

                #pokud ještě není v seznamu vyhraných matic, přidej ji tam
                if matrix not in maticeCoVyhraly:
                    maticeCoVyhraly.append(matrix)
                    if(len(maticeCoVyhraly) == 99):
                        posledniVyhleseneCislo = int(announcedNumbers[announcedNumber])
                        delka = len(maticeCoVyhraly) - 1
                        posledniMatice = (maticeCoVyhraly[delka])
                        print(posledniMatice, posledniVyhleseneCislo)
                        countWinnerMatrix(matrix_list[posledniMatice], posledniVyhleseneCislo)


                #end = 1

# 59598 too low
# 60249 too low
# 61060 too low
# 64084 correct for 1st part