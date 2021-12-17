import re

file = open('05input.txt', 'r')
lines = file.read().splitlines()
#lines = ["0,0 -> 0,4", "0,1 -> 3,1","0,0 -> 0,3"]

# metoda vezme ze zadani pouza ta pole kde x1=x2 nebo y1=y2
def sliceIt(_lines):
    temp2 = []
    final_list = []

    for i in range(len(lines)):
        temp = re.split(' |,|-|>', _lines[i])
        #print(lines[i])
        if temp[0] == temp[5] or temp[1] == temp[6]:

            x1_temp = int(temp[0])
            x2_temp = int(temp[5])
            y1_temp = int(temp[1])
            y2_temp = int(temp[6])

            if x1_temp > x2_temp:
                x2 = x1_temp
                x1 = x2_temp
            else:
                x1 = x1_temp
                x2 = x2_temp

            if y1_temp > y2_temp:
                y2 = y1_temp
                y1 = y2_temp
            else:
                y1 = y1_temp
                y2 = y2_temp

            temp2.append(x1) #x1
            temp2.append(y1) #y1
            temp2.append(x2) #x2
            temp2.append(y2) #y2
            final_list.append(temp2)
        temp2 = []

    return final_list


def draw_lines(_filtered_lines, _sea):

    for line in range(len(_filtered_lines)):
        x1 = _filtered_lines[line][0] # 1
        x2 = _filtered_lines[line][2] # 1
        y1 = _filtered_lines[line][1] # 1
        y2 = _filtered_lines[line][3] # 4

        for sloupec in range(len(_sea)):
            for radek in range(len(_sea)):
                if radek >= x1 and radek <= x2 and sloupec >= y1 and sloupec <= y2:
                    sea[sloupec][radek] += 1

    # print("\nnove more")
    # for i in range(len(sea)):
    #     print(sea[i])
    # print()


def create_sea(size):
    temp_sea = []
    line = []
    for i in range(size):
        for j in range(size):
            line.append(0)
        temp_sea.append(line)
        line = []

    return temp_sea


sea = create_sea(999)


# priprav zadani ve forme poli
filtered_lines = sliceIt(lines)

updated_sea = draw_lines(filtered_lines,sea)

pocet = 0

for line in range(len(sea)):
    for item in range(len(sea[line])):
        if sea[line][item] >= 2:
            pocet += 1

print(pocet)

# too high 873923
# too high 47848
# too low 1297
# correct 4826

# 2nd part
# 954973 too high