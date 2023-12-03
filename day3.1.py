import re 

max = 0
current = 0
sum = 0 

f = open("input.txt", "r").readlines()
lenLines = len(f)

def isMatch(number, numberIndex, currentLine):
  left = 0
  right = numberIndex + len(number)
  if(numberIndex-1>0):
    left = numberIndex-1

  if(re.search("([^0-9.])", f[currentLine][left].strip())):
    return True
  if(re.search("([^0-9.])", f[currentLine][right].strip())):
    return True
  if(currentLine < lenLines-1 and re.search("([^0-9.])", f[currentLine+1][left:right+1].strip())):
    return True
  if(currentLine > 0 and re.search("([^0-9.])", f[currentLine-1][left:right+1].strip())):
    return True
  return False
  
for x in f:
  numbers = re.findall("\d+", x.strip())
  searchIndex = -1
  for number in numbers:
    if current > lenLines:
      break
    try:
      loc = x.index(number, searchIndex+1)
    except ValueError:
      break
    else:
      searchIndex = loc+1
    if(isMatch(number, loc, current)):
      sum += int(number)
  current+=1
print(sum) 


