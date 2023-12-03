import re

file = open("input.txt", 'r')
Lines = file.readlines()

i = 0
stars = []
length = len(Lines[0])

for line in Lines:    
    for j in range(length - 1):
        if line[j] == "*":
            stars.append([i,j])      
    i += 1

sum = 0

def gearChecker (i, j):
    nums = 0
    if re.match(r'[0-9]', Lines[i - 1][j - 1]) and re.match(r'[0-9]', Lines[i - 1][j + 1]) and Lines[i - 1][j] == ".":
        nums += 2
    elif re.match(r'[0-9]', Lines[i - 1][j - 1]) or re.match(r'[0-9]', Lines[i - 1][j]) or re.match(r'[0-9]', Lines[i - 1][j + 1]):
        nums += 1
    if re.match(r'[0-9]', Lines[i + 1][j - 1]) and re.match(r'[0-9]', Lines[i + 1][j + 1]) and Lines[i + 1][j] == ".":
        nums += 2
    elif re.match(r'[0-9]', Lines[i + 1][j - 1]) or re.match(r'[0-9]', Lines[i + 1][j]) or re.match(r'[0-9]', Lines[i + 1][j + 1]):
        nums += 1
    if re.match(r'[0-9]', Lines[i][j - 1]):
        nums += 1
    if re.match(r'[0-9]', Lines[i][j + 1]):
        nums += 1
    
    if nums == 2:
        return True
    return False

def gearCalculator (i , j):
    num1 = -1
    if re.match(r'[0-9]',Lines[i][j + 1]):
        k = j + 2
        while k < length and re.match(r'[0-9]', Lines[i][k]):
            k += 1
        if num1 < 0:
            num1 = int(Lines[i][j + 1:k])
        else:
            return num1 * int(Lines[i][j + 1:k])
    if re.match(r'[0-9]',Lines[i][j - 1]):
        k = j - 2
        while k > -1 and re.match(r'[0-9]', Lines[i][k]):
            k -= 1
        if num1 < 0:
            num1 = int(Lines[i][k+1:j])
        else:
            return num1 * int(Lines[i][k + 1: j])
    
    if not re.match(r'[0-9]', Lines[i - 1][j - 1]) and not re.match(r'[0-9]', Lines[i - 1][j]) and re.match(r'[0-9]', Lines[i - 1][j + 1]):
        k = j + 2
        while k < length and re.match(r'[0-9]', Lines[i - 1][k]):
            k += 1
        if num1 < 0:
            num1 = int(Lines[i - 1][j + 1:k])
        else:
            return num1 * int(Lines[i - 1][j + 1:k])
    elif not re.match(r'[0-9]', Lines[i - 1][j - 1]) and re.match(r'[0-9]', Lines[i - 1][j]) and not re.match(r'[0-9]', Lines[i - 1][j + 1]):
        if num1 < 0:
            num1 = int(Lines[i - 1][j])
        else:
            return num1 * int(Lines[i - 1][j])
    elif re.match(r'[0-9]', Lines[i - 1][j - 1]) and not re.match(r'[0-9]', Lines[i - 1][j]) and not re.match(r'[0-9]', Lines[i - 1][j + 1]):
        k = j - 2
        while k > -1 and re.match(r'[0-9]', Lines[i - 1][k]):
            k -= 1
        if num1 < 0:
            num1 = int(Lines[i - 1][k + 1:j])
        else:
            return num1 * int(Lines[i - 1][k + 1:j])
    elif not re.match(r'[0-9]', Lines[i - 1][j - 1]) and re.match(r'[0-9]', Lines[i - 1][j]) and re.match(r'[0-9]', Lines[i - 1][j + 1]):
        k = j + 2
        while k < length and re.match(r'[0-9]', Lines[i - 1][k]):
            k += 1
        if num1 < 0:
            num1 = int(Lines[i - 1][j:k])
        else:
            return num1 * int(Lines[i - 1][j:k])
    elif re.match(r'[0-9]', Lines[i - 1][j - 1]) and re.match(r'[0-9]', Lines[i - 1][j]) and not re.match(r'[0-9]', Lines[i - 1][j + 1]):
        k = j - 2
        while k > -1 and re.match(r'[0-9]', Lines[i - 1][k]):
            k -= 1
        if num1 < 0:
            num1 = int(Lines[i - 1][k + 1:j + 1])
        else:
            return num1 * int(Lines[i - 1][k + 1:j + 1])
    elif re.match(r'[0-9]', Lines[i - 1][j - 1]) and not re.match(r'[0-9]', Lines[i - 1][j]) and re.match(r'[0-9]', Lines[i - 1][j + 1]):
        k = j + 2
        while k < length and re.match(r'[0-9]', Lines[i - 1][k]):
            k += 1
        l = j - 2
        while l > -1 and re.match(r'[0-9]', Lines[i - 1][l]):
            l -= 1
        return int(Lines[i - 1][j + 1:k]) * int(Lines[i - 1][l + 1:j])
    elif re.match(r'[0-9]', Lines[i - 1][j - 1]) and re.match(r'[0-9]', Lines[i - 1][j]) and re.match(r'[0-9]', Lines[i - 1][j + 1]):
        k = j + 2
        while k < length and re.match(r'[0-9]', Lines[i - 1][k]):
            k += 1
        l = j - 2
        while l > -1 and re.match(r'[0-9]', Lines[i - 1][l]):
            l -= 1
        if num1 < 0:
            num1 = int(Lines[i - 1][l + 1: k])
        else:
            return num1 * int(Lines[i - 1][l + 1: k])
    if not re.match(r'[0-9]', Lines[i + 1][j - 1]) and not re.match(r'[0-9]', Lines[i + 1][j]) and re.match(r'[0-9]', Lines[i + 1][j + 1]):
        k = j + 2
        while k < length and re.match(r'[0-9]', Lines[i + 1][k]):
            k += 1
        if num1 < 0:
            num1 = int(Lines[i + 1][j + 1:k])
        else:
            return num1 * int(Lines[i + 1][j + 1:k])
    elif not re.match(r'[0-9]', Lines[i + 1][j - 1]) and re.match(r'[0-9]', Lines[i + 1][j]) and not re.match(r'[0-9]', Lines[i + 1][j + 1]):
        if num1 < 0:
            num1 = int(Lines[i + 1][j])
        else:
            return num1 * int(Lines[i + 1][j])
    elif re.match(r'[0-9]', Lines[i + 1][j - 1]) and not re.match(r'[0-9]', Lines[i + 1][j]) and not re.match(r'[0-9]', Lines[i + 1][j + 1]):
        k = j - 2
        while k > -1 and re.match(r'[0-9]', Lines[i + 1][k]):
            k -= 1
        if num1 < 0:
            num1 = int(Lines[i + 1][k + 1:j])
        else:
            return num1 * int(Lines[i + 1][k + 1:j])
    elif not re.match(r'[0-9]', Lines[i + 1][j - 1]) and re.match(r'[0-9]', Lines[i + 1][j]) and re.match(r'[0-9]', Lines[i + 1][j + 1]):
        k = j + 2
        while k < length and re.match(r'[0-9]', Lines[i + 1][k]):
            k += 1
        if num1 < 0:
            num1 = int(Lines[i + 1][j:k])
        else:
            return num1 * int(Lines[i + 1][j:k])
    elif re.match(r'[0-9]', Lines[i + 1][j - 1]) and re.match(r'[0-9]', Lines[i + 1][j]) and not re.match(r'[0-9]', Lines[i + 1][j + 1]):
        k = j - 2
        while k > -1 and re.match(r'[0-9]', Lines[i + 1][k]):
            k -= 1
        if num1 < 0:
            num1 = int(Lines[i + 1][k + 1:j + 1])
        else:
            return num1 * int(Lines[i + 1][k + 1:j + 1])
    elif re.match(r'[0-9]', Lines[i + 1][j - 1]) and not re.match(r'[0-9]', Lines[i + 1][j]) and re.match(r'[0-9]', Lines[i + 1][j + 1]):
        k = j + 2
        while k < length and re.match(r'[0-9]', Lines[i + 1][k]):
            k += 1
        l = j - 2
        while l > -1 and re.match(r'[0-9]', Lines[i + 1][l]):
            l -= 1
        return int(Lines[i + 1][j + 1:k]) * int(Lines[i + 1][l + 1:j])
    elif re.match(r'[0-9]', Lines[i + 1][j - 1]) and re.match(r'[0-9]', Lines[i + 1][j]) and re.match(r'[0-9]', Lines[i + 1][j + 1]):
        k = j + 2
        while k < length and re.match(r'[0-9]', Lines[i + 1][k]):
            k += 1
        l = j - 2
        while l > -1 and re.match(r'[0-9]', Lines[i + 1][l]):
            l -= 1
        if num1 < 0:
            num1 = int(Lines[i + 1][l + 1: k])
        else:
            return num1 * int(Lines[i + 1][l + 1: k])

for star in stars:
    if gearChecker(star[0], star[1]):
        sum += gearCalculator(star[0], star[1])

print(sum)   
