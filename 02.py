file = open('02.txt', 'r')
Lines = file.readlines()

validOnes = 0

def validate(minimum,maximum,letter,text):
    if (minimum <= text.count(letter) <= maximum):
        valid = True
    else:
        valid = False
    return valid

for line in Lines:
    minimum = int(line.split('-')[0])
    maximum = int(line.split('-')[1].split(' ')[0])
    letter = line.split(' ')[1].split(':')[0]
    text = line.split(': ')[1]
    if (validate(minimum,maximum,letter,text)):
        validOnes = validOnes + 1

print (validOnes)

