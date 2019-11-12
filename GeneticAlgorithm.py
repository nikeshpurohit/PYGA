import random

N = 10 #number of bits in the string
P = 10 #population size (no of individuals in the population)
nGen = 3 #number of generations
mutRate = 1/P #mutation rate

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

population = [] #list to store the population of individuals
winners = [] #list to store selected individuals

def createInitalPopulation(): #create P number of individuals and append them to the list.
    for x in range(0, P):
        i = individual()
        population.append(i)

def randomisePopulation(): #function to set up the intial random genes in the population
    for i in population:
        i.randomiseGene()
        #i.printGene()

def calculateFitness(indiv): #function to calculate and store the fitness value for a given individual
    count = 0
    for i in indiv.gene:
        if i == 1:
            count = count + 1
    indiv.fitness = count

def randomIndividual(pop): #function to pick and return a random individual from a given list
    indiv = random.choice(pop)
    return indiv

def selectWinners(): #function to select P number of winners by comparing two and selecting the one with the highest fitness or a random one if equal
    while len(winners) != P:
        i1 = randomIndividual(population)
        i2 = randomIndividual(population)
        if i1.fitness > i2.fitness:
            winners.append(i1)
        elif i1.fitness == i2.fitness:
            winners.append(random.choice([i1,i2]))
        elif i2.fitness > i1.fitness:
            winners.append(i2)

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
        

    
#initalise and randomise
createInitalPopulation()
randomisePopulation()

#generate fitness values
for i in population: #calculate the fitness of each individual in population
    calculateFitness(i)
    i.printFitness()

#selection
selectWinners()

#mutation
for i in winners: #perform mutation on all individuals in the winners list
    mutateIndividual(i)
    calculateFitness(i)
    i.printFitness()

#crossover
population = doCrossover(winners)

for i in winners:
    i.printFitness()

# repeat this process for n generations!