file = open("input.txt", "r")
Lines = file.readlines()
sum = 0

def checker (line, redNum, greenNum ,blueNum):
    id = int(line.split(":")[0].split(" ")[1])
    reveals = (line).split(": ")[1].split("; ")
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    for reveal in reveals:
        reds = 0
        greens = 0
        blues = 0
        colorCounts = reveal.split(", ")
        for colorCount in colorCounts:
            if "red" in colorCount:
                reds += int(colorCount.split(" red")[0])
            elif "green" in colorCount:
                greens += int(colorCount.split(" green")[0]) 
            else:
                blues += int(colorCount.split(" blue")[0]) 
        maxRed = max(reds, maxRed)
        maxGreen = max(greens, maxGreen)
        maxBlue = max(blues, maxBlue)   
    
    if maxRed <= redNum and maxGreen <= greenNum and maxBlue <= blueNum: return id
    return 0

for line in Lines:
    sum += checker(line, 12, 13, 14)
print(sum)