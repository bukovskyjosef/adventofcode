# https://docs.python.org/3/howto/regex.html
import re

file = open('04.txt', 'r')
lines = file.read().splitlines()

passports = [[]]
pNumber = 0

# prepare password fields
for  line in lines:
    if (line!=""):
        # process line
        regex = re.compile("(byr|iyr|eyr|hgt|hcl|ecl|pid|cid):")

        for i in (regex.findall(line)):
            passports[pNumber].append(i)
    else:
        # start new passport
        passports.append([])
        pNumber = pNumber + 1

validPassports = 0

#validate passports
for passport in passports:
    if ("byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport):
        validPassports = validPassports+1

print(validPassports)