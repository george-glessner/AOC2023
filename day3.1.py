import re 

max = 0
current = 0
sum = 0 

f = open("input.txt", "r").readlines()
lenLines = len(f)

def isMatch(number, numberIndex, currentLine):
  # next to left, next to right, above, below, above diag right, above diag left, below diag left below diag right
  if(numberIndex > 0 and re.search("([^0-9.])", f[currentLine][numberIndex-1])):
    # right
    return True
  if(numberIndex < len(f[currentLine]) and re.search("([^0-9.])", f[currentLine][numberIndex + len(number)])):
    # left
    return True
  if(currentLine < lenLines-1 and re.search("([^0-9.])", f[currentLine+1][numberIndex:numberIndex + len(number)])):
    # below
    return True
  if(currentLine < lenLines-1 and re.search("([^0-9.])", f[currentLine+1][numberIndex + len(number)])):
    # below right
    return True
  if(currentLine < lenLines-1 and re.search("([^0-9.])", f[currentLine+1][numberIndex - 1])):
    # below left
    return True
  if(currentLine > 0 and re.search("([^0-9.])", f[currentLine-1][numberIndex:numberIndex + len(number)])):
    # above
    return True
  if(currentLine > 0 and re.search("([^0-9.])", f[currentLine-1][numberIndex - 1])):
    # above left
    return True
  if(currentLine > 0 and re.search("([^0-9.])", f[currentLine-1][numberIndex + len(number)])):
    # above right
    return True
  return False
  
for x in f:
  numbers = re.findall("\d+", x.strip())
  for number in numbers:
    if current > lenLines:
      break
    if(isMatch(number, x.index(number), current)):
      sum += int(number)
  current+=1
print(sum)


