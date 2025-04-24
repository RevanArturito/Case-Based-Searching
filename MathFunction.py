import math
import random
from typing import List, Tuple
from pair import *

# TAHAP 1 

# Mengubah binary ke decimal and vice versa
def Encode(value: int) -> str:
    shifted = value + 10  
    return format(shifted, '05b')
def Decode(binary_str: str) -> int:
    shifted = int(binary_str, 2)
    return shifted - 10

# TAHAP 1 

# Mengubah binary ke decimal and vice versa
def Encode(value: int) -> str:
    shifted = value + 10  
    return format(shifted, '05b')
def Decode(binary_str: str) -> int:
    shifted = int(binary_str, 2)
    return shifted - 10

# Fungsi untuk menghitung nilai Objective
def ObjectiveFunction(x1, x2 : int) -> float:
    result = -(math.sin(x1)*math.cos(x2)*math.tan(x1+x2) + (0.75)*math.exp(1-math.sqrt(x1**2)))
    return round(result,3)

# Fungsi untuk me-generate random integer dengan interval [-10,10]
def RandomVal(n : int) -> List[Pair]:
    pairs = []
    for _ in range(n):
        x1 = random.randint(-10,10)
        x2 = random.randint(-10,10)
        pairs.append(Pair(x1,x2))
    return pairs

# Fungsi untuk menghitung nilai Fitness
def FitnessFunction(x1, x2 : int, sum : float) -> float:
    return  round(1 / (1 + ObjectiveFunction(x1,x2)) ,3)
    return  round(1 / (1 + ObjectiveFunction(x1,x2)) ,3)

# Fungsi untuk menghitung nilai sum atau jumla dari keseluruhan nilai Objective
def SumPairValue(pair : List[Pair]) -> float:
    sum : float = 0.0
    for p in pair:
        sum += ObjectiveFunction(p.x1, p.x2)
    return round(sum,3)

# Fungsi untuk me-convert bilangan integer menjadi 5 digit binary
def FitnessValues(pairs: List[Pair]) -> List[float]:
    obj_values = [ObjectiveFunction(p.x1, p.x2) for p in pairs]
    min_val = min(obj_values)
    epsilon = 1e-6  # Biar ngga enol
    epsilon = 1e-6  # Biar ngga enol

    # Shift jika ada nilai negatif
    if min_val < 0:
        shifted_values = [v + abs(min_val) + epsilon for v in obj_values]
    else:
        shifted_values = obj_values

    # totalnya juga dari nilai yang sudah di shift
    total = sum(shifted_values)

    fitness = [round(v / total, 3) for v in shifted_values]
    return fitness

# Fungsi untuk menghitung nilai kumulatif berdasarkan nilai Fitness yang ada
def CumFitness(fitness_list: List[float]) -> List[float]:
    cumulative = []
    total = 0.0
    for cf in fitness_list:
        total += cf
        cumulative.append(round(total, 3))
    return cumulative

# Fungsi untuk membuat Interval berdasarkan nilai cumulative yang ada
def IntervalRange(batasKiri, cumulative: List[float]) -> List[str]:
    interval = []
    for cum in cumulative:
        batasKanan = cum
        interval.append(f"{batasKiri:.3f} – {batasKanan:.3f}")
        # Mastiin kalau batas kiri biar ga lebih dari 1
        if batasKanan + 0.001 > 1:
            batasKiri = batasKiri
        else:
            batasKiri = batasKanan + 0.001
    return interval



# TAHAP 2
def parseInterval(interval_str):
    parts = interval_str.replace("–", "-").split("-")
    lower = float(parts[0].strip())
    upper = float(parts[1].strip())
    return lower, upper

def selectParent(intervals, fitnesses, pairs):
    selected_indices = []
    used_indices = set()

    while len(selected_indices) < 2:
        r = round(random.uniform(0, 1), 3)
        for i, interval in enumerate(intervals):
            if i in used_indices or fitnesses[i] == 0:
                continue
            lower, upper = parseInterval(interval)
            if lower <= r <= upper:
                kromosom1, kromosom2 = Encode(pairs[i].x1), Encode(pairs[i].x2)
                kromosom = kromosom1 + kromosom2
                selected_indices.append((i, r, interval, kromosom))
                used_indices.add(i)
                break

    return selected_indices

# TAHAP 3
def crossover(parents: List[tuple]) -> List[Tuple[str, int, int]]:
    parent1 = parents[0][3]  # kromosom yang diambil dari tahap kedua (kromosom lama)
    parent2 = parents[1][3]

    crossover = 4  # 4 angka didepan bit yang akan di crossover antar parent
    print(f"Crossover: {crossover}")

    # penukaran bit terdepan dengan bit sisanya
    child1 = parent1[:crossover] + parent2[crossover:]
    child2 = parent2[:crossover] + parent1[crossover:]

    # Decode mengubah nilai biner menjadi integer
    child1_x1 = Decode(child1[:5])
    child1_x2 = Decode(child1[5:])
    child2_x1 = Decode(child2[:5])
    child2_x2 = Decode(child2[5:])

    return [
        (child1, child1_x1, child1_x2),
        (child2, child2_x1, child2_x2)
    ]
