from MathFunction import *
from pair import *
from typing import List
from header import *

# 3 Pasang data 
DATA_COUNT = 3
pairs: List[Pair] = RandomVal(DATA_COUNT)

pairsBinary: List[Pair] = []

Objective: List[float] = []

# Menampilkan data yang telah di generate
print("----------------------------TAHAP 1 -----------------------------")
print()

# Menampilkan nilai dari Fungsi Objective berdasarkan data yang ada
ObjectiveHeader()
for i in range(DATA_COUNT):
    o = ObjectiveFunction(pairs[i].x1, pairs[i].x2)
    print(f"|{pairs[i].x1:^7} | {pairs[i].x2:^7} | {o:^20} |")
    Objective.append(o)
HeaderUp1()


# Menampilkan jumlah atau sum dari nilai Fungsi Objective
print()
print(f"Sum Value:  {SumPairValue(pairs)}")    
print()

# Menampilkan nilai Fitness[i] berdasarkan data yang ada
Tahap1Header()
for i in range(DATA_COUNT):
    f = FitnessFunction(pairs[i].x1, pairs[i].x2, SumPairValue(pairs))
    print(f"|{pairs[i].x1:^7} | {pairs[i].x2:^7} | {Objective[i]:^20} | {f:^20} |")
HeaderUp2()


# Jika ada nilai negatif pada Objective, maka nilai akan di-shift
# Kemungkinan besar ada nilai fitness pada akhirnya akan ada yg 0,
# Soalnya yang tadinya bernilai negatif (Individu terburuk) memiliki nilai Fitness 0
print()
if Objective [0] < 0 or Objective [1] < 0 or Objective [2] < 0:
    fitnessList = FitnessValues(pairs)
    print("Terdapat nilai negatif pada Objective.\nMaka nilai Objective akan di-shift")
    Tahap1Header()
    for i in range(DATA_COUNT):
        print(f"|{pairs[i].x1:^7} | {pairs[i].x2:^7} | {Objective[i]:^20} | {fitnessList[i]:^20} | ")
    HeaderUp2()

    
    
# pairsBinary = BinaryConvert(pairs)
# print()
# print("Dalam Binary:")
# for pair in pairsBinary:
#     # Menampilkan x1 dan x2 dalam bentuk binary
#     print(f"{pair.x1}, {pair.x2}")