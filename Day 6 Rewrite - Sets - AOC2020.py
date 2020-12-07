#Open up and clean data
data = []

with open('inputs\input6.txt') as f:
    data = f.read().split('\n\n')
    
dataClean = []
for x in data:
    dataClean.append(x.split('\n'))


#Solution 1 with sets
total = 0

for x in data:
    x = "".join(x.split()) #remove all white space characters
    total += len(set(x)) #sets remove all duplicate values

print(total)


#Solution 2 with sets

total = 0

for group in dataClean:
    compSet = set(group[0]) 
    for i in range(len(group[1:])):
        compSet = compSet.intersection(set(group[i+1]))
    total += len(compSet)

print(total)

