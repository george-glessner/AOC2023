import re 
import math

timeDistance = {}
winnings = []

f = open("input.txt", "r")

lines = f.readlines()
times = lines[0].strip().split(":")[1].split()
distances = lines[1].strip().split(":")[1].split()

for index, time in enumerate(times):
    timeDistance[int(time)] = int(distances[index])

for entry in timeDistance:
    winningWays = 0
    for i in range(0,entry):
        if i * (entry-i) > timeDistance[entry]:
            winningWays+=1
    winnings.append(winningWays)

print(math.prod(winnings))