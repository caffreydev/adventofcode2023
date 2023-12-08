import math

file = open("input.txt", "r")
Lines = file.readlines()

leftRight = Lines[0].split("\n")[0]

nodes = {}

for i in range(1, len(Lines)):
    line = Lines[i]
    key = line.split(" = ")[0]
    left = line.split("(")[1].split(",")[0]
    right = line.split(", ")[1].split(")")[0]
    nodes.update({key: {"L": left, "R": right}})

keys = [key for key in nodes.keys() if key[2] == "A"]
directionsLength = len(leftRight)

repeatLengths = []

for i in range(len(keys)):
    count = 0
    key = keys[i]
    while True:
        if key[2] == "Z":
            repeatLengths.append(count)
            break
        node = nodes[key]
        index = count % directionsLength
        key = node[leftRight[index]]
        count += 1

print(math.lcm(*repeatLengths ))

