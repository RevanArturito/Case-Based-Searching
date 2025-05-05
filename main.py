from MathFunction import *
from pair import *
from typing import List
from header import *
from mainUtils import *


bestChromosome = None
bestObjective = float("inf")
randomPopulation = RandomPopulation(POPULATIONS, CHROMOSOME_LENGTH)


# for i in range(0, POPULATIONS):
#     print(randomPopulation[i], " ", Fitness(randomPopulation[i]))

for i in range(1, MAX_GENERATIONS):
    print()
    print(f"======================= GENERASI {i} =======================")
    parent1, parent2 = selectParents(randomPopulation, 3)
    print(parent1, " ", parent2)
    print(Decode(parent1[:BIT_PER_GEN]), " ", Decode(parent1[BIT_PER_GEN:]), " ", Decode(parent2[:BIT_PER_GEN]), " ", Decode(parent2[BIT_PER_GEN:]))
    

    mutationBit = math.floor(MUTATION_RATE * CHROMOSOME_LENGTH)
    child1, child2 = singlePointCrossover(parent1, parent2, CROSSOVER_RATE)
    print(f"Stelah krosover : {child1} {child2}")
    print(f"sbelum mutasi : {child1}")
    print(f"sbelum mutasi : {child2}")
    
    selected1 = Mutation(child1, mutationBit)
    selected2 = Mutation(child2, mutationBit)
    # print(f"stelah mutasi : {selected1}")
    # print(f"stelah mutasi : {selected2}")

    # print(f"objective gen {i} {Objective(Decode(selected1[:8]), Decode(selected1[8:]))}, {Objective(Decode(selected2[:8]), Decode(selected2[8:]))}")

    # Hitung objective untuk semua individu
    objectiveValues = [Objective(Decode(ind[:BIT_PER_GEN]), Decode(ind[BIT_PER_GEN:])) for ind in randomPopulation]

    # Ganti dua terburuk dengan hasil mutasi
    worstIndices = sorted(
        range(len(objectiveValues)), 
        key=lambda k: objectiveValues[k], 
        reverse=True
    )
    randomPopulation[worstIndices[0]] = selected1
    randomPopulation[worstIndices[1]] = selected2

    # Cek kromosom terbaik sejauh ini
    currentBestIndex = min(range(len(objectiveValues)), key=lambda k: objectiveValues[k])
    currentBestObjective = objectiveValues[currentBestIndex]
    if currentBestObjective < bestObjective:
        bestGeneration = i
        bestObjective = currentBestObjective
        bestChromosome = randomPopulation[currentBestIndex]


x = Decode(bestChromosome[:BIT_PER_GEN])
y = Decode(bestChromosome[BIT_PER_GEN:])
print(f"\nKromosom terbaik selama seluruh generasi:")
print(f"{bestChromosome} -> x={x}, y={y}, Objective={bestObjective} pada generasi ke {bestGeneration}")
  
  
# print(Objective(Decode("00001"),Decode("01101")))


