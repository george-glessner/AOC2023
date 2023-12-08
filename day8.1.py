import re 
import math

max = 0
current = 0
sum = 0 

f = open("input.txt", "r").read()

f = re.split("\n", f)
directions = list(f[0])
nodeMap = {}
for node in f[2::]:
  node = node.split(" = ")
  leftRight = re.findall("\w+", node[1])
  nodeMap[node[0]] = {"L": leftRight[0], "R": leftRight[1]}

current = "AAA"
count = 0

while not current == 'ZZZ':
  current = nodeMap.get(current)[directions[count % len(directions)]]
  count += 1
print(count)