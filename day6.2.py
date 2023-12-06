import re 
import math

f = open("input.txt", "r")
lines = f.readlines()
time = int(lines[0].strip().split(":")[1].replace(" ", ""))
distance = int(lines[1].strip().split(":")[1].replace(" ", ""))

for i in range(0,time):
    if i * (time-i) > distance:
        print(time+1 - i*2)
        break