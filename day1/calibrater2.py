file = open('input.txt', 'r')
Lines = file.readlines()
sum = 0


digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


for line in Lines:
    firstDigit = 0
    lastDigit = 0
    for i in range (len(line)):
        if (line[i].isdecimal()):
            firstDigit = int(line[i])
            break
        else:
            for j in range (i + 1):
                if line[j:i + 1] in digits:
                    firstDigit = digits.index(line[j:i + 1]) + 1
                    break
        if firstDigit > 0: break
                
    for i in reversed(range (len(line))):
        if (line[i].isdecimal()):
            lastDigit = int(line[i])
            break
        else:
            for j in reversed(range (i, len(line))):
                if line[i:j + 1] in digits:
                    lastDigit = digits.index(line[i:j + 1]) + 1
                    break
            if lastDigit > 0: break
    sum += firstDigit * 10 + lastDigit

print(sum)
         
    
        

