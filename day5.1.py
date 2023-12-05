import re 
import math

max = 0
current = 0
min = 0 
input = []

f = open("input.txt", "r").read()

with open("input.txt", "r") as f:
  input = [line.rstrip() for line in f]
  input = list(filter(None, input))

seeds_to_soil_index = input.index("seed-to-soil map:")
soil_to_fertilizer_index = input.index("soil-to-fertilizer map:")
fertilizer_to_water_index = input.index("fertilizer-to-water map:")
water_to_light_index = input.index("water-to-light map:")
light_to_temperature_index = input.index("light-to-temperature map:")
temperature_to_humidity_index = input.index("temperature-to-humidity map:")
humidity_to_location_index = input.index("humidity-to-location map:")

seeds = input[0].split("seeds: ")[1].split()
seeds = list(map(int, seeds))

def findMin(curDestination, start, end):
  current=curDestination
  for x in input[start+1:end]:
    x = list(map(int, x.split()))
    destination, source, range = x
    # print(curDestination, destination, source, range)
    if source <= curDestination and curDestination < source + range:
      current = curDestination - source + destination
    if curDestination >= source and curDestination <= source + range:
      current = curDestination - source + destination
    else:
      pass
  return current
    
for seed in seeds:
  minDestination = findMin(seed, seeds_to_soil_index, soil_to_fertilizer_index)
  minDestination = findMin(minDestination, soil_to_fertilizer_index, fertilizer_to_water_index)
  minDestination = findMin(minDestination, fertilizer_to_water_index, water_to_light_index)
  minDestination = findMin(minDestination, water_to_light_index, light_to_temperature_index)
  minDestination = findMin(minDestination, light_to_temperature_index, temperature_to_humidity_index)
  minDestination = findMin(minDestination, temperature_to_humidity_index, humidity_to_location_index)
  minDestination = findMin(minDestination, humidity_to_location_index, len(input))
  if min == 0:
    min = minDestination
  if minDestination < min:
    min = minDestination
print(min)