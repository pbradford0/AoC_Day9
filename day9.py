#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/9

import sys
import itertools

def longest_route(filename):
  #output: distance of longest route
  longest = 0
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
  routes = itertools.permutations(locations)
  #determine which route is the fastest
  #add all distances for one route,
  #then compare it to the next one to see which is smaller
  for route in routes:
    prev_stop = ()
    route_distance = 0
    for stop in route:
      if prev_stop:
        for lookup in distances:
          if lookup[0] == prev_stop and lookup[1] == stop:
            route_distance += lookup[2]
          elif lookup[1] == prev_stop and lookup[0] == stop:
            route_distance += lookup[2]
      prev_stop = stop
    longest = max(longest, route_distance)
    #print str(route) + ": " + str(route_distance)
  return longest

def shortest_route(filename):
  #output: distance of shortest route
  shortest = 999999
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
  routes = itertools.permutations(locations)
  #determine which route is the fastest
  #add all distances for one route,
  #then compare it to the next one to see which is smaller
  for route in routes:
    prev_stop = ()
    route_distance = 0
    for stop in route:
      if prev_stop:
        for lookup in distances:
          if lookup[0] == prev_stop and lookup[1] == stop:
            route_distance += lookup[2]
          elif lookup[1] == prev_stop and lookup[0] == stop:
            route_distance += lookup[2]
      prev_stop = stop
    shortest = min(shortest, route_distance)
  return shortest

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  a = shortest_route(sys.argv[1])
  print "The shortest route is distance " + str(a)
  
  b = longest_route(sys.argv[1])
  print "The longest route is distance" + str(b)

if __name__ == '__main__':
  main()