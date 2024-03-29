import os
import sys

seznam_ryb = [4, 1, 1, 1, 5, 1, 3, 1, 5, 3, 4, 3, 3, 1, 3, 3, 1, 5, 3, 2, 4, 4, 3, 4, 1, 4, 2, 2, 1, 3, 5, 1, 1, 3, 2,
              5, 1, 1, 4, 2, 5, 4, 3, 2, 5, 3, 3, 4, 5, 4, 3, 5, 4, 2, 5, 5, 2, 2, 2, 3, 5, 5, 4, 2, 1, 1, 5, 1, 4, 3,
              2, 2, 1, 2, 1, 5, 3, 3, 3, 5, 1, 5, 4, 2, 2, 2, 1, 4, 2, 5, 2, 3, 3, 2, 3, 4, 4, 1, 4, 4, 3, 1, 1, 1, 1,
              1, 4, 4, 5, 4, 2, 5, 1, 5, 4, 4, 5, 2, 3, 5, 4, 1, 4, 5, 2, 1, 1, 2, 5, 4, 5, 5, 1, 1, 1, 1, 1, 4, 5, 3,
              1, 3, 4, 3, 3, 1, 5, 4, 2, 1, 4, 4, 4, 1, 1, 3, 1, 3, 5, 3, 1, 4, 5, 3, 5, 1, 1, 2, 2, 4, 4, 1, 4, 1, 3,
              1, 1, 3, 1, 3, 3, 5, 4, 2, 1, 1, 2, 1, 2, 3, 3, 5, 4, 1, 1, 2, 1, 2, 5, 3, 1, 5, 4, 3, 1, 5, 2, 3, 4, 4,
              3, 1, 1, 1, 2, 1, 1, 2, 1, 5, 4, 2, 2, 1, 4, 3, 1, 1, 1, 1, 3, 1, 5, 2, 4, 1, 3, 2, 3, 4, 3, 4, 2, 1, 2,
              1, 2, 4, 2, 1, 5, 2, 2, 5, 5, 1, 1, 2, 3, 1, 1, 1, 3, 5, 1, 3, 5, 1, 3, 3, 2, 4, 5, 5, 3, 1, 4, 1, 5, 2,
              4, 5, 5, 5, 2, 4, 2, 2, 5, 2, 4, 1, 3, 2, 1, 1, 4, 4, 1, 5]

seznam_ryb = [4]

# finds unique values in list
def unique(_seznam_ryb):
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in _seznam_ryb:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # return unique list
    return (unique_list)


def countUniques(_unique_list, _seznam_ryb):
    unique_list_count = []

    for i in range(len(_unique_list)):
        temp = []
        temp.append(_unique_list[i])
        temp.append(0)
        unique_list_count.append(temp)

    for item in range(len(unique_list_count)):
        for ryba in range(len(_seznam_ryb)):

            if _seznam_ryb[ryba] == unique_list_count[item][0]:
                unique_list_count[item][1] += 1

    return (unique_list_count)


class Fish():
    def __init__(self, _timer=8):
        self.timer = _timer

    def starni(self):

        nova_hodnota_timeru = 0

        if self.timer > 1:
            nova_hodnota_timeru = self.timer - 1

        if self.timer == 0:
            novaEyba = Fish()
            hejno.append(novaEyba)
            nova_hodnota_timeru = 6

        self.timer = nova_hodnota_timeru

    def vratMi(self):
        return (self.timer)


def vytvorHejno(_seznam_ryb):
    hejno = []
    for ryba in range(len(_seznam_ryb)):
        vek = _seznam_ryb[ryba]
        ryba = Fish(vek)
        hejno.append(ryba)
    return hejno


hejno = vytvorHejno(seznam_ryb)

for day in range(10):
    print(str(day) + " hejno " + str(len(hejno)))

    for ryba in range(len(hejno)):
        print("vek = " + str(hejno[ryba].vratMi()))

    for ryba in range(len(hejno)):
        hejno[ryba].starni()



unique_list = unique(seznam_ryb)
unique_list_count = countUniques(unique_list, seznam_ryb)