import re
file = open("input.txt", "r")
Lines = file.readlines()

def cardReader(card):
    winningString = card.split(" | ")[0].split(": ")[1]
    playersString = card.split(" | ")[1]
    winningNums = re.findall(r'\d+', winningString)
    playersNums = re.findall(r'\d+', playersString)
    cardNumber = int(re.findall(r'\d+', card.split(":")[0])[0])
    wins = 0
    for num in playersNums:
        if num in winningNums:
            wins += 1
    return [cardNumber, wins]

cards = []

for line in Lines:
    cards.append(cardReader(line))

lineMarker = 0

def cardProcessor(card):
    cards.extend( cards[card[0] + 1: card[0] + card[1] + 1])

while lineMarker < len(cards):
    cardProcessor(cards[lineMarker])
    lineMarker += 1

print(lineMarker)