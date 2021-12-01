## zadání úkolu https://adventofcode.com/2021/day/1

file = open('01input.txt', 'r')
lines = file.read().splitlines()

sum = 0

for n in range(len(lines)-1):

    if int(lines[n]) < int(lines[n+1]):
        sum += 1

print(sum)