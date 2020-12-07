#Open up and clean data
data = []

with open('inputs\input6.txt') as f:
    data = f.read().split('\n\n')
    
dataClean = []
for x in data:
    dataClean.append(x.split('\n'))

#Solution 1

total = 0

for x in data:
    uniqueChars = []
    for char in x:
        if (char not in uniqueChars) and (char != '\n'):
            uniqueChars.append(char)
    total += len(uniqueChars)
    
print(total)

#Solution 2

total = 0

for x in dataClean:
    combinedChars = []
    uniqueCombinedChars = []
    for entry in x:
        for char in entry:
            inAll = True
            for entry2 in x:
                if char in entry2:
                    continue
                else:
                    inAll = False
            if inAll:
                combinedChars.append(char)
    for char in combinedChars:
        if (char not in uniqueCombinedChars) and (char != '\n'):
            uniqueCombinedChars.append(char)
    total += len(uniqueCombinedChars)
    
print(total)

