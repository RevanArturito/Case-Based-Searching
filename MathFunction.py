import math
import random
from typing import List
from pair import *

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
    return  round(ObjectiveFunction(x1,x2) / sum,3)

# Fungsi untuk menghitung nilai sum atau jumla dari keseluruhan nilai Objective
def SumPairValue(pair : List[Pair]) -> float:
    sum : float = 0.0
    for p in pair:
        sum += ObjectiveFunction(p.x1, p.x2)
    return round(sum,3)

# Fungsi untuk me-convert bilangan integer menjadi 5 digit binary
def BinaryConvert(pairs: List[Pair]) -> List[Pair]:
    binaries = []
    for pair in pairs:
        x1 = format(pair.x1, 'b') if pair.x1 >= 0 else "-" + format(abs(pair.x1), 'b')
        x2 = format(pair.x2, 'b') if pair.x2 >= 0 else "-" + format(abs(pair.x2), 'b')        
        binaries.append(Pair(x1, x2))
    return binaries