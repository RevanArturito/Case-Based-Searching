import math
import random
from typing import List
from pair import *

def Fitness(x1, x2 : int) -> float:
    return  -(math.sin(x1)*math.cos(x2)*math.tan(x1+x2) + (0.75)*math.exp(1-math.sqrt(x1**2)))

def RandomVal(n : int) -> List[Pair]:
    pairs = []
    i = 0
    for i in range(n):
        x1 = random.randint(-10,10)
        x2 = random.randint(-10,10)
        pairs.append(Pair(x1,x2))
    return pairs