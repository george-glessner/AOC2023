import re 
import math
from collections import Counter

max = 0
current = 0
sum = 0 

handBids = {}
handOrder = {}
handOrderMap = {}
handsSet = {}
handValues = {}  

def handKey(hand):
  return handsSet[hand]

f = open("input.txt", "r")

for line in f:
  splitLine = line.split()
  handBids[splitLine[0]] = int(splitLine[1])
  line = line.replace("A", "Z")
  line = line.replace("K", "Y")
  line = line.replace("Q", "X")
  line = line.replace("J", "W")
  splitLineReplaced = line.split()
  handOrderMap[splitLineReplaced[0]] = splitLine[0]
  handOrder[splitLineReplaced[0]] = Counter(sorted(splitLineReplaced[0])).most_common(5)

for hand in sorted(handOrder.items()):
  if len(hand[1]) == 1:
    # 5 king
    handsSet[hand[0]] = 7
  if len(hand[1]) == 2 and hand[1][0][1] == 4:
    # 4 kind
    handsSet[hand[0]] = 6
  if len(hand[1]) == 2 and hand[1][0][1] == 3:
    # full house
    handsSet[hand[0]] = 5
  if len(hand[1]) == 3 and hand[1][0][1] == 3:
    # 3 kind
    handsSet[hand[0]] = 4
  if len(hand[1]) == 3 and hand[1][0][1] == 2:
    # 2 kind
    handsSet[hand[0]] = 3
  if len(hand[1]) == 4:
    # 1 kind
    handsSet[hand[0]] = 2
  if len(hand[1]) == 5:
    # high
    handsSet[hand[0]] = 1

  
for index, hand in enumerate(sorted(handsSet, key=handKey), 1):
  sum+= index * handBids[handOrderMap[hand]]
  
print(sum)