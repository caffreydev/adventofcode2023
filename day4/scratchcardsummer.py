import re
file = open("input.txt", "r")
Lines = file.readlines()

sum = 0

def cardReader(card):
    winningString = card.split(" | ")[0].split(": ")[1]
    playersString = card.split(" | ")[1]
    winningNums = re.findall(r'\d+', winningString)
    playersNums = re.findall(r'\d+', playersString)
    return [winningNums, playersNums]

def cardSummer(card):
    winningNums = 0
    for num in card[1]:
        if num in card[0]:
            winningNums += 1
    return 0 if winningNums == 0 else 2 ** (winningNums - 1)
cards = []

for line in Lines:
    cards.append(cardReader(line))

for card in cards:
    sum += cardSummer(card)

print(sum)