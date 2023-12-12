import re

file = open('input.txt', 'r')
Lines = file.readlines()

emptyRows = []
emptyColumns = []

galaxyMap = []

for line in Lines:
    row = []
    for j in range(len(line) - 1):
        row.append(line[j])
    galaxyMap.append(row)

emptyRowCount = 0
for i in range(len(galaxyMap)):
    if all(position == '.' for position in galaxyMap[i]):
        emptyRows.append(i + emptyRowCount)
        emptyRowCount += 1

emptyColumnCount = 0
for i in range(len(galaxyMap[0])):
    galaxies = False
    for j in range(len(galaxyMap)):
        if galaxyMap[j][i] == "#":
            galaxies = True
            break
    if not galaxies:
        emptyColumns.append(i + emptyColumnCount)
        emptyColumnCount += 1

for emptyColumn in emptyColumns:
    for j in range (len(galaxyMap)):
        galaxyMap[j].insert(emptyColumn, '.')
print(len(galaxyMap))
for emptyRow in emptyRows:
    galaxyMap.insert(emptyRow+1, galaxyMap[emptyRow])

galaxies = []

for i in range(len(galaxyMap)):
    for j in range(len(galaxyMap[0])):
        if galaxyMap[i][j] == "#":
            galaxies.append([i,j])

sum = 0

def galaxyPairSummer (galaxy1, galaxy2):
    return abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
        sum += galaxyPairSummer(galaxies[i], galaxies[j])

print(sum)