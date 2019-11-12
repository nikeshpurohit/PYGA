import random
from statistics import mean
import matplotlib.pyplot as plt

N = 50 #number of bits in the string
P = 50 #population size (no of individuals in the population)
nGen = 50 #number of generations
mutRate = 0.02 #mutation rate

class individual():
    gene = [] 
    fitness = 0

    def __init__(self):
        self.gene = []
        self.fitness = 0
        
    def randomiseGene(self):
        for i in range (0, N):
            c = random.randrange(0, 2, 1)
            self.gene.append(c)

    def setGene(self, gene):
        self.gene = gene

    def printGene(self):
         print(self.gene)
        
    def printFitness(self):
        print(self.fitness)

#population = [] #list to store the population of individuals
#winners = [] #list to store selected individuals

def createInitalPopulation(): #create P number of individuals and append them to the list.
    pop = []
    for x in range(0, P):
        i = individual()
        pop.append(i)
    return pop

def randomisePopulation(pop): #function to set up the intial random genes in the population
    for i in pop:
        i.randomiseGene()
        #i.printGene()

def calculateFitness(indiv): #function to calculate and store the fitness value for a given individual
    count = 0
    for i in indiv.gene:
        if i == 1:
            count = count + 1
    indiv.fitness = count

def recalculateAllFitness(pop):
    for i in pop:
        calculateFitness(i)

def randomIndividual(pop): #function to pick and return a random individual from a given list
    indiv = random.choice(pop)
    return indiv

def selectWinners(pop): #function to select P number of winners by comparing two and selecting the one with the highest fitness or a random one if equal
    winners = []
    while len(winners) != P:
        i1 = randomIndividual(pop)
        i2 = randomIndividual(pop)
        if i1.fitness > i2.fitness:
            winners.append(i1)
        elif i1.fitness == i2.fitness:
            winners.append(random.choice([i1,i2]))
        elif i2.fitness > i1.fitness:
            winners.append(i2)
    return winners

def mutateIndividual(indiv): #perform mutation in all bits in an individuals gene
    for index, b in enumerate(indiv.gene):
        if random.random() < mutRate:
            if b == 1:
                indiv.gene[index] = 0
            if b == 0:
                indiv.gene[index] = 1

def doCrossover(pop):
    motherlist = pop[::2] #get every member at even positions
    fatherlist = pop[1::2] #get every member at odd positions
    postCrossoverChilden = [] # a list to hold the children after crossover
    for i in range(0, int(P/2)):
        parent1 = motherlist[i]
        parent2 = fatherlist[i]
        pivotpoint = random.randint(0,N)
        while pivotpoint == 0 or pivotpoint == N: #make sure pivotpoint is not 0 or N
            pivotpoint = random.randint(0,N)
        #print("pivotpoint", pivotpoint, "p1gene", motherlist[i].gene, "p2gene", fatherlist[i].gene)
        child1Gene = fatherlist[i].gene[:pivotpoint] + motherlist[i].gene[pivotpoint:]
        child1 = individual()
        child1.setGene(child1Gene)
        calculateFitness(child1)
        postCrossoverChilden.append(child1)
        child2Gene = motherlist[i].gene[:pivotpoint] + fatherlist[i].gene[pivotpoint:]
        child2 = individual()
        child2.setGene(child2Gene)
        calculateFitness(child2)
        postCrossoverChilden.append(child2)
    return postCrossoverChilden

def findGoldenBaby(pop): #this function is specfic to the fitness function used
    for i in pop:
        if i.fitness == N:
            print("  GoldenBaby: Individual with fitness " + str(i.fitness) + ", found! Quit searching")
            return i
    return None

def findAllTimeBest(pop, previous):
    if previous == None:
        previous = pop[0]
    best = previous
    for i in pop:
        calculateFitness(i)
        if i.fitness > previous.fitness:
            best = i
    return best



        

    
#REPLACE THE WORST INDIVIDUAL WITHT HE ALL TIME BEST AT THE END OF EVERY GENERATION


def runGA():
    #Lists to store population
    meanPlot = []
    bestPlot = []
    winners = []
    population = []
    goldenBaby = None
    allTimeBest = None
    generation = 0

    #Create population with random genes
    population = createInitalPopulation()
    randomisePopulation(population)
    generation += 1

    #Generate their fitness values
    for i in population:
        calculateFitness(i)
        #i.printFitness()
    print("  The average fitness for the initial population is", mean(i.fitness for i in population))

    while generation <= nGen: #stop the loop once fitness N is reached
        if goldenBaby == None:
            recalculateAllFitness(population)
            goldenBaby = findGoldenBaby(population)

        print()
        print("========Generation",str(generation)+"========")
        print()
        #Perform selection
        winners = selectWinners(population)
        #print("  mean fitness after selection is", mean(i.fitness for i in winners))

        #Perform crossover
        population = doCrossover(winners)
        #print("  mean fitness after crossover is", mean(i.fitness for i in population))

        #Perform mutation
        for i in population:
            mutateIndividual(i)
        recalculateAllFitness(population)
        #print("  mean fitness after mutation is", mean(i.fitness for i in population))

        #Gather some data
        if goldenBaby == None:
            recalculateAllFitness(population)
            goldenBaby = findGoldenBaby(population)

        if goldenBaby != None:
            print("  Golden baby found in",generation,"generations.")
            allTimeBest = goldenBaby
            break;
        
        
        recalculateAllFitness(population)
        allTimeBest = findAllTimeBest(population, allTimeBest)
        print("  The fittest individual this generation has a fitness value of", allTimeBest.fitness)
        bestPlot.append(allTimeBest.fitness)

        meanVal = mean(i.fitness for i in population)
        print("  The average fitness value for this generation is", meanVal)
        meanPlot.append(meanVal)


        #Finish generation
        generation += 1
    plt.plot(bestPlot)
    plt.plot(meanPlot)
    plt.xlabel('Generation')
    plt.ylabel('Fitness')
    plt.show()


runGA()
