## zadání úkolu https://adventofcode.com/2021/day/2
## řešení pouze druhé úlohy

file = open('02input.txt', 'r')
lines = file.read().splitlines()

aim = 0
hor = 0
depth = 0

for i in lines:

    order = str(i.split(" ",1)[0])
    value = int(i.split(" ",1)[1])

    if order=="forward":
        hor += value
        depth = depth+(aim*value)
    if order=="up":
        aim -= value
    if order=="down":
        aim += value

print("horizontal value = " + str(hor))
print("depth = " + str(depth))
print(hor*depth)