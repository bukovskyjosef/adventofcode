# First star
file1 = open('03.txt', 'r')
lines = file1.read().splitlines()

print(len(lines[0]))
#line lenght = 31

letter =""
trees = 0
x = 0

for line in lines:

    print(line,line[x], x)

    if (line[x] == "#"):
        trees = trees + 1

    if (x<28):
        x = x+3
    else:
        if (x==28):
            x = 0
        if (x==29):
            x = 1
        if (x == 30):
            x = 2

print(trees)

#wrong:  285