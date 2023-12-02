max = 0
current = 0 


values = []

f = open("test.txt", "r")
for x in f:
  first = ""
  last = ""
  for i in x:
    try:
      int(i)
      first = i
      break
    except ValueError:
      pass
  
  for j in reversed(x):
    try:
      int(j)
      last = j
      break
    except ValueError:
      pass
    
  value = first + last
  values.append(value)
  
print(values)

for x in values:
  current += int(x)
  
print(current)
  