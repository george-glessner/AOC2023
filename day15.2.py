import re 
import math

finalSum = 0
input = []
boxMap = {}

with open("input.txt", "r") as f:
  input = [line.rstrip().split(',') for line in f][0]

def getHashValue(code):
  currentValue=0
  for value in code:
    currentValue += ord(value)
    currentValue = currentValue * 17
    currentValue = currentValue % 256
  return int(currentValue)

for entry in input:
  if "=" in entry:
    label = entry.split("=")
    boxPosition = getHashValue(label[0])
    labelKey = label[0] + " " + label[1]
    if boxPosition in boxMap:
      for index, oldKey in enumerate(boxMap[boxPosition]):
        if label[0] in oldKey:
          boxMap[boxPosition][index] = labelKey
          break
      else:
        boxMap[boxPosition].append(labelKey)
    else:
      boxMap[boxPosition] = [labelKey]
  else:
    label = entry.split("-")
    boxPosition = getHashValue(label[0])
    if boxPosition in boxMap:
      for index, oldKey in enumerate(boxMap[boxPosition]):
        if label[0] in oldKey:
          boxMap[boxPosition].remove(boxMap[boxPosition][index])
          break
  
for box, x in enumerate(boxMap):
  for y, z in enumerate(boxMap[x],1):
    finalSum += ((x + 1) * y) * int(z.split(' ')[1])
    
print(finalSum)