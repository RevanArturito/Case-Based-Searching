from MathFunction import *
from pair import *
from typing import List

# 3 Pasang data random
pairs: List[Pair] = RandomVal(3)

# Menampilkan data yang telah di generate
for pair in pairs:
    # Menampilkan nilai Fitness[i] berdasarkan data yang ada
    print(f"f({pair.x1}, {pair.x2}) = {Fitness(pair.x1, pair.x2)}")