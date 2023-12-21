file = open('input.txt', 'r')
Lines = file.readlines()

summary = 0
patterns = []
pattern = []

for line in Lines:
    if line == "\n":
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append(line[0:len(line) - 1])
scores = []
def patternPointsRows(pattern):
    maximum = 0
    for i in range (len(pattern) - 1):
        if pattern[i] != pattern[i + 1]:
            continue
        if len(pattern)/2 >= i + 1:
            mirror = True
            for j in range (i):
                if (pattern[i - 1 - j] != pattern[i + j + 1]):
                    mirror = False
                    break
            if mirror:
                maximum = max(maximum, i + 1)
        else:
            mirror = True
            for j in range (len(pattern) - i - 2):
                if (pattern[i - 1 - j] != pattern[i + j + 2]):
                    mirror = False
                    break
            if mirror:
                maximum = max(maximum, i + 1)
    return maximum
            
def patternPointsCols(pattern):
    cols = []
    maximum = 0
    for i in range(len(pattern[0])):
        col = []
        for j in range(len(pattern)):
            col.append(pattern[j][i])
        cols.append(col)
        for i in range (len(cols) - 1):
            if cols[i] != cols[i + 1]:
                continue
            if len(cols)/2 >= i + 1:
                mirror = True
                for j in range (i):
                    if (cols[i - 1 - j] != cols[i + j + 1]):
                        mirror = False
                        break
                if mirror:
                    maximum = max(maximum, i + 1)
            else:
                mirror = True
                for j in range (len(cols) - i - 2):
                    if (cols[i - 1 - j] != cols[i + j + 2]):
                        mirror = False
                        break
                if mirror:
                    maximum = max(i + 1, maximum)
    
    return maximum
    
colScores = []

for pattern in patterns:
    summary += 100 * patternPointsRows(pattern) + patternPointsCols(pattern)
    scores.append(patternPointsRows(pattern))
    colScores.append(patternPointsCols(pattern))

print(summary)