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

# Menampilkan nilai dari Fungsi Objective berdasarkan data yang ada
for i in range(DATA_COUNT):
    o = ObjectiveFunction(pairs[i].x1, pairs[i].x2)
    Objective.append(o)
printObjective(pairs, Objective, DATA_COUNT)

# Menampilkan jumlah atau sum dari nilai Fungsi Objective
printSumValue(pairs)

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
    for i in range(DATA_COUNT):
        fitnessList.append(f)
    printFitness(pairs, Objective, fitnessList, DATA_COUNT)

# Nilai kumulatif dari nilai Fitness
CumFitnessList = CumFitness(fitnessList)
# Batas bawah dan batas atas (Interval)
Interval = IntervalRange(0, CumFitnessList)
# Menampilkan data TAHAP 1
printTahap1(pairs, Objective, fitnessList, CumFitnessList, Interval, DATA_COUNT)
    
    

# pairsBinary = BinaryConvert(pairs)
# print()
# print("Dalam Binary:")
# for pair in pairsBinary:
#     # Menampilkan x1 dan x2 dalam bentuk binary
#     print(f"{pair.x1}, {pair.x2}")