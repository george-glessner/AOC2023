import re 
import math

timeDistance = {}
totalWinnings = 1

f = open("test.txt", "r")

lines = f.readlines()
times = lines[0].strip().split(":")[1].split()
distances = lines[1].strip().split(":")[1].split()

for index, time in enumerate(times):
    timeDistance[int(time)] = int(distances[index])

for entry in timeDistance:
    for i in range(0,entry):
        if i * (entry-i) > timeDistance[entry]:
            totalWinnings *= entry+1 - i*2
            break
print(totalWinnings)
