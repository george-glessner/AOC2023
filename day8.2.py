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

startNodes = list(node for node in nodeMap if node.endswith("A")) 
numSteps = []

for node in startNodes:
  steps = 0
  while not node.endswith("Z"):
      node = nodeMap.get(node)[directions[steps % len(directions)]]
      steps += 1
  numSteps.append(steps)
print(math.lcm(*numSteps))