#Open file and load data
data = []

with open('inputs\input8.txt') as f:
    data = f.readlines()

instructions = []    
    
#Clean up data
for entry in data:
    instructions.append(entry.strip().split(' '))

#Solution 1
indexesRun = []
run = True
instIndex = 0
accCount = 0

while run:
    executed = False
    if instructions[instIndex][0] == 'nop':
        indexesRun.append(instIndex)
        executed = True
        instIndex += 1
    if instructions[instIndex][0] == 'acc' and (not executed):
        indexesRun.append(instIndex)
        accCount += int(instructions[instIndex][1].strip('+'))
        executed = True
        instIndex += 1
    if instructions[instIndex][0] == 'jmp' and (not executed):
        indexesRun.append(instIndex)
        executed = True
        instIndex += int(instructions[instIndex][1].strip('+'))
    if instIndex in indexesRun: 
        run = False
    
print(accCount)

