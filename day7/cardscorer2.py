file = open("input.txt", "r")
Lines = file.readlines()

hands = []

for line in Lines:
    hands.append(
        [line.split(" ")[0], int( line.split(" ")[1])]
    )

fives = []
fours = []
fullhouses = []
threes = []
twoPairs = []
pairs = []
highCards = []


def faceCardMapper(card):
    if card == "T":
        return 10
    elif card == "J":
        return 1
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A": 
        return 14
    else:
        return int(card)
    
def handSorter (hand):
    keyVal = 0
    for i in range(len(hand[0])):
        keyVal += faceCardMapper(hand[0][i]) * 15 ** 4 / 15 ** i
    return keyVal

hands = sorted(hands, key=handSorter)

def handCategoriser (hand):
    cards = hand[0]
    matching = {}
    numJacks = 0
    for card in cards:
        if not card in matching.keys() and card != "J":
            matching.update({card: 1})
        elif card == "J":
            numJacks += 1
        else: matching.update({card: matching[card] + 1})
    values = matching.values()
    numPairs = 0
    for value in values:
        if value == 2:
            numPairs += 1

    
    if 5 in values or numJacks == 5 or max(values) + numJacks == 5:
        fives.append(hand)
    elif 4 in values or max(values) + numJacks == 4:
        fours.append(hand)
    elif 3 in values and 2 in values or (numPairs == 2 and numJacks == 1) or (numPairs == 1 and numJacks >= 2):
        fullhouses.append(hand)
    elif 3 in values or max(values) + numJacks == 3:
        threes.append(hand)
    elif numPairs == 2:
        twoPairs.append(hand)
    elif 2 in values or numJacks == 1:
        pairs.append(hand)
    else: highCards.append(hand)

for hand in hands:
    handCategoriser(hand)

sum = 0
i = 1

for highCard in highCards:
    sum += i * highCard[1]
    i += 1
for pair in pairs:
    sum += i * pair[1]
    i += 1
for twoPair in twoPairs:
    sum += i * twoPair[1]
    i += 1
for three in threes:
    sum += i * three[1]
    i += 1
for fullhouse in fullhouses:
    sum += i * fullhouse[1]
    i += 1
for four in fours:
    sum += i * four[1]
    i += 1
for five in fives:
    sum += i * five[1]
    i += 1

print(sum)