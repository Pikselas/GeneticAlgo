from algo import *
import math
import random

class City:
    def __init__(self, x, y , name):
        self.X = x
        self.Y = y
        self.Name = name
    def __repr__(self):
        return self.Name

def GetDistance(city1, city2):
    return abs(math.sqrt((city1.X - city2.X)**2 + (city1.Y - city2.Y)**2))

def GetFitness(chromosome):
    fitness = 0
    for i in range(len(chromosome) - 1):
        fitness += GetDistance(chromosome[i], chromosome[i+1])
    fitness += GetDistance(chromosome[len(chromosome) - 1], chromosome[0])
    return -fitness

def CrossOver(route1 , route2):
    # randomly select a point from route1
    point = random.randint(0, len(route1) - 1)
    # create a new route by taking the first part of route1
    new_route = route1[:point]
    # add cities from route2 that are not already in new_route
    for city in route2:
        if city not in new_route:
            new_route.append(city)
    return new_route

A = City(0, 0 , "A")
B = City(0, 10 , "B")
C = City(10, 10 , "C")
D = City(10, 0 , "D")
E = City(5, 5 , "E")

# staring from A via B, C, D, E
route1 = [A, B, C, D , E]
route2 = [A, B, D, C , E]
route3 = [A, D, B, C , E]
route4 = [A, D, C, B , E]

routes = [route1, route2 , route3 , route4]

for i in range(3):
    # get strong population
    strong_populations = GetStrongPopulation(routes , GetFitness)
    # get selection pairs
    pairs = GetSelectionPairs(strong_populations)
    if pairs == None:
        break
    # get new population
    new_populations = []
    for pair in pairs:
        new_populations.append(CrossOver(pair[0].Chromosome, pair[1].Chromosome))
    routes = new_populations
    print("Generation ->" , i , routes)