# First star 
file1 = open('01.txt', 'r')
lines = file1.read().splitlines()

for n, line in enumerate(lines):
  for i in range(len(lines)-n):
    if (int(lines[n+i]))+int(line) == 2020:
      hello = int(line) * int(lines[n+i])

print(hello)

# Second star
doubles = []

for n, line in enumerate(lines):
  for i in range(len(lines)-n):
    if ((int(lines[n+i]))+int(line)) < 2020:
        doubles.append([(int(lines[n+i])), int(line), (int(lines[n+i]))+int(line)])

for single in lines:
    count = 0
    for i in doubles:
        if (doubles[count][2]+int(single) == 2020):
            print(doubles[count][0]*doubles[count][1]*int(single))
        count = count + 1