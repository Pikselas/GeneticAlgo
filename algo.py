
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
        return f"Chromosome: {self.Chromosome}\nFitness: {self.Fitness}\nProbability: {self.Probability}\nExpectedCount: {self.ExpectedCount}\nActualCount: {self.ActualCount}\n"

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
    Individuals.sort(reverse=True)

    # return strong individuals
    strongIndividuals = []
    for individual in Individuals:
        if individual.ActualCount > 0:
            strongIndividuals.append(individual)
        else:
            break
    return strongIndividuals 

def GetSelectionPairs(strong_populations):
    if len(strong_populations) >= 2:
        pairs = []
        select_len = None
        if len(strong_populations) % 2 == 0:
            select_len = len(strong_populations)
        elif len(strong_populations) >= 3:
            select_len = len(strong_populations) - 3
        else:
            pairs.append((strong_populations[0] , strong_populations[1]))
        
        for i in range(0 , select_len , 2):
                pairs.append((strong_populations[i] , strong_populations[i+1]))

        if select_len != None and select_len != len(strong_populations):
            pairs.append((strong_populations[-2] , strong_populations[-1]))
            pairs.append((strong_populations[-3] , strong_populations[-1]))
        
        return pairs
    else:
        return None

# performs crossover between two individuals based on cut points
def PerformCrossOver(individual1 , individual2 , cut_points = []):
    offspring1 = ""
    offspring2 = ""

    for i in range(len(cut_points) - 1):
        if i % 2 == 0:
            offspring1 += individual1[cut_points[i] : cut_points[i+1]]
            offspring2 += individual2[cut_points[i] : cut_points[i+1]]
        else:
            offspring1 += individual2[cut_points[i] : cut_points[i+1]]
            offspring2 += individual1[cut_points[i] : cut_points[i+1]]  
    return offspring1 , offspring2


# generates uniform cut points based on frequency
def UniformCutPoints(length , frequency = 1):
    return [i for i in range(0 , length + 1 , frequency)]

def to_binary(n, digits):
    return format(n, f'0{digits}b')


#population = [9 , 11 , 13 , 15]
#fx = lambda x: 2 * x ** 2 + 3 * x + 1

# for i in range(2):
#     strong_population = GetStrongPopulation(population , fx)
#     pairs = GetSelectionPairs(strong_population)
#     population = []
#     for pair in pairs:
#         print(pair)
#         offspring1 , offspring2 = PerformCrossOver(to_binary(pair[0].Chromosome , 5) , to_binary(pair[1].Chromosome , 5) , UniformCutPoints(6))
#         population.append(int(offspring1 , 2))
#         population.append(int(offspring2 , 2))
#     print(i , "generation" ,population)
#     print("=====================================")