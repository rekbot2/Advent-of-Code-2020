#Open file and store data
data = []

with open('inputs\input5.txt') as f:
    data = f.readlines()
    data = [line.strip() for line in data]

#Define Functions with Binary Conversions
def splitRowCol(boardingPass):
    return(boardingPass[0:7],boardingPass[7:])

def convToBinary(inputStr,convToZero=["F","L"],convToOne=["B","R"]):
    inputStr = list(inputStr)
    for charIndex in range(len(inputStr)):
        if inputStr[charIndex] in convToZero:
            inputStr[charIndex] = "0"
        elif inputStr[charIndex] in convToOne:
            inputStr[charIndex] = "1"
    return "".join(inputStr)

def getRowCol(boardingPass):
    rowStr,colStr = splitRowCol(boardingPass)
    rowBinary = convToBinary(rowStr)
    colBinary = convToBinary(colStr)
    row = int(rowBinary,2)
    col = int(colBinary,2) 
    return row,col

def calcSeatID(row,col):
    return (row*8)+col


#Solution 1 with Binary conversions
seatIDs = []

for boardingPass in data:
    row,col = getRowCol(boardingPass)
    seatIDs.append(calcSeatID(row,col))
    
print(max(seatIDs))

#Solution 2 with Binary conversions
seatIDs = []

for boardingPass in data:
    row,col = getRowCol(boardingPass)
    seatIDs.append(calcSeatID(row,col))
    
seatIDs.sort()
for i in range(len(seatIDs)-1):
    if seatIDs[i]+1 != seatIDs[i+1]:
        print(seatIDs[i],seatIDs[i+1]) #sanity check print statement
        print("Solution: " + str(seatIDs[i]+1))

