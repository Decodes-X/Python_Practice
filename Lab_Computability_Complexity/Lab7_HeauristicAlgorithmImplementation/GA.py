import random
DataSet = open("dataset.out","r")
firstpass = True

GENES = []
TotalGeneesLength = len(GENES)
MUTATION_RATE = 0.2
TotalRunTime = 100
Generations = 200
with DataSet as f:
    if firstpass:
        next(f)
    data = f.readlines()
    for row in data:
        Elements = row.split(",")
        Time = float(Elements[2]) + float(Elements[3])
        GENES.append(Time)



def create_individual():
    return random.sample(GENES, TotalGeneesLength)

def calculate_fitness():
    for i in range(TotalGeneesLength):
        TotalTime += GENES[i]
    return TotalTime

def mutate(self):
    seq = self.chromosome[:]
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(TotalGeneesLength), 2)
        seq[i], seq[j] = seq[j], seq[i]
    return seq

def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]

    p2_filtered = [item for item in parent2 if item not in child]
    p2_index = 0
    for i in range(TotalGeneesLength):
        if child[i] is None:
            child[i] = p2_filtered[p2_index]
            p2_index += 1
    return child

def RunGA():
    population = [create_individual() for _ in range(TotalRunTime)]
    for gen in range(Generations):
        population.sort(key=calculate_fitness)
        parents = population[:int(TotalRunTime * 0.2)]
        next_generation = parents[:]

        while len(next_generation) < TotalRunTime:
            parent1, parent2 = random.sample(parents,2)
            child = crossover(parent1,parent2)
            child = mutate(child)
            next_generation.append(child)

        population = next_generation

    bestSequence = min(population, key=calculate_fitness)
    bestFitness = calculate_fitness(bestSequence)
    print(f"Best order: {bestSequence} | Shortest total time: {bestFitness} mins")

RunGA()




        
