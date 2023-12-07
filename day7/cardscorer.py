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

def handSorter (hand1, hand2):
    #to do
    return 1

# hands.sort(handSorter, True)

def handCategoriser (hand):
    cards = hand[0]
    matching = {}
    for card in cards:
        if not card in matching.keys():
            matching.update({card: 1})
        else: matching.update({card: matching[card] + 1})
    values = matching.values()
    numPairs = 0
    for value in values:
        if value == 2:
            numPairs += 1
    
    if 5 in values:
        fives.append(hand)
    elif 4 in values:
        fours.append(hand)
    elif 3 in values and 2 in values:
        fullhouses.append(hand)
    elif 3 in values:
        threes.append(hand)
    elif numPairs == 2:
        twoPairs.append(hand)
    elif 2 in values:
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