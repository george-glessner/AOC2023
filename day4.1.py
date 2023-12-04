import re 
import math

max = 0
current = 0
sum = 0 
cardNumber = 1

f = [line.rstrip() for line in open('input.txt')]

for x in f:
  card = re.split("Card +\d+: ", x)
  numbers = card[1].split(" | ")
  winningNumbers = numbers[0]
  myNumbers = numbers[1]
  current=0
  for number in myNumbers.split(" "):
    if number.strip().isnumeric() and number in winningNumbers.split(" "):
      if current == 0:
          current = 1
      else:
        current = current*2
  sum += current
print(sum)