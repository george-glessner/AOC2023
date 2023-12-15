import re 
import math

finalSum = 0
input = []

with open("input.txt", "r") as f:
  input = [line.rstrip().split(',') for line in f][0]

for entry in input:
  currentValue = 0
  for value in entry:
    currentValue += ord(value)
    currentValue = currentValue * 17
    currentValue = currentValue % 256
  finalSum += currentValue
  
print(finalSum)