import random

N = 10 #number of bits in the string
P = 10 #population size (no of individuals in the population)
nGen = 3 #number of generations

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
            #print(self.gene)

    def printGene(self):
         print(self.gene)
        
    def printFitness(self):
        print(self.fitness)

population = [] #list to store the population of individuals

def createInitalPopulation(): #create P number of individuals and append them to the list.
    for x in range(0, P):
        i = individual()
        population.append(i)

def randomisePopulation(): #function to set up the intial random genes in the population
    for i in population:
        i.randomiseGene()
        i.printGene()

def calculateFitness(indiv): #function to calculate and store the fitness value for a given individual
    count = 0
    for i in indiv.gene:
        if i == 1:
            count = count + 1
    indiv.fitness = count

#initalise and randomise
createInitalPopulation()
randomisePopulation()

#generate fitness values
for i in population: #calculate the fitness of each individual in population
    calculateFitness(i)
    #i.printFitness()

#selection
winners = [] #a list to store the selected individuals

