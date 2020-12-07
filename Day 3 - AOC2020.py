#Read data
data = []

with open('inputs\input3.txt') as f:
    for line in f.readlines():
        data.append(line.strip())


#Solution 1
xPos = 0
yPos = 0
xStepSize = 3
yStepSize = 1

steps = len(data)
lineLen = len(data[0])

tree = 0

for i in range(steps):
    if data[yPos][xPos] == '#':
        tree+=1
    xPos += xStepSize
    xPos = xPos % lineLen
    yPos += yStepSize
    
print(tree)


#Solution 2
def calcTrees(data,xStepSize,yStepSize,xPos=0,yPos=0):
    tree = 0
    steps = len(data)
    lineLen = len(data[0])
    
    for i in range(steps):
        if yPos > steps:
            return tree
        if data[yPos][xPos] == '#':
            tree+=1
        xPos += xStepSize
        xPos = xPos % lineLen
        yPos += yStepSize
    return tree

#Run it
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
multHits = 1

for slope in slopes:
    multHits *= calcTrees(data,slope[0],slope[1])
    
print(multHits)

