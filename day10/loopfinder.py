# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

file = open("input.txt", "r")
Lines = file.readlines()

startPosition = [-1, -1]

for i in range(len(Lines)):
    for j in range(len(Lines[0])):
        if Lines[i][j] == "S":
            startPosition[0] = i
            startPosition[1] = j
            break
    if startPosition[0] != -1:
        break
    
def move(cursor):
    if Lines[cursor[0]][cursor[1]] == '|':
        if cursor[2] == 'S':
            if cursor[0] == 0:
                return [-1, -1, -1]
            return [cursor[0] - 1, cursor[1], 'S']
        elif cursor[2] == 'N':
            if cursor[0] == len(Lines) - 1:
                return [-1, -1, -1]
            return [cursor[0] + 1, cursor[1], 'N']
    if Lines[cursor[0]][cursor[1]] == '-':
        if cursor[2] == 'W':
            if cursor[1] == len(Lines[0]) - 1:
                return [-1, -1, -1]
            return [cursor[0], cursor[1] + 1, 'W']
        elif cursor[2] == 'E':
            if cursor[1] == 0:
                return [-1, -1, -1]
            return [cursor[0], cursor[1] - 1, 'E']
    if Lines[cursor[0]][cursor[1]] == 'L':
        if cursor[2] == 'N':
            if cursor[1] == len(Lines[0]) - 1:
                return [-1, -1, -1]
            return [cursor[0], cursor[1] + 1, 'W']
        elif cursor[2] == 'E':
            if cursor[0] == 0:
                return [-1, -1, -1]
            return [cursor[0] - 1, cursor[1], 'S']
    if Lines[cursor[0]][cursor[1]] == 'J':
        if cursor[2] == 'N':
            if cursor[1] == 0:
                return [-1, -1, -1]
            return [cursor[0], cursor[1] - 1, 'E']
        elif cursor[2] == 'W':
            if cursor[0] == 0:
                return [-1, -1, -1]
            return [cursor[0] - 1, cursor[1], 'S']
    if Lines[cursor[0]][cursor[1]] == '7':
        if cursor[2] == 'S':
            if cursor[1] == 0:
                return [-1, -1, -1]
            return [cursor[0], cursor[1] - 1, 'E']
        elif cursor[2] == 'W':
            if cursor[0] == len(Lines) - 1:
                return [-1, -1, -1]
            return [cursor[0] + 1, cursor[1], 'N']
    if Lines[cursor[0]][cursor[1]] == 'F':
        if cursor[2] == 'S':
            if cursor[1] == len(Lines[0]) - 1:
                return [-1, -1, -1]
            return [cursor[0], cursor[1] + 1, 'W']
        elif cursor[2] == 'E':
            if cursor[0] == len(Lines) - 1:
                return [-1, -1, -1]
            return [cursor[0] + 1, cursor[1], 'N']
    return [-1, -1, -1]
         
nextUp = [[startPosition[0] -1, startPosition[1], 'S'], [startPosition[0] + 1, startPosition[1], 'N'], [startPosition[0], startPosition[1] + 1, 'W'], [startPosition[0], startPosition[1] - 1, 'E'],]

loopSize = 0


for next in nextUp:
    count = 0
    cursor = [next[0], next[1], next[2]]
    
    while not (cursor[0] == startPosition[0] and cursor[1] == startPosition[1]) and not (cursor[0] == -1 and cursor[1] == -1):
        count += 1
        cursor = move(cursor)
    if cursor[0] == -1:
        continue
    loopSize = (count + 1) / 2
    break
    
print(loopSize)