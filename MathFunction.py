import math

def Fitness(x1, x2 : int) -> float:
    return  -(math.sin(x1)*math.cos(x2)*math.tan(x1+x2) + (0.75)*math.exp(1-math.sqrt(x1**2)))