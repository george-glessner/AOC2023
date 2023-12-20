import re 
import math

finalSum = 0
coordinateMap = {"R": 1, "L": -1, "U": 1, "D": -1}
xAxis = ["R", "L"]
yAxis = ["U", "D"]
input = []
coordinates = []
currentX = 0
currentY = 0

with open("test.txt", "r") as f:
  inputs = [line.split(' ') for line in f]
  input = [[i[0], int(i[1])] for i in inputs]

for i, coordinate in enumerate(input):
  if coordinate[0] in xAxis:
    currentX += coordinate[1] * coordinateMap.get(coordinate[0])
    coordinates.append([currentX, currentY])
  else:
    currentY += coordinate[1] * coordinateMap.get(coordinate[0])
    coordinates.append([currentX, currentY])

'''
Let 'vertices' be an array of N pairs (x,y), indexed from 0
Let 'area' = 0.0
for i = 0 to N-1, do
  Let j = (i+1) mod N
  Let area = area + vertices[i].x * vertices[j].y
  Let area = area - vertices[i].y * vertices[j].x
end for
Return 'area'

https://web.archive.org/web/20090220072705/http://valis.cs.uiuc.edu/~sariel/research/CG/compgeom/msg00831.html
'''   
coordinateLength = len(coordinates)   
for i in range(coordinateLength):
  j = (i+1) % coordinateLength
  finalSum = finalSum + coordinates[i][0] * coordinates[j][1]
  finalSum = finalSum - coordinates[i][1] * coordinates[j][0]
  
print(coordinates)
print(abs(finalSum)/2)