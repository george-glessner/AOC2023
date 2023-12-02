max = 0
current = 0 
values = []
digit_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

f = open("input.txt", "r")

for x in f:
  first = ""
  last = ""
  firstdigit = ""
  lastdigit = ""
  firstdigitindex = 0
  lastdigitindex = 0
  for i in x:
    min = 100000
    for d in digits:
      if d in x:
        firstdigitindex = x.index(d)
        if firstdigitindex < min:
          min = firstdigitindex
          firstdigit = str(digit_map.get(d))

    try:
      int(i)
      if x.index(i) <= int(min):
        first = i
      else:
        first = firstdigit
      break
    except ValueError:
      first = firstdigit
      pass
  
  for j in reversed(x):
    max = 0
    for d in digits:
      if d in x:
        lastdigitindex = x.rindex(d)
        if lastdigitindex > max:
          max = lastdigitindex
          lastdigit = str(digit_map.get(d))

    try:
      int(j)
      if x.rindex(j) >= int(max):
        last = j
      else:
        last = lastdigit
      break
    except ValueError:
      last = lastdigit
      pass
  value = first + last
  values.append(value)
    
for x in values:
  current += int(x)
  
print(current)
  