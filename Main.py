import math
import random

aX = -3
bX = 3
aY = -3
bY = 3

All_Ch = list()
Parents = list()

class Chromosome:
    
    def __init__(self, var_X, var_Y):
        self.var_X = bin(var_X)
        self.var_Y = bin(var_Y)
    
    def Var_X(self):
        return int(self.var_X, 2)

    def Var_Y(self):
        return int(self.var_Y, 2)

    def Var_X_B(self):
        return str(self.var_X)[2:].rjust(6,'0')

    def Var_Y_B(self):
        return str(self.var_Y)[2:].rjust(6,'0')


def Fitness(_chromosome):
    X = _chromosome.Var_X() * ((bX - aX) / 63) + aX
    Y = _chromosome.Var_Y() * ((bY - aY) / 63) + aY
    ret = -20 * math.exp(-0.2 * pow((0.5 * (X * X + Y * Y)), 0.5)) - math.exp(0.5 * (math.cos(2 * X * math.pi) + math.cos(2 * Y * math.pi))) + 2.7 + 20
    return ret

def Sort():
    for i in range(len(All_Ch)):
        for j in range(i + 1, len(All_Ch)):
            if Fitness(All_Ch[i]) > Fitness(All_Ch[j]):
                All_Ch[i], All_Ch[j] = All_Ch[j], All_Ch[i]

def ParentSelection():
    Sort()
    n = len(All_Ch)
    parents = list()
    for i in range(10):
        Parents.append(All_Ch[random.randint(0, int(n / 2))])
        parents.append(All_Ch[random.randint(int(n / 2), int(3 / 4 * n))])
        parents.append(All_Ch[random.randint(int(3 / 4 * n), int(7 / 8 * n))])
        parents.append(All_Ch[random.randint(int(7 / 8 * n), int(15 / 16 * n))])
        parents.append(All_Ch[random.randint(int(15 / 16 * n), int(31 / 32 * n))])
        parents.append(All_Ch[random.randint(int(31 / 32 * n), n - 1)])
    for i in range(0, len(parents), 2):
        ch1, ch2 = Crossover(parents[i], parents[i + 1])
        All_Ch.append(ch1)
        All_Ch.append(ch2)

def Crossover(_ch1, _ch2):
    x1 = '0b' + _ch1.Var_X_B()[:3] + _ch2.Var_X_B()[3:]
    y1 = '0b' + _ch1.Var_Y_B()[:3] + _ch2.Var_Y_B()[3:]
    x2 = '0b' + _ch1.Var_X_B()[3:] + _ch2.Var_X_B()[:3]
    y2 = '0b' + _ch1.Var_Y_B()[3:] + _ch2.Var_Y_B()[:3]
    ch1 = Chromosome(int(x1, 2), int(y1, 2))
    ch2 = Chromosome(int(x2, 2), int(y2, 2))
    return ch1, ch2

def SurvivorSelection(_ch1, _ch2):
    pass

for i in range(1000):
    All_Ch.append(Chromosome(random.randint(0, 64), random.randint(0, 64)))

while 1:
    ParentSelection()
    print("-----------")
    #Ans = input() 
