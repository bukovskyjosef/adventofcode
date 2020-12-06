# https://docs.python.org/3/howto/regex.html
import re

file = open('04.txt', 'r')
lines = file.read().splitlines()

passports = [[]]
pNumber = 0

# prepare password fields
for n, line in enumerate(lines):
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
for n, passport in enumerate(passports):
    if ("byr" in passports[n] and "iyr" in passports[n] and "eyr" in passports[n] and "hgt" in passports[n] and "hcl" in passports[n] and "ecl" in passports[n] and "pid" in passports[n]):
        validPassports = validPassports+1

print(validPassports)