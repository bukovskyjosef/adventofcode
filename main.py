# Using readlines() 
file1 = open('expanses.txt', 'r') 
Lines = file1.readlines()

for n, line in enumerate(Lines): 
  for i in range(len(Lines)-n):
    if (int(Lines[n+i]))+int(line) == 2020:
      hello = int(line) * int(Lines[n+i])

print (hello)
  #print("Line{}: {}".format(count, line.strip()))