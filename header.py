# Header
from typing import *
from pair import *
from MathFunction import *


def HeaderUp1():
    print("+--------+---------+----------------------+")

def HeaderUp2():
    print("+--------+---------+----------------------+----------------------+")
    
def HeaderUp3():
    print("+--------+---------+----------------------+----------------------+----------------------+----------------------+")
    
def HeaderUp4():
    print("+---------------------+----------------------+----------------------+----------------------+")
    
def HeaderDown():
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    
def ObjectiveHeader():
    HeaderUp1()
    print(f"|{'x1':^7} | {'x2':^7} | {'Objective':^20} |")
    HeaderUp1()

def FitnessHeader():
    HeaderUp2()
    print(f"|{'x1':^7} | {'x2':^7} | {'Objective':^20} | {'Fitness':^20} |")
    HeaderUp2()

def Tahap1Header():
    HeaderUp3()
    print(f"|{'x1':^7} | {'x2':^7} | {'Objective':^20} | {'Fitness':^20} | {'Cumulative':^20} | {'Interval':^20} |")
    HeaderUp3()
    
def Tahap2Header():
    HeaderUp4()
    print(f"|{'Kromosom Lama':^20} | {'Random R[k]':^20} | {'Interval':^20} | {'Kromosom Baru':^20} |")
    HeaderUp4()
    
def printObjective(pairs: List[Pair], o: List[float], n:int) -> None:
    ObjectiveHeader()
    for i in range(n):
        print(f"|{pairs[i].x1:^7} | {pairs[i].x2:^7} | {o[i]:^20} |")
    HeaderUp1()
    
def printSumValue(pairs: List[Pair]) -> None:
    print()
    print(f"Sum Value:  {SumPairValue(pairs)}")    
    print()
    
def printFitness(pairs: List[Pair], o: List[float], f: List[float], n:int) -> None:
    FitnessHeader()
    for i in range(n):
        print(f"|{pairs[i].x1:^7} | {pairs[i].x2:^7} | {o[i]:^20} | {f[i]:^20} |")
    HeaderUp2()
    
def printTahap1(pairs: List[Pair], o: List[float], f: List[float], cum: List[float],interval: List[str], n:int) -> None:
    Tahap1Header()
    for i in range(n):
        print(f"|{pairs[i].x1:^7} | {pairs[i].x2:^7} | {o[i]:^20} | {f[i]:^20} | {cum[i]:^20} | {interval[i]:^20} | ")
    HeaderUp3()
    
    
def printTahap2(parent) -> None:
    Tahap2Header()
    for idx, r, interval, kromosom in parent:
        print(f"|{idx + 1:^20} | {r:^20} | {interval:^20} | {f'{idx+1} ({kromosom})':^20} | {Decode(kromosom[:5])} {Decode(kromosom[5:])}")
    HeaderUp4()
    

    

    