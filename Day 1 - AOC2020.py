#Read data
inputList = []

with open('inputs\input1.txt') as f:
    for line in f.readlines():
        inputList.append(int(line.strip()))


#Define functions
import itertools
import numpy as np

def solveProblem(inputList,n):
    allCombos = list(itertools.combinations(inputList,n))
    
    for i in allCombos:
        combination = list(i)
        if sum(combination) == 2020:
            out = np.prod(combination)
            
    return out

#Solution 1
print(solveProblem(inputList,2))

#Solution 2
print(solveProblem(inputList,3))

