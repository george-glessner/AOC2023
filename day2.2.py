import re

sum = 0

f = open("input.txt", "r")
for x in f:
  x = x.strip()
  curr = re.split("Game \d+:", x)
  games = curr[1].split(";")
  min_results = {"red": 0, "green": 0, "blue": 0}
  for game in games:
    grabbed = re.split("\w ,", game)
    grabbed = grabbed[0].split(",")
    for pulled in grabbed:
      hand = re.split("\s", pulled.strip())
      if int(hand[0]) > min_results.get(hand[1]):
        min_results[hand[1]] = int(hand[0])
  answer = 1
  for i in min_results:
    answer = answer*min_results[i]
  sum += answer
    
print(sum) 
        
  