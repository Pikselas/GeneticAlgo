
class Individual:
    Chromosome = 0
    Fitness = 0
    Probability = 0
    ExpectedCount = 0
    ActualCount = 0

    def __init__(self , chromosome , fitness , fitness_summation , fitness_avg):
        self.Chromosome = chromosome
        self.Fitness = fitness
        self.Probability = fitness / fitness_summation
        self.ExpectedCount = fitness / fitness_avg
        self.ActualCount = round(self.ExpectedCount)
    
    def __lt__(self, other):
        if self.ActualCount < other.ActualCount:
            return True
        elif self.ExpectedCount < other.ExpectedCount:
            return True
        elif self.Probability < other.Probability:
            return True
        else:
            return False
        return True

    def __repr__(self):
        return f"Chromosome: {self.Chromosome} , Fitness: {self.Fitness} , Probability: {self.Probability} , ExpectedCount: {self.ExpectedCount} , ActualCount: {self.ActualCount}"


# takes in a population & f(x) and returns collection of strong individuals
def GetStrongPopulation(population , fx):
    
    # calculate fx for each individual
    fx_Res = [fx(individual) for individual in population]
    
    # calculate summation of fx's
    summation = sum(fx_Res)
    
    # calculate average of fx's
    avg = summation / len(population)

    Individuals = [ Individual(population[i] , fx_Res[i] , summation , avg) for i in range(len(population)) ]

    # sort individuals
    Individuals.sort()

    # return strong individuals
    strongIndividuals = []
    for individual in Individuals:
        if individual.ActualCount > 0:
            strongIndividuals.append(individual)
    return strongIndividuals 

In = GetStrongPopulation([13 , 24 , 8 , 19] , lambda x: x**2)

print(In)