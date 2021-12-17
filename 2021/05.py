import re

file = open('05input.txt', 'r')
lines = file.read().splitlines()
lines = ["0,1 -> 0,4"]

# metoda vezme ze zadani pouza ta pole kde x1=x2 nebo y1=y2
def sliceIt(_lines):
    temp2 = []
    final_list = []

    for i in range(len(lines)):
        temp = re.split(' |,|-|>', _lines[i])

        if temp[0] == temp[5] or temp[1] == temp[6]:
            temp2.append(int(temp[0]))
            temp2.append(int(temp[1]))
            temp2.append(int(temp[5]))
            temp2.append(int(temp[6]))
            final_list.append(temp2)
        temp2 = []

    return final_list


def draw_lines(_filtered_lines, _sea):
    print(_filtered_lines)

    for radek in range(_filtered_lines[0][0],_filtered_lines[0][2]):
        print("a")

    return


def create_sea(size):
    temp_sea = []
    line = []
    for i in range(size):
        for j in range(size):
            line.append(0)
        temp_sea.append(line)
        line = []

    return temp_sea


sea = create_sea(5)

print()
for i in range(len(sea)):
    print(sea[i])
print()

# priprav zadani ve forme poli
filtered_lines = sliceIt(lines)

draw_lines(filtered_lines,sea)