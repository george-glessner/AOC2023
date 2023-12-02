import re

sum = 0
current = 0 
error = False

possible = {"red": 12, "green": 13, "blue": 14}
colors = ["red", "green", "blue"]

f = open("input.txt", "r")
for x in f:
  error = False
  x = x.strip()
  current += 1
  curr = re.split("Game \d+:", x)
  games = curr[1].split(";")
  for game in games:
    if(error):
      break
    grabbed = re.split("\w ,", game)
    grabbed = grabbed[0].split(",")
    for pulled in grabbed:
      hand = re.split("\s", pulled.strip())
      if possible.get(hand[1]) < int(hand[0]):
        error = True
  if not error:
    sum += current
    
print(sum) 
        
  