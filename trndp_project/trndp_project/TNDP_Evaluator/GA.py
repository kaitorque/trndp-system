import random
import time

POP_SIZE = 50
NUM_ROUTE = 4
MUTATION_RATE = 0.1
NUM_NODE = 15
MAX_NODE = 10

class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome    #Exp: [0,0,0,0,0,0]
        self.fitness = 0                #Calculated Fitness

    def setChromosome(self, chromosome):
        self.chromosome = chromosome

    def setFitness(self, fitvalue):
        self.fitness = fitvalue


def initialize(popsize):
    population = []
    node_list = list(range(1, NUM_NODE))
    for x in range(popsize):
        chromosome = []
        for y in range(NUM_ROUTE):
            first = random.randint(1, NUM_NODE)
            second = random.choice([ele for ele in node_list if ele != first])
            route = sorted([first, second])
            if route in chromosome:
                first = random.randint(1, NUM_NODE)
                second = random.choice([ele for ele in node_list if ele != first])
                route = sorted([first, second])
            chromosome.append(route)
        population.append(Individual(chromosome))
    return population

#population = initialize(POP_SIZE)
#for x in population:
#    print(x.chromosome)