from MathFunction import *
from pair import *
from typing import List

# 3 Pasang data random
pairs: List[Pair] = RandomVal(3)

pairsBinary: List[Pair]

# Menampilkan data yang telah di generate
for pair in pairs:
    # Menampilkan nilai dari Fungsi Objective berdasarkan data yang ada
    print(f"Fungsi Objective({pair.x1}, {pair.x2}) = {ObjectiveFunction(pair.x1, pair.x2)}")
print()
# Menampilkan jumlah atau sum dari nilai Fungsi Objective
print(f"Sum Value:  {SumPairValue(pairs)}")    
print()
for pair in pairs:
    # Menampilkan nilai Fitness[i] berdasarkan data yang ada
    print(f"Nilai Fitness({pair.x1}, {pair.x2}) = {FitnessFunction(pair.x1, pair.x2, SumPairValue(pairs))}")
    
    
pairsBinary = BinaryConvert(pairs)
print()
print("Dalam Binary:")
for pair in pairsBinary:
    # Menampilkan x1 dan x2 dalam bentuk binary
    print(f"{pair.x1}, {pair.x2}")