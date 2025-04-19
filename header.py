# Header
def HeaderUp1():
    print("-------------------------------------------")

def HeaderUp2():
    print("------------------------------------------------------------------")
    
def HeaderDown():
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    
def ObjectiveHeader():
    HeaderUp1()
    print(f"|{'x1':^7} | {'x2':^7} | {'Objective':^20} |")
    HeaderUp1()

def Tahap1Header():
    HeaderUp2()
    print(f"|{'x1':^7} | {'x2':^7} | {'Objective':^20} | {'Fitness':^20} |")
    HeaderUp2()