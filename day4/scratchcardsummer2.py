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
    prizes = []
    for i in range(cardNumber + 1, cardNumber + 1 + wins):
        prizes.append(i)
    return [cardNumber, prizes]

cards = []
winners = {}

for line in Lines:
    card = cardReader(line)
    cards.append(card[0])
    winners.update({card[0]: card[1]})

lineMarker = 0

def cardProcessor(card):
    cards.extend( winners[card])

while lineMarker < len(cards):
    cardProcessor(cards[lineMarker])
    lineMarker += 1

print(lineMarker)