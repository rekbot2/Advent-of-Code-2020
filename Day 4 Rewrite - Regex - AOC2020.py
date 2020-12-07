#Open file 
file = open('inputs\input4.txt')
data = file.read().split('\n\n')
file.close()

#Clean input
dataClean = []

for x in data:
    dataClean.append(x.split()) #Split with no argument splits on whitespace


#Define functions
import re

def validatePassport(passport,reqFields,rules=None):
    passportFields = [i.split(':')[0] for i in passport]
    validPassport = set(reqFields).issubset(set(passportFields))
    if validPassport and (rules != None):
        for entry in passport:
            entry = entry.split(':')
            if re.match(rules[entry[0]],entry[1].strip()):
                continue
            else:
                validPassport = False
    return validPassport


#Solution 1 with sets
reqFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

valid = 0

for passport in dataClean:
    if validatePassport(passport,reqFields):
        valid+=1
        
print(valid)


#Solution 2 with Regex
reqFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

rules = {
    'byr' : r'^(19[2-9]\d)|(200[0-2])$',
    'iyr' : r'^(201\d)|2020$',
    'eyr' : r'^(202\d)|2030$',
    'hgt' : r'^(1[5-8]\dcm|19[0-3]cm)|(59in|6\din|7[0-6]in)$',
    'hcl' : r'^#[\da-fA-F]{6}$',
    'ecl' : r'^(amb|blu|brn|gry|grn|hzl|oth)$',
    'pid' : r'^\d{9}$',
    'cid' : r'^.*$'
}

valid = 0

for passport in dataClean:
    if validatePassport(passport,reqFields,rules):
        valid += 1
        
print(valid)

