import math
import random
from typing import List, Tuple
from pair import *

# TAHAP 1 

# Mengubah binary ke decimal and vice versa
def Encode(value: int) -> str:
    shifted = value + 10  
    return format(shifted, '05b')
def Decode(binary: str) -> int:
    shifted = int(binary, 2)
    return shifted - 10


# Fungsi untuk menghitung nilai Objective
def ObjectiveFunction(x1, x2 : int) -> float:
    result = -(math.sin(x1)*math.cos(x2)*math.tan(x1+x2) + (0.75)*math.exp(1-math.sqrt(x1**2)))
    return abs(round(result,3))

def CheckObjectiveFunction(x1, x2 : int) -> float:
    result = -(math.sin(x1)*math.cos(x2)*math.tan(x1+x2) + (0.75)*math.exp(1-math.sqrt(x1**2)))
    return result


# Fungsi untuk me-generate random integer dengan interval [-10,10]
def RandomVal(n : int) -> List[Pair]:
    pairs = []
    for _ in range(n):
        x1 = random.randint(-10,10)
        x2 = random.randint(-10,10)
        pairs.append(Pair(x1,x2))
    return pairs

# Fungsi untuk menghitung nilai Fitness
def FitnessFunction(x1, x2: int, sum: float) -> float:
    fitness = 1 / (1 + ObjectiveFunction(x1, x2))
    return round(fitness / sum, 3)

def CheckFitnessFunction(x1, x2: int) -> float:
    fitness = 1 / (1 + CheckObjectiveFunction(x1, x2))
    return round(fitness, 3)

# Fungsi untuk menghitung nilai sum atau jumla dari keseluruhan nilai Objective
def SumTotalFitness(pairs: List[Pair]) -> float:
    total = 0.0
    for p in pairs:
        total += 1 / (1 + ObjectiveFunction(p.x1, p.x2))
    return total

# Fungsi untuk menghitung nilai kumulatif berdasarkan nilai Fitness yang ada
def CumFitness(fitnessList: List[float]) -> List[float]:
    cumulative = []
    total = 0.0
    for cf in fitnessList:
        total += cf
        cumulative.append(round(total, 3))
    return cumulative

# Fungsi untuk membuat Interval berdasarkan nilai cumulative yang ada
def IntervalRange(batasKiri, cumulative: List[float]) -> List[str]:
    interval = []
    for cum in cumulative:
        if cum >= 1:
            batasKanan = 1
        batasKanan = cum
        interval.append(f"{batasKiri:.3f} – {batasKanan:.3f}")
        # Mastiin kalau batas kiri biar ga lebih dari 1
        if batasKanan + 0.001 > 1:
            batasKiri = batasKiri
        else:
            batasKiri = batasKanan + 0.001
    return interval


# TAHAP 2
def parseInterval(interval):
    parts = interval.replace("–", "-").split("-")
    lower = float(parts[0].strip())
    upper = float(parts[1].strip())
    return lower, upper

def selectParent(intervals, fitnesses, pairs):
    selectedIndices = []
    usedIndices = set()

    while len(selectedIndices) < 2:
        r = round(random.uniform(0, 1), 3)
        for i, interval in enumerate(intervals):
            if i in usedIndices or fitnesses[i] == 0:
                continue
            lower, upper = parseInterval(interval)
            if lower <= r <= upper:
                kromosom1, kromosom2 = Encode(pairs[i].x1), Encode(pairs[i].x2)
                kromosom = kromosom1 + kromosom2
                selectedIndices.append((i, r, interval, kromosom))
                usedIndices.add(i)
                break

    return selectedIndices

# TAHAP 3
def crossover(parents: List[tuple], crossoverRate: float) -> List[Tuple[str, int, int]]:
    # Cek apakah crossover dilakukan berdasarkan crossoverRate
    if random.random() > crossoverRate:
        print()
        print("Crossover tidak terjadi. Nilai random lebih besar dari Crossover Rate")
        # Kembalikan parent tanpa perubahan
        return [
            (parents[0][3], Decode(parents[0][3][:5]), Decode(parents[0][3][5:])),
            (parents[1][3], Decode(parents[1][3][:5]), Decode(parents[1][3][5:]))
        ]

    parent1 = parents[0][3]
    parent2 = parents[1][3]

    for attempt in range(10):
        crossoverPoint = random.randint(1, 9)
        print()
        print(f"Crossover point: {crossoverPoint}")
        
        child1 = parent1[:crossoverPoint] + parent2[crossoverPoint:]
        child2 = parent2[:crossoverPoint] + parent1[crossoverPoint:]

        try:
            child1X1, child1X2 = Decode(child1[:5]), Decode(child1[5:])
            child2X1, child2X2 = Decode(child2[:5]), Decode(child2[5:])
        except ValueError:
            continue

        if all(-10 <= x <= 10 for x in [child1X1, child1X2, child2X1, child2X2]):
            return [
                (child1, child1X1, child1X2),
                (child2, child2X1, child2X2)
            ]

    # Jika gagal 10 kali, pakai crossover titik tengah
    print("Crossover gagal setelah 10 percobaan, pakai titik tengah.")
    midpoint = 6
    child1 = parent1[:midpoint] + parent2[midpoint:]
    child2 = parent2[:midpoint] + parent1[midpoint:]
    return [
        (child1, Decode(child1[:5]), Decode(child1[5:])),
        (child2, Decode(child2[:5]), Decode(child2[5:]))
    ]


    
# TAHAP 4

def mutasi(children, mutationRate):
    hasilMutasi = []
    i = 0
    print()
    for kromosom in children:
        kromosomAsli = kromosom[0]  # Kromosom hasil crossover
        kromosomBaru = ""

        # Proses mutasi bit per bit
        for bit in kromosomAsli:
            if random.random() < mutationRate:
                bit = '1' if bit == '0' else '0'
            kromosomBaru += bit

        # Decode hasil mutasi
        x1Mutasi = Decode(kromosomBaru[:5])
        x2Mutasi = Decode(kromosomBaru[5:])

        if -10 <= x1Mutasi <= 10 and -10 <= x2Mutasi <= 10:
            print(f"[Mutasi {i+1}] BERHASIL -> Kromosom: {kromosomBaru}   -> x1: {x1Mutasi}, x2: {x2Mutasi}")
            hasilMutasi.append((kromosomBaru, x1Mutasi, x2Mutasi))
        else:
            print(f"[Mutasi {i+1}] GAGAL    -> Diluar batas Interval  -> x1: {x1Mutasi}, x2: {x2Mutasi}")
            x1Asli = Decode(kromosomAsli[:5])
            x2Asli = Decode(kromosomAsli[5:])
            hasilMutasi.append((kromosomAsli, x1Asli, x2Asli))
        i+=1

    return hasilMutasi

