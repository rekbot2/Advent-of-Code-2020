#Read data
data = []

with open('inputs\input2.txt') as f:
    for line in f.readlines():
        splitLine=line.strip().split(' ')
        splitLine[0] = splitLine[0].split('-')
        data.append(splitLine)

#Solution 1
good = 0
bad = 0

for entry in data:
    charCount = entry[2].count(entry[1].strip(':'))
    if int(entry[0][0]) <= charCount and charCount <= int(entry[0][1]):
        good += 1
    else:
        bad += 1

print(good,bad)

#Solution 2
good = 0
bad = 0

for entry in data:
    charTarget = entry[1].strip(':')
    if (entry[2][int(entry[0][0])-1]== charTarget) ^ (entry[2][int(entry[0][1])-1] == charTarget):
        good += 1
    else:
        bad += 1

print(good,bad)

