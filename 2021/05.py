import re

file = open('05input.txt', 'r')
lines = file.read().splitlines()
# lines = ["1,1 -> 1,4"]


def sliceIt(_lines):
    temp2 = []
    final_list_unordered = []

    for i in range(len(lines)):
        temp = re.split(' |,|-|>', _lines[i])
        temp2.append(int(temp[0]))
        temp2.append(int(temp[1]))
        temp2.append(int(temp[5]))
        temp2.append(int(temp[6]))
        final_list_unordered.append(temp2)
        temp2 = []

    return final_list_unordered


def draw_lines(_lines, _sea):
    for line in range(len(_lines)):
        x1 = _lines[line][0]
        x2 = _lines[line][2]
        y1 = _lines[line][1]
        y2 = _lines[line][3]

        x1_temp = _lines[line][0]
        x2_temp = _lines[line][2]
        y1_temp = _lines[line][1]
        y2_temp = _lines[line][3]

        # horizontalni tam
        # 0,0 -> 0,4  x1 == x2 and y1 < y2
        # horizontalni  zpět
        # 0,4 -> 0,0  x1 == x2 and y1 > y2
        #
        # vertikální tam
        # 0,0 -> 2,0  x1 < x2 and y1 == y2
        # vertikální zpět
        # 2,0 -> 0,0  x1 > x2 and y1 == y2
        #
        # úhlopříčka tam
        # 2,0 -> 4,2  x2-x1 == y2-y1 and x1 < x2 and y1 < y2
        # úhlopříčka zpět
        # 4,2 -> 2,0  x1-x2 == y1-y2 and x1 > x2 and y1 > y2
        #
        # uhlopříčka tam 2
        # 0,4 -> 3,1  x2-x1 == y1-y2 and x1 < x2 and y1 > y2
        # úhlopříčka zpět 2
        # 3,1 -> 0,4  x1-x2 == y2-y1 and x1 > x2 and y1 < y2

        # menší dopředu pro horizontální
        if x1 == x2 and y1 > y2:
            y1 = y2_temp
            y2 = y1_temp

        # menší dopředu pro vertikální
        if x1 > x2 and y1 == y2:
            x1 = x2_temp
            x2 = x1_temp

        # srovnání uhlopříčka zpět a zpět2
        if (x1 - x2 == y1 - y2 and x1 > x2 and y1 > y2) or (x1 - x2 == y2 - y1 and x1 > x2 and y1 < y2):
            x1 = x2_temp
            x2 = x1_temp
            y1 = y2_temp
            y2 = y1_temp

        if x1 == x2 and y1 < y2:
            # print("x1 == x2 and y1 < y2")
            temp_line = []
            pocet = y2 - y1

            for i in range(0, pocet+1):
                temp_line.append([x1, y1 + i])

            for j in range(len(temp_line)):
                sea[temp_line[j][0]][temp_line[j][1]] += 1

        if x1 < x2 and y1 == y2:
            # print("x1 < x2 and y1 == y2")
            temp_line = []
            pocet = x2 - x1

            for i in range(0, pocet+1):
                temp_line.append([x1 + i, y1])

            for j in range(len(temp_line)):
                sea[temp_line[j][0]][temp_line[j][1]] += 1

        if x2 - x1 == y2 - y1 and x1 < x2 and y1 < y2:
            # print("x2 - x1 == y2 - y1 and x1 < x2 and y1 < y2")
            temp_line = []
            pocet = x2 - x1

            for i in range(0, pocet + 1):
                temp_line.append([x1 + i, y1 + i])

            for j in range(len(temp_line)):
                sea[temp_line[j][0]][temp_line[j][1]] += 1

        if x2 - x1 == y1 - y2 and x1 < x2 and y1 > y2:
            # print("x2 - x1 == y1 - y2 and x1 < x2 and y1 > y2")
            temp_line = []
            pocet = x2 - x1

            for i in range(0, pocet + 1):
                temp_line.append([x1 + i, y1 - i])

            for j in range(len(temp_line)):
                sea[temp_line[j][0]][temp_line[j][1]] += 1

        # for i in range(len(sea)):
        #     print(sea[i])
        # print("\n")


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
lines = sliceIt(lines)
updated_sea = draw_lines(lines, sea)
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
# 20047 too high
# 16793 CORRECT
# 16891 wrong
# 16749 wrong
# 13974 low
