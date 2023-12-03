import re

file = open("input.txt", 'r')
Lines = file.readlines()


i = 0
numbers = []
length = len(Lines[0])

#run through and find all the numbers - record in a list with vector start point and the number, and length
for line in Lines:    
    for j in range(length - 1):
        if line[j] == ".":
            continue
        elif re.match(r'[0-9]', line[j]):
            if j > 0 and re.match(r'[0-9]', line[j-1]):
                continue
            k = j + 1
            while k < length and re.match(r'[0-9]', line[k]):
                k += 1
            numbers.append([[i,j], line[j:k]])      
    i += 1

sum = 0

def symbolChecker (i, j):
    if not re.match(r'[0-9]', Lines[i][j]) and not Lines[i][j] == "." and not Lines[i][j] == " " and not Lines[i][j] == "\n":
        return True
    return False
    
def numberChecker (num):
    if num[0][1] != 0 and symbolChecker(num[0][0], num[0][1] - 1):
        return int(num[1])
    elif num[0][1] + len(num[1]) != length and symbolChecker(num[0][0], num[0][1] + len(num[1])):
        return int(num[1])
    if num[0][0] != 0:
        for j in range (num[0][1] - 1, num[0][1] + len(num[1]) + 1):
            if j != -1 and j != length and symbolChecker(num[0][0] - 1, j):
                return int(num[1])
    if num[0][0] != len(Lines) - 1:
        for j in range (num[0][1] - 1, num[0][1] + len(num[1]) + 1):
            if j != -1 and j != length and symbolChecker(num[0][0] + 1, j):
                return int(num[1])
                
    return 0
    

for number in numbers:
    sum += numberChecker(number)
   
print(sum)   