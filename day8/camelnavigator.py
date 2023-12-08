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

key = "AAA"
count = 0
directionsLength = len(leftRight)

while True:
    if key == "ZZZ":
        break
    node = nodes[key]
    index = count % directionsLength
    if count > directionsLength - 5 and count < directionsLength + 5:
        print(count)
        print(index)
        print("---")
    key = node[leftRight[index]]
    count += 1


print(count)
print(directionsLength)