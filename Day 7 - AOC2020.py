#Open up and clean data
data = []

with open('inputs\input7.txt') as f:
    data = f.readlines()
    
dataClean = []

for entry in data:
    entry = entry.strip('.\n').replace(' bags ','').split('contain ')
    dataClean.append(entry)

#Solution 1

def findParents(rules,target):
    parentConts = []
    for rule in rules:
        if target in rule[1]:
            parentConts.append(rule[0])
            parentConts += findParents(rules,rule[0])
                    
    return parentConts

target = 'shiny gold'

parentContainers = findParents(dataClean,target)
print(len(set(parentContainers)))


#Solution 2

def bagsInside(rules,bagType):
    containedBags = 0
    for rule in rules:
        if bagType in rule[0]:
            if 'no other bags' in rule[1]:
                return 0
            contents = rule[1].split(', ')
            for bag in contents:
                splitBag = bag.split(' ',1)
                numContained = int(splitBag[0])
                bagColor = splitBag[1].strip('bags').strip()
                containedBags += numContained*bagsInside(rules,bagColor) + numContained
    return containedBags

start = 'shiny gold'
print(bagsInside(dataClean,start))

