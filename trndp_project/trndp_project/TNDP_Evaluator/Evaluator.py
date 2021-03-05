import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import pandas as pd
import copy 
import math

POP_SIZE = 200
NUM_ROUTE = 4
MUTATION_RATE = 0.25
MAX_NODE = 10
ELITE_RATIO = 20

NUM_NODE = 15
MIN_NODE = 2
W_SHORTPATH= 0.05
W_TRANSFER= 1
W_CO= 1

NETWORK_TYPE = "mandl1"

MAX_GEN = 500

class Individual:
    def __init__(self, chromosome, graph = nx.Graph()):
        self.chromosome = chromosome    #Exp: [0,0,0,0,0,0]
        self.fitness = 0                #Calculated Fitness
        self.graph = graph
        self.d0 = 0
        self.d1 = 0
        self.d2 = 0
        self.dun = 0
        self.travelTime = 0
        self.atravelTime = 0
        self.opcost = 0


demandMatrix = [[0 for j in range(NUM_NODE)] for i in range(NUM_NODE)] 
pos = {}
def resetNetwork():
    demandMatrix = [[0 for j in range(NUM_NODE)] for i in range(NUM_NODE)] 
    pos = {}

def createNetwork():
    G = nx.Graph()
    #Nodes
    f = open(f"trndp_project/TNDP_Evaluator/input/{NETWORK_TYPE}_nodes.txt", "r")
    count = 0
    nodes = []
    for line in f:
        if count > 0:
            nodes.append(line.split(","))
        count+=1
    f.close()
    
    for x in nodes:
        G.add_node(int(x[0]))
        pos[int(x[0])]=[float(x[1]),float(x[2])]
    #print(pos)
    #link
    f = open(f"trndp_project/TNDP_Evaluator/input/{NETWORK_TYPE}_links.txt", "r")
    count = 0
    link = []
    for line in f:
        if count > 0:
            link.append(list(map(int, line.split(","))))
        count+=1
    f.close()
    for x in link:
        G.add_edge(x[0], x[1], weight=x[2])
    #demand
    f = open(f"trndp_project/TNDP_Evaluator/input/{NETWORK_TYPE}_demand.txt", "r")
    count = 0
    demand = []
    for line in f:
        if count > 0:
            demand.append(list(map(int, line.split(","))))
        count+=1
    f.close()
    totalDemand = 0
    for line in demand:
        totalDemand += line[2]
        demandMatrix[line[0]-1][line[1]-1] = line[2]
    #print(demandMatrix)
    #for x in demand:
    #    G.add_edge(x[0], x[1], demand=x[2])
    
    
    return G, totalDemand

G, totalDemand = createNetwork()

def addMissingNode(missing_node, chromosome):
    count = 0
    random.shuffle(missing_node)
    while missing_node and count < len(missing_node):
        x = missing_node[count]
        found = False
        for j, y in enumerate(chromosome):
            #print("Chromosome inside: ", chromosome[j])
            if found:
                break
            if len(y) < MAX_NODE:
                for k, z in enumerate(chromosome[j]):
                    #print("Chromosome inside 2: ", chromosome[j][k])
                    if k == 0:
                        if G.has_edge(chromosome[j][k], x):
                            #print("has path")
                            if x not in chromosome[j]:
                                chromosome[j].insert(k, x)
                                #print(f"Edge Front[{x}]: ", chromosome[j])
                                found = True
                                break
                        else:
                            floyd = nx.shortest_path(G,source=x,target=z,weight="weight")
                            if (len(set(floyd[:-1]) & set(chromosome[j]))) == 0 and len(floyd[:-1] + chromosome[j]) <= MAX_NODE:
                                chromosome[j] = floyd[:-1] + chromosome[j]
                                #print(f"Floyd Front[{x}]: ", chromosome[j])
                                found = True
                                break
                    elif k == (len(chromosome[j])-1):
                        if G.has_edge(chromosome[j][k], x):
                            #print("edge end", chromosome[j][k], x)
                            if x not in chromosome[j]:
                                chromosome[j].insert(len(chromosome[j]), x)
                                #print(f"Edge End[{x}]: ", chromosome[j])
                                found = True
                                break
                        else:
                            floyd = nx.shortest_path(G,source=z,target=x,weight="weight")
                            if (len(set(floyd[1:]) & set(chromosome[j]))) == 0 and len(chromosome[j] + floyd[1:]) <= MAX_NODE:
                                chromosome[j] = chromosome[j] + floyd[1:]
                                #print(f"Floyd End[{x}]: ", chromosome[j])
                                found = True
                                break
                    else:
                        if G.has_edge(chromosome[j][k], x) and G.has_edge(chromosome[j][k+1], x):
                            if x not in chromosome[j]:
                                chromosome[j].insert(k+1, x)
                                #print(f"Edge Mid[{x}]: ", chromosome[j])
                                found = True
                                break
                        else:
                            startfloyd = nx.shortest_path(G,source=x,target=chromosome[j][k-1],weight="weight") #[x, a, b, c]
                            endfloyd = nx.shortest_path(G,source=chromosome[j][k],target=x,weight="weight") #[a, b, c, x]
                            combinefloyd = endfloyd + startfloyd[1:]
                            floyd = endfloyd[1:] + startfloyd[1:-1]
                            floyd.reverse()
                            if(len(set(endfloyd[1:]) & set(endfloyd[1:-1])) == 0) and (len(set(floyd) & set(chromosome[j]))) == 0 and len(chromosome[j] + floyd) <= MAX_NODE:
                                #print(f"Combined Floyd[{x}]", combinefloyd)
                                #print(f"Cut Floyd[{x}]", floyd)
                                chromosome[j][k:k] = floyd
                                #print(f"Floyd Mid[{x}]", chromosome[j])
                                found = True
                                break 
        #Recheck for missing node
        count += 1
        node_exist = []             
        for x in chromosome:
            node_exist += x
            #print("node_exist", node_exist)
        node_set = set(node_exist)
        #print("node_set: ", node_set)
        all_node = set(range(1, NUM_NODE))
        if found:
            missing_node = list(all_node-node_set)
            count = 0
    tempG = nx.Graph()
    for x in chromosome:
        nx.add_path(tempG, x)
    for x in tempG.edges():
        tempG.add_edge(x[0], x[1], weight=G[x[0]][x[1]]["weight"])
    #print("list edges: ", tempG.edges())
    return chromosome, missing_node, tempG

def fitnessCalc(population):
    for index, x in enumerate(population):
        #print(x.chromosome)
        chromostr = []
        Co = 0
        #Cr = 0
        for i, y in enumerate(x.chromosome):
            routeCost = 0
            for j, z in enumerate(y):
                if j < len(y)-1:
                    distance = x.graph[x.chromosome[i][j]][x.chromosome[i][j+1]]["weight"]
                    routeCost += distance
                    Co += distance
            #routeDemand = demandMatrix[x.chromosome[i][0]-1][x.chromosome[i][-1]-1]
            #Cr += routeCost*routeDemand
            chromostr.append(",".join(map(str, y)))
            y.reverse()
            chromostr.append(",".join(map(str, y)))
        #print(chromostr)
        len_path = dict(nx.all_pairs_dijkstra(x.graph))
        # print(len_path[3][0][1]) source, len, target
        # print(len_path[3][1][1]) source, path, target
        d0 = 0
        d1 = 0
        d2 = 0
        dun = 0
        totalTravelTime = 0
        total = 0
        cost = 0
        cost2 = 0
        cost3 = 0
        #totalDemand = 0
        for i, y in enumerate(demandMatrix):
            for j, z in enumerate(y):
                path = len_path[i+1][1][j+1]
                oripath = ",".join(map(str, path))
                travelTime = len_path[i+1][0][j+1]
                count = 0
                c0=0
                c1=0
                c2=0
                cun=0
                while path:
                    k = len(path)
                    while k >= 0:
                        pathstr = ",".join(map(str, path[:k]))
                        if any(pathstr in item for item in chromostr):
                            #print("Found: ", pathstr)
                            if k == len(path):
                                path = path[k:]
                                break
                            else:
                                path = path[k-1:]
                                count += 1
                                break
                        else:
                            k -= 1
                #print("Path String: ", oripath)
                if count == 0:
                    c0+=1
                    d0 += demandMatrix[i][j]
                elif count == 1:
                    c1+=1
                    d1 += demandMatrix[i][j]
                elif count == 2:
                    c2+=1
                    d2 += demandMatrix[i][j]
                else:
                    cun+=1
                    dun += demandMatrix[i][j]
                #print("Transfer: ", count)
                #print(f"Travel Time [{i+1}][{j+1}]: ", travelTime)
                travelTransfer = travelTime + count*5
                #print(f"Travel Time + Tansfer [{i+1}][{j+1}]: ", travelTransfer)
                totalTravelTime += travelTransfer
                cost += demandMatrix[i][j]*travelTransfer
                cost2 += demandMatrix[i][j]*travelTime
                cost3 += demandMatrix[i][j]*count
                total += 1
                #totalDemand += demandMatrix[i][j]
                # print(f"Path[{i+1}][{j+1}]: ", len_path[i+1][1][j+1])
                # print(f"Length[{i+1}][{j+1}]: ", len_path[i+1][0][j+1])
                # print("")
        #print("d0: ", d0)
        population[index].d0 = d0
        #print("d1: ", d1)
        population[index].d1 = d1
        #print("d2: ", d2)
        population[index].d2 = d2
        #print("dun: ", dun)
        population[index].dun = dun
        #print("Total travel Time: ", totalTravelTime)
        population[index].travelTime = cost
        att = cost/totalDemand
        population[index].atravelTime = att
        #print("Average Travel Time: ", att)
        #print("Total Cost: ", cost)
        #print("Operator Cost: ", Co)
        population[index].opcost = Co
        #print("Route Cost: ", Cr)
        #print("Total Demand: ", totalDemand)
        FitnessVal = cost2*W_SHORTPATH+cost3*W_TRANSFER+Co*W_CO
        #print("Objective Function", FitnessVal)
        population[index].fitness = FitnessVal
    return population


def selection(population):
    population = sorted(population, key=lambda x: x.fitness, reverse=True)
    #print("Sorted")
    halfpop = POP_SIZE/2
    selectionResults = []
    eliteSize =int((ELITE_RATIO/100.0)*POP_SIZE)
    for x in range(eliteSize):
        selectionResults.append(population.pop())

    while len(selectionResults) < halfpop:
        index = random.randint(0, len(population)-1)
        index2 = random.randint(0, len(population)-1)
        pair = population[index]
        #print(pair.fitness)
        pair2 = population[index2]
        #print(pair2.fitness)
        pick = random.randint(0, 3)
        if pick == 0:
            if pair.fitness > pair2.fitness:
                selectionResults.append(population.pop(index))
            else:
                selectionResults.append(population.pop(index2))
        else:
            if pair.fitness < pair2.fitness:
                selectionResults.append(population.pop(index))
            else:
                selectionResults.append(population.pop(index2))
    # for x in selectionResults:
    #     print(x.fitness)
    return selectionResults

def crossover(population):
    newPopulation = copy.deepcopy(population)
    while len(newPopulation) < POP_SIZE :
        index = random.randint(0, len(population)-1)
        index2 = random.randint(0, len(population)-1)
        while index2==index:
            index2 = random.randint(0, len(population)-1)
        offspring = copy.deepcopy(population[index])
        offspring2 = copy.deepcopy(population[index2])
        swap1 = random.randint(0, NUM_ROUTE-1)
        swap2 = random.randint(0, NUM_ROUTE-1)
        tempChromosome = offspring.chromosome[swap1]
        offspring.chromosome[swap1] = offspring2.chromosome[swap2]
        offspring2.chromosome[swap2] = tempChromosome
        # print("After1: ", offspring.chromosome)
        # print("After2: ", offspring2.chromosome)
        newPopulation.append(Individual(offspring.chromosome))
        newPopulation.append(Individual(offspring2.chromosome))
    # for i, x in enumerate(newPopulation):
    #     if i == 25:
    #         print("Offspring")
    #     if i >= 25:
    #         print(x.chromosome)
    return newPopulation

def mutate(population):
    for i, x in enumerate(population):
        for j, y in enumerate(x.chromosome):
            if random.random() < MUTATION_RATE:
                #print(y)
                if len(y) > 2:
                    cutRoute = random.randint(1, len(y)-2)
                    #print("Cut Route: ", cutRoute)
                    #print("Before:", population[i].chromosome[j])
                    if bool(random.getrandbits(1)):
                        population[i].chromosome[j] = y[cutRoute:]
                    else:
                        population[i].chromosome[j] = y[:-cutRoute]
                    #print("After:", population[i].chromosome[j])
    return population
    
                    
        

#Initialize population
def initialize(popsize):
    population = []
    node_list = list(range(1, NUM_NODE))
    x = 0
    while x < popsize:
        chromosome = []
        #chromostr = []
        node_exist = []
        #Generate route
        for y in range(NUM_ROUTE):
            first = random.randint(1, NUM_NODE)
            second = random.choice([ele for ele in node_list if ele != first])
            route = sorted([first, second])
            floyd = nx.shortest_path(G,source=first,target=second,weight="weight")
            floydsize = len(floyd)
            #Check for duplicate route or maximum node traversal
            if floyd in chromosome or floydsize>MAX_NODE:
                first = random.randint(1, NUM_NODE)
                second = random.choice([ele for ele in node_list if ele != first])
                route = sorted([first, second])
                floyd = nx.shortest_path(G,source=first,target=second,weight="weight")
                floydsize = len(floyd)
            node_exist += floyd
            chromosome.append(floyd)
            #chromostr += floyd + [0]
        node_set = set(node_exist)
        all_node = set(range(1, NUM_NODE))
        missing_node = list(all_node-node_set)
        #print(f"Chromosome[{x}]: ", chromosome)
        #print(f"Missing node[{x}]: ", missing_node)
        chromosome, missing_node, tempG = addMissingNode(missing_node, chromosome)
        #print(f"After Chromosome[{x}]: ", chromosome)
        #print(f"After Missing node[{x}]: ", missing_node)
        #print("Connected: ", nx.is_connected(tempG))
        #print("")
        if not missing_node and nx.is_connected(tempG):
            population.append(Individual(chromosome,tempG))
            x += 1
    return population

def listMissingNode(individual):
    node_exist = []
    for x in individual.chromosome:
        node_exist += x
    node_set = set(node_exist)
    all_node = set(range(1, NUM_NODE))
    missing_node = list(all_node-node_set)
    return missing_node
    


def gaEval(networkid): 
    time_start = time.process_time() 
    population = initialize(POP_SIZE)
    t = 0
    lastChange = 0
    lastElapse = (time.process_time()-time_start)
    bestFitness = math.inf
    bestChromosome = []
    bestd0 = []
    bestd1 = []
    bestd2 = []
    bestdun = []
    bestTT = []
    bestATT = []
    bestNetwork = []
    bestGraph = nx.Graph()
    while t < MAX_GEN:
        print(f"Generation {t+1}")
        print("---------------------------------------------")
        population = fitnessCalc(population)
        population = sorted(population, key=lambda x: x.fitness)
        fitness = np.array([(y.fitness) for y in population])
        if population[0].fitness < bestFitness:
            bestFitness = population[0].fitness
            lastChange = t+1
            bestChromosome = population[0].chromosome
            bestd0 = (population[0].d0/totalDemand)*100
            bestd1 = (population[0].d1/totalDemand)*100
            bestd2 = (population[0].d2/totalDemand)*100
            bestdun = (population[0].dun/totalDemand)*100
            bestTT = population[0].travelTime
            bestATT = population[0].atravelTime
            bestNetwork = population[0].opcost
            lastElapse = (time.process_time()-time_start)
            bestGraph = population[0].graph
        print("Average Fitness: ", np.mean(fitness))
        print("Last Best Change: ", lastChange)
        print("Time: %.2f" % lastElapse)
        print("---------------------------------------------")
        print("Best Chromosome: ", bestChromosome)
        print("Best Fitness: ", bestFitness)
        print("Best d0: %.2f" % bestd0)
        print("Best d1: %.2f" % bestd1)
        print("Best d2: %.2f" % bestd2)
        print("Best dun: %.2f" % bestdun)
        print("Best Travel Time: ", bestTT)
        print("Best Average Travel Time: %.2f" % bestATT)
        print("Network Cost:", bestNetwork)
        print("---------------------------------------------")
        print("Chromosome:", population[0].chromosome)
        print("Fitness:", population[0].fitness)
        print("d0: %.2f" % ((population[0].d0/totalDemand)*100))
        print("d1: %.2f" % ((population[0].d1/totalDemand)*100))
        print("d2: %.2f" % ((population[0].d2/totalDemand)*100))
        print("dun: %.2f" % ((population[0].dun/totalDemand)*100))
        print("Travel Time: ", population[0].travelTime)
        print("Average Travel Time: %.2f" % population[0].atravelTime)
        print("Network Cost:", population[0].opcost)
        print("Total Time: %.2f" % (time.process_time()-time_start))
        print("---------------------------------------------")
        if np.mean(fitness) <= bestFitness:
            break

        population = selection(population)
        population = crossover(population)
        population = mutate(population)
        feastPop = []
        for x in population:
            missing_node = listMissingNode(x)
            #print("Old: ", x.chromosome)
            chromosome, missing_node, tempG = addMissingNode(missing_node, x.chromosome)
            if not missing_node and nx.is_connected(tempG):
                #print("New: ",chromosome)
                feastPop.append(Individual(chromosome,tempG))
            else:
                #print("Infeasible Chromosome")
                pass
        # print(len(feastPop))
        #del population
        population.clear()
        population= copy.deepcopy(feastPop)
        # print(len(population))
        t += 1
        #print(population[0].chromosome)
    # f = open(f"trndp_project/TNDP_Evaluator/eval.txt", "w")
    # f.write("Best d0: %.2f\n" % bestd0)
    # f.write("Best d1: %.2f\n" % bestd1)
    # f.write("Best d2: %.2f\n" % bestd2)
    # f.write("Best dun: %.2f\n" % bestdun)
    # f.write("Best Average Travel Time: %.2f\n" % bestATT)
    # f.write(f"Network Cost: {bestNetwork}\n")
    # f.write("Time: %.2f\n" % lastElapse)
    # f.write("Total Time: %.2f\n" % (time.process_time()-time_start))
    # f.write(f"Last Best Change: {lastChange}")

    
    plt.subplots()
    edge_labels = nx.get_edge_attributes(bestGraph, "weight")
    nx.draw(bestGraph, pos, with_labels=True, font_weight='bold')
    nx.draw_networkx_edge_labels(bestGraph, pos, edge_labels=edge_labels)
    # plt.savefig("trndp_project/TNDP_Evaluator/network")
    plt.savefig("trndp_web/static/network/"+str(networkid))
    # plt.show()
    plt.clf()

    route = ""
    for i, x in enumerate(bestChromosome):
        route += "Route ["+str(i+1)+"]: "+str(x)+"\n"
        #f.write(f"Route [{i+1}]: {x}\n")
    # f.write("d0: %.2f\n" % bestd0)
    # f.write("d1: %.2f\n" % bestd1)
    # f.write("d2: %.2f\n" % bestd2)
    # f.write("dun: %.2f\n" % bestdun)
    # f.write("ATT: %.2f\n" % bestATT)
    # f.write(f"Network Cost: {bestNetwork}\n")
    # t = open(f"trndp_project/TNDP_Evaluator/comp.txt", "w")
    # t.write("Time: %.2f\n" % lastElapse)
    # t.write(f"Generation: {lastChange}\n")
    # t.write("Total Time: %.2f\n" % (time.process_time()-time_start))
    # t.close()
    #f.write("%.2f\n" % lastElapse)
    #f.write("%.2f\n" % (time.process_time()-time_start))
    #f.write(f"{lastChange}")
    # f.close()
    return {"route": route, "d0": bestd0, "d1": bestd1, "d2": bestd2, "dun": bestdun, "att": bestATT, "network": bestNetwork, "time": lastElapse, "gen": lastChange,"totaltime": time.process_time()-time_start}
