import re 
import math

max = 0
current = 0
sum = 0 
cardNumber = 1

f = [line.rstrip() for line in open('input.txt')]

copies = []

for x in f:
  card = re.split("Card +\d+: ", x)
  cardNumber = re.findall("\d+:", x)
  cardNumber = int(cardNumber[0].split(":")[0])
  numbers = card[1].split(" | ")
  winningNumbers = numbers[0]
  myNumbers = numbers[1]
  current=0
  for number in myNumbers.split(" "):
    if number.strip().isnumeric() and number in winningNumbers.split(" "):
      current+=1
  if(current>0):
    for copy in range(0,current):
      copies.append(f[cardNumber+copy])

for x in copies:
  card = re.split("Card +\d+: ", x)
  cardNumber = re.findall("\d+:", x)
  cardNumber = int(cardNumber[0].split(":")[0])
  numbers = card[1].split(" | ")
  winningNumbers = numbers[0]
  myNumbers = numbers[1]
  current=0
  for number in myNumbers.split(" "):
    if number.strip().isnumeric() and number in winningNumbers.split(" "):
      current+=1
  if(current>0):
    for copy in range(0,current):
      copies.append(f[cardNumber+copy])

print(len(f) + len(copies))