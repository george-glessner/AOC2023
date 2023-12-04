import re 
import math

max = 0
current = 0
currentSum = 0
resultSum = 0 
rollingTotal = 0
results = []

f = open("input.txt", "r").readlines()
lenLines = len(f)

def checkMatch(numbers, gearIndex, line):
  searchIndex = -1
  global results
  for number in numbers:
    try:
      loc = line.index(number, searchIndex+1)
    except ValueError:
      break
    else:
      searchIndex = loc+1
    if(loc == gearIndex):
      results.append(int(number))
      continue
    if(loc == gearIndex + 1):
      results.append(int(number))
      continue
    if(loc == gearIndex - 1):
      results.append(int(number))
      continue
    if(loc < gearIndex and loc + len(number) >= gearIndex):
      results.append(int(number))
      continue
  return len(results) == 2
  
def isMatch(gear, gearIndex, currentLine):
  global rollingTotal
  global results
  numMatches=0

  if(re.search("\d+", f[currentLine].strip())):
    if(checkMatch(re.findall("\d+", f[currentLine].strip()), gearIndex, f[currentLine])):
      numMatches+=1
  if(currentLine < lenLines-1 and re.search("\d+", f[currentLine+1].strip())):
    if(checkMatch(re.findall("\d+", f[currentLine+1].strip()), gearIndex, f[currentLine+1])):
      numMatches+=1
  if(currentLine > 0 and re.search("\d+", f[currentLine-1].strip())):
    if(checkMatch(re.findall("\d+", f[currentLine-1].strip()), gearIndex, f[currentLine-1])):
      numMatches+=1
  
  if(len(results)==2):
    rollingTotal += math.prod(results)
    numMatches = 0
  results = []
  return False
  
for x in f:
  gears = re.findall("\*", x.strip())
  searchIndex = -1
  for gear in gears:
    if current > lenLines:
      break
    try:
      loc = x.index(gear, searchIndex+1)
    except ValueError:
      break
    else:
      searchIndex = loc+1
    isMatch(gear, loc, current)
  current+=1
print(rollingTotal) 


