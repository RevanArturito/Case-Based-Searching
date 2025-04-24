from MathFunction import *
from pair import *
from typing import List
from header import *

# 3 Pasang data 
DATA_COUNT = 3

# TAHAP 1 DATA
pairs: List[Pair] = RandomVal(DATA_COUNT)
pairsBinary: List[Pair] = []
Objective: List[float] = []
fitnessList: List[float] = []
CumFitnessList: List[float] = []
Interval: List[str] = []

# Menampilkan data yang telah di generate
print("----------------------------TAHAP 1 -----------------------------")
print()

# Menghitung nilai objective berdasarkan nilai x1 dan x2
# Menghitung nilai objective berdasarkan nilai x1 dan x2
for i in range(DATA_COUNT):
    o = ObjectiveFunction(pairs[i].x1, pairs[i].x2)
    Objective.append(o)

# Menampilkan nilai Fitness[i] berdasarkan data yang ada
for i in range(DATA_COUNT):
    f = FitnessFunction(pairs[i].x1, pairs[i].x2, SumPairValue(pairs))
    fitnessList.append(f)
printFitness(pairs, Objective, fitnessList, DATA_COUNT)


# Jika ada nilai negatif pada Objective, maka nilai akan di-shift
# Kemungkinan besar ada nilai fitness pada akhirnya akan ada yg 0,
# Soalnya yang tadinya bernilai negatif (Individu terburuk) memiliki nilai Fitness 0
print()
if Objective [0] < 0 or Objective [1] < 0 or Objective [2] < 0:
    fitnessList = FitnessValues(pairs)
    print("Terdapat nilai negatif pada Objective.\nMaka nilai Objective akan di-shift")

# Nilai kumulatif dari nilai Fitness
CumFitnessList = CumFitness(fitnessList)
# Batas bawah dan batas atas (Interval)
Interval = IntervalRange(0, CumFitnessList)
# Menampilkan data TAHAP 1
printTahap1(pairs, Objective, fitnessList, CumFitnessList, Interval, DATA_COUNT)





# Menampilkan data yang telah di generate
print()
print()
print("----------------------------TAHAP 2 -----------------------------")
print()
parents = selectParent(Interval, fitnessList, pairs)
printTahap2(parents)


print()
print()
print("----------------------------TAHAP 3 -----------------------------")
print()

children = crossover(parents)
for idx, (kromosom_baru, x1, x2) in enumerate(children):
    print(f"Child {idx + 1} : {kromosom_baru} -> x1: {x1}, x2: {x2}")



    