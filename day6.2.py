import re 
import math

winningWays = 0

f = open("input.txt", "r")

lines = f.readlines()
time = int(lines[0].strip().split(":")[1].replace(" ", ""))
distance = int(lines[1].strip().split(":")[1].replace(" ", ""))

for i in range(0,time):
    if i * (time-i) > distance:
        winningWays+=1

print(winningWays)