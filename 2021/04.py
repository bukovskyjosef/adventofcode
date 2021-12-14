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
        return self.value


class BingoMatrix:
    def __init__(self, _data, _name):
        self.data = _data
        self.name = _name

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
            for j in range(len(docasnyList)):
                matrix.append(Item(docasnyList[j]))
    return matrix_list


file = open('04input.txt', 'r')
lines = file.read().splitlines()


#načtení vyhlašovaných čísel v bingo
vyhlasovanaCisla = lines[0]
matrix_list = create_matrix_list(lines)

print(matrix_list[0][0].return_value())
print(matrix_list[0][0].return_announced())





