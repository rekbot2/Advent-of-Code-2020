#Open file 
file = open('inputs\input4.txt')
data = file.read().split('\n\n')
file.close()

#Clean input
dataClean = []

for x in data:
    dataClean.append(x.split()) #Split with no argument splits on whitespace

#Solution 1
reqFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

valid = 0

for passport in dataClean:
    reqsMet = 0
    for field in passport:
        field = field.split(':')
        if field[0] in reqFields:
            reqsMet += 1
    if reqsMet == 7:
        valid += 1
        
print(valid)

#Solution 2
reqFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
validEcl = ['amb','blu','brn','gry','grn','hzl','oth']
validHcl = '0123456789abcdef'

valid = 0

for passport in dataClean:
    reqsMet = 0
    for field in passport:
        field = field.split(':')
        if field[0] == reqFields[0]:                                       #byr field
            if int(field[1]) <= 2002 and int(field[1]) >= 1920:
                reqsMet += 1
        elif field[0] == reqFields[1]:                                     #iyr field
            if int(field[1]) <= 2020 and int(field[1]) >= 2010:
                reqsMet += 1
        elif field[0] == reqFields[2]:                                     #eyr field
            if int(field[1]) <= 2030 and int(field[1]) >= 2020:
                reqsMet += 1
        elif field[0] == reqFields[3]:                                     #hgt field (sketchyy)                         
            if 'cm' in field[1]:
                field[1] = field[1].split('c')
            elif 'in' in field[1]:
                field[1] = field[1].split('i')
            if field[1][1] == 'n':
                if int(field[1][0]) <= 76 and (int(field[1][0]) >= 59):
                    reqsMet += 1
            elif field[1][1] == 'm':
                if int(field[1][0]) <= 193 and (int(field[1][0]) >= 150):
                    reqsMet += 1
        elif field[0] == reqFields[4]:                                     #hcl field
            validHclChars = 0
            for c in field[1][1:]:
                if c in validHcl:
                    validHclChars += 1
            if field[1][0] == '#' and (validHclChars == 6):
                reqsMet += 1
        elif field[0] == reqFields[5]:                                     #ecl field
            if field[1] in validEcl:
                reqsMet += 1
        elif field[0] == reqFields[6]:                                     #pid field                               
            if field[1].isnumeric() and (len(field[1]) == 9):
                reqsMet += 1
                
    if reqsMet == 7:
        valid += 1
        
print(valid)

