from MathFunction import *
from pair import *
from typing import List
from header import *

# 3 Pasang data
DATA_COUNT = 3
GENERATIONS = 1000
CROSSOVER_RATE = 0.7
MUTATION_RATE = 0.1

# Fungsi untuk menginisialisasi generasi awal
def init_population() -> List[Pair]:
    return RandomVal(DATA_COUNT)

# Fungsi GA utama
def genetic_algorithm():
    population = init_population()
    bestX1 = None
    bestX2 = None
    bestObjectiveValue = 0  
    bestGeneration = -1  

    for generation in range(GENERATIONS):
        print(f"\n===================================== Generation {generation + 1} =====================================")

        # TAHAP 1 - Evaluasi
        fitnessList: List[float] = [FitnessFunction(p.x1, p.x2, SumTotalFitness(population)) for p in population]
        CumFitnessList: List[float] = CumFitness(fitnessList)
        Interval: List[str] = IntervalRange(0, CumFitnessList)

        # TAHAP 2 - Seleksi
        parents = selectParent(Interval, fitnessList, population)
        printTahap2(parents)

        # TAHAP 3 - Crossover
        children = crossover(parents, CROSSOVER_RATE)
        printCrossOver(children)

        # TAHAP 4 - Mutasi menggunakan fungsi mutasi baru
        mutation = mutasi(children, MUTATION_RATE)
        print()
        printMutation(mutation)

        # Pengecekan nilai terbaik setelah semua anak dicek
        for krom, x1, x2 in mutation:
            objectiveValue = CheckObjectiveFunction(x1, x2)
            if objectiveValue < bestObjectiveValue:
                bestObjectiveValue = objectiveValue
                bestX1 = x1
                bestX2 = x2
                bestGeneration = generation + 1

        # Populasi baru dari hasil mutasi
        population = [Pair(x1, x2) for _, x1, x2 in mutation]
        
        

    print("\n======================================= HASIL AKHIR =======================================")
    print(f"Nilai x1 Terbaik: {bestX1}")
    print(f"Nilai x2 Terbaik: {bestX2}")
    print(f"Nilai Objective Terbaik: {bestObjectiveValue}")
    print(f"Ditemukan pada Generasi ke: {bestGeneration}")


# Jalankan GA
genetic_algorithm()