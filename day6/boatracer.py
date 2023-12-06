import re
file = open("input.txt", "r")
Lines = file.readlines()

times = list(map(int, re.findall(r'\d+', Lines[0])))
records = list(map(int,re.findall(r'\d+', Lines[1])))

def optionsFinder (raceNum):
    options = 0
    record = records[raceNum]
    time = times[raceNum]
    for i in range(1, time):
        if i * (time - i) > record:
            options += 1
    return options

product = 1

for i in range(len(times)):
    product *= optionsFinder(i)

print(product)