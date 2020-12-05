#line lenght = 31
# First star
file1 = open('03.txt', 'r')
lines = file1.read().splitlines()

# Slopes in second star
# 1 Right 1, down 1.
# 2 Right 3, down 1. (This is the slope you already checked.)
# 3 Right 5, down 1.
# 4 Right 7, down 1.
# 5 Right 1, down 2.

trees1 = 0
trees2 = 0
trees3 = 0
trees4 = 0
trees5 = 0
x = 0


# first slope
for n, line in enumerate(lines):
    if (line[x]=="#"):
        trees1= trees1+1
    #print('n {}, line:  {}, char {} x: {} trees1 {}'.format(n, line, line[x], x, trees1))
    if (x<30):
        x=x+1
    else:
        x=0
x=0

# second slope
for n, line in enumerate(lines):
    if (line[x]=="#"):
        trees2=trees2+1
    #print('n {}, line:  {}, char {} x: {} trees2 {}'.format(n, line, line[x], x, trees2))
    if (x<28):
        x=x+3
    else:
        if (x==28):
            x=0
        if (x==29):
            x=1
        if (x==30):
            x=2
x=0
line=""

# third slope
for n, line in enumerate(lines):
    if (line[x]=="#"):
        trees3=trees3+1
    #print('n {}, line:  {}, char {} x: {} trees3 {}'.format(n, line, line[x], x, trees3))
    if (x<26):
        x=x+5
    else:
        if (x==26):
            x=0
        if (x==27):
            x=1
        if (x==28):
            x=2
        if (x==29):
            x=3
        if (x==30):
            x=4
x=0

# fourth slope
for line in lines:
    if (line[x]=="#"):
        trees4=trees4+1
    if (x<24):
        x=x+7
    else:
        if (x==24):
            x=0
        if (x==25):
            x=1
        if (x==26):
            x=2
        if (x==27):
            x=3
        if (x==28):
            x=4
        if (x==29):
            x=5
        if (x==30):
            x=6
x=0

# fifth slope
for n, line in enumerate(lines):
    if(n==0 or n%2==0):
        if (line[x]=="#"):
            trees5=trees5+1
        #print('n {}, line:  {}, char {} x: {} trees5 {}'.format(n, line, line[x], x, trees5))
        if (x<30):
            x=x+1
        else:
            x=0

print(trees1)
print(trees2)
print(trees3)
print(trees4)
print(trees5)
print(trees1*trees2*trees3*trees4*trees5)
