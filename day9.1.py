import re 
import math

max = 0
current = 0
sequences = []
missingSum = 0


f = open("input.txt", "r")


def findDifferences(sequence):
  count = 0
  currentSequence = []
  currentSequence.append(sequence)
  zeroDiffFound = False
  while not zeroDiffFound:
    currentSequence.append(list(currentSequence[count][i+1]-currentSequence[count][i] for i in range(0, len(currentSequence[count])-1)))
    count += 1
    zeroDiffFound = sum(abs(x) for x in currentSequence[-1]) == 0
  return currentSequence

def findMissingValue(sequence):
  missingValue = 0
  for i, _ in enumerate(sequence, start=1):
    try:
      missingValue = sequence[-i][-1] + sequence[-i-1][-1]
      sequence[-i-1][-1] = missingValue
    except:
      pass
  return missingValue

for x in f:
  sequences.append(list(int(x) for x in x.split()))
  
for sequence in sequences:
  currentSequence = findDifferences(sequence)
  missingValues = findMissingValue(currentSequence)
  missingSum += missingValues
  
print(missingSum)