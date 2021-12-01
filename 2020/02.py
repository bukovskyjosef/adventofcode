file = open('02.txt', 'r')
Lines = file.readlines()

validOnesFirstStar = 0
validOnesSecondStar = 0

def validateFirstStar(minimum, maximum, letter, text):
    if (minimum <= text.count(letter) <= maximum):
        valid = True
    else:
        valid = False
    return valid

def validateSecondStar(first, second, letter, text):
    if ((text[first-1]==letter) ^ (text[second-1]==letter)):
        print(line)
        valid = True
    else:
        valid = False
    return valid

for line in Lines:
    minimum = int(line.split('-')[0])
    maximum = int(line.split('-')[1].split(' ')[0])
    letter = line.split(' ')[1].split(':')[0]
    text = line.split(': ')[1]
    if (validateFirstStar(minimum, maximum, letter, text)):
        validOnesFirstStar = validOnesFirstStar + 1
    if (validateSecondStar(minimum, maximum, letter, text)):
        validOnesSecondStar = validOnesSecondStar + 1

print ("Validní pro prvnní hvězdu:", validOnesFirstStar)
print ("Validní pro druhou hvězdu:", validOnesSecondStar)



