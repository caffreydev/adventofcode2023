file = open('input.txt', 'r')
Lines = file.readlines()
sum = 0

for line in Lines:
    firstDigit = 0
    lastDigit = 0
    for i in range (len(line)):
        if (line[i].isdecimal()):
            firstDigit = int(line[i])
            break
    for i in reversed(range (len(line))):
        if (line[i].isdecimal()):
            lastDigit = int(line[i])
            break
    sum += firstDigit * 10 + lastDigit

print(sum)
         
    
        

