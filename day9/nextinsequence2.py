import re

file = open("input.txt", "r")
Lines = file.readlines()

sum = 0
generatedValues = []

def nextSequence(currSequence):
    newSequence = []
    for i in range(len(currSequence) - 1):
        newSequence.append(currSequence[i + 1] - currSequence[i])
    return newSequence
def sequenceNextNum(currSequence, prevSequence):
    return currSequence[len(currSequence) - 1] + prevSequence[len(prevSequence) -1 ]

for line in Lines:
    sequence = list(map(int ,re.findall(r'-*\d+', line)))
    sequences = [sequence]
    while not all(num == 0 for num in sequence):
        sequence = nextSequence(sequence)
        sequences.append(sequence)
    depth = len(sequences) - 1
    sequences[depth].append(0)
    for i in range (depth - 1, -1, -1):
        sequences[i].append(sequenceNextNum(sequences[i], sequences[i + 1]))
    sum += sequences[0][len(sequences[0]) - 1]
    generatedValues.append(sequences[0][len(sequences[0]) - 1])

print(sum)