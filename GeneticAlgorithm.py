import random

N = 10 #number of bits in the string
P = 10 #population size
nGen = 3 #number of generations

class individual():
    gene = [] 
    fitness = 0
    def __init__(self):
        print("indiviual created")
        self.gene = gene
        self.fitness = fitness
        

    def randomiseGene(self):
        for i in range (0, N):
            c = random.randrange(0, 2, 1)
            self.gene.append(c)
            print(self.gene)

#class population():
#    def __init__(self):
#        pop = []

pop = [individual] #create the object P number of times

def calculateFitness(indiv):
    count = 0
    for i in indiv.gene:
        if i == 1:
            count = count + 1
    idiv.fitness = count
    print(count)


def startingPop():
    for i in range (0,1):
        individual.gene.append(i)

i1 = individual
i1.randomiseGene(i1)
calculateFitness(i1)