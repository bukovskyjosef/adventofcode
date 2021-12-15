# třída item reprezentuje položku herní matice
class Item:
    def __init__(self, _value):
        self.value = _value
        self.announced = 0

    def mark_as_announced(self):
        self.announced = 1
        return "announced"

    def return_announced(self):
        return self.announced

    def return_value(self):
        return int(self.value)


def create_matrix_list(lines):
    matrix_list = []
    matrix = []
    for i in range(2, len(lines)):
        # pokud ma matice 5 radku, pridej ji do listu matic
        if len(matrix) == 5:
            matrix_list.append(matrix)
            matrix = []
        elif len(lines[i]) == 0:
            print()
        else:
            #pridej do matice radek objektů Item
            docasnyList = lines[i].split()
            docasnyList2 = []
            for item in range(len(docasnyList)):
                docasnyList2.append(Item(docasnyList[item]))
            matrix.append(docasnyList2)
    return matrix_list

def checkWin(matrix):

    soucetRadku = 0
    soucetSloupcu = 0

    #součet řádků
    for radek in range(len(matrix[0])):
        for item in range(len(matrix[radek])):
            if matrix[radek][item].return_announced() == 1:
                soucetRadku = soucetRadku + 1

    #součét sloupců
    for radek in range(len(matrix)):
        if matrix[radek][radek].return_announced() == 1:
            soucetSloupcu = soucetSloupcu + 1

    if soucetRadku == 5 or soucetSloupcu == 5:
        vysledek = 1
    else:
        vysledek = 0
    return vysledek

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
matrix_list = create_matrix_list(lines)


end = 0
for announcedNumber in range(len(announcedNumbers)):
    if end == 1:
        break
    else:
        for matrix in range(len(matrix_list)):
            for line in range(len(matrix_list[matrix])):
                for item in range(len(matrix_list[matrix][line])):
                    if matrix_list[matrix][line][item].return_value() == int(announcedNumbers[announcedNumber]):
                        matrix_list[matrix][line][item].mark_as_announced()
            if checkWin(matrix_list[matrix]):
                countWinnerMatrix(matrix_list[matrix],int(announcedNumbers[announcedNumber]))
                end = 1
                break

#
# 60249 too low
