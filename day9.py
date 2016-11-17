#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/8

import sys

def quickest_route(filename):
  #output: distance of shortest route
  shortest = 0
  distances = []
  routes = []
  locations = []
  stops = 0
  #convert the file into a list of tuples
  input = open(filename, 'rU')
  for line in input:
    chop = line.split()
    distances.append((str(chop[0]), str(chop[2]), int(chop[4])))
  #create a list of locations (len will determine stops/route)
  for item in distances:
    if item[0] not in locations:
      locations.append(item[0])
    elif item[1] not in locations:
      locations.append(item[1])
  stops = len(locations)
  #create a list of all possible end distances
  #begin witn 12345678 -> 12345687
  stops_0 = 0
  stops_1 = 0
  stops_2 = 0
  stops_3 = 0
  stops_4 = 0
  stops_5 = 0
  stops_6 = 0
  stops_7 = 0
  while stops_0 <= stops:
    routes.append([])
    while stops_y <= stops:
      if () not in
    stops_y = 0
    stops_x += 1
  #determine which route is the fastest
  #add all distances for one route,
  #then compare it to the next one to see which is smaller
  
  return shortest

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  a = quickest_route(sys.argv[1])
  print "The shortest route is distance " + str(a)
  
  #b = encode_calc(sys.argv[1])
  #print "(encoded chars) - (literal chars) = " + str(b)

if __name__ == '__main__':
  main()