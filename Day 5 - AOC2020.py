#Open file and store data
data = []

with open('inputs\input5.txt') as f:
    data = f.readlines()
    data = [line.strip() for line in data]

#Define Functions
import math

def lowerCalc(curRange):
    return (math.ceil((curRange[1]-curRange[0])/2)+curRange[0],curRange[1])

def upperCalc(curRange):
    return (curRange[0],((curRange[1]-curRange[0])//2)+curRange[0])

def solveProb(fbChars,curRange,lowerChars=["F","L"],upperChars=["B","R"]):
    for char in fbChars:
        if char in lowerChars: 
            curRange = upperCalc(curRange)
        elif char in upperChars: 
            curRange = lowerCalc(curRange)
    return(curRange[0])

def calcSeatID(row,col):
    return (row*8)+col

#Solution 1
seatIDs = []

for line in data:
    row = solveProb(line[0:7],(0,127))
    col = solveProb(line[7:],(0,7))
    seatID = calcSeatID(row,col)
    seatIDs.append(seatID)
    
print(max(seatIDs))

#Solution 2
seatIDs = []

for line in data:
    row = solveProb(line[0:7],(0,127))
    col = solveProb(line[7:],(0,7))
    seatID = calcSeatID(row,col)
    seatIDs.append(seatID)
    
seatIDs.sort()
for i in range(len(seatIDs)-1):
    if seatIDs[i]+1 != seatIDs[i+1]:
        print(seatIDs[i],seatIDs[i+1]) #sanity check print statement
        print("Solution: " + str(seatIDs[i]+1))

