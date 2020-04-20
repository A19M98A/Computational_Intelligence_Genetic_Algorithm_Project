import math
import random

aX = -3
bX = 3
aY = -3
bY = 3

ch_C = 1
ch_PS = 1
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
    print(Fitness(All_Ch[len(All_Ch) - 1]))

def Parent_Selection():
    if ch_PS == 1:
       Roulette_Wheel_Selection()
    elif ch_PS == 2:
       Stochastic_Universal_Sampling()
    elif ch_PS == 3:
       Tournament_Selection()
    elif ch_PS == 4:
       Rank_based_Selection()

def Roulette_Wheel_Selection():
    Sort()
    n = len(All_Ch)
    parents = list()
    l = random.randint(0, 6)
    for i in range(4):
        if l == 0:
            Parents.append(All_Ch[random.randint(0, int(n / 2))])
        elif l == 1:
            parents.append(All_Ch[random.randint(int(n / 2), int(3 / 4 * n))])
        elif l == 2:
            parents.append(All_Ch[random.randint(int(3 / 4 * n), int(7 / 8 * n))])
        elif l == 3:
            parents.append(All_Ch[random.randint(int(7 / 8 * n), int(15 / 16 * n))])
        elif l == 4:
            parents.append(All_Ch[random.randint(int(15 / 16 * n), int(31 / 32 * n))])
        elif l == 5:
            parents.append(All_Ch[random.randint(int(31 / 32 * n), n - 1)])
    for i in range(0, len(parents), 2):
        ch1, ch2 = Crossover(parents[i], parents[i + 1])
        All_Ch.append(ch1)
        All_Ch.append(ch2)

def Stochastic_Universal_Sampling():
    Sort()
    n = len(All_Ch)
    parents = list()
    for i in range(2):
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

def Tournament_Selection():
    Sort()
    n = len(All_Ch)
    parents = list()
    for i in range(2):
        a = list()
        a[1] = All_Ch[random.randint(0, n)]
        a[2] = All_Ch[random.randint(0, n)]
        a[3] = All_Ch[random.randint(0, n)]
        a[4] = All_Ch[random.randint(0, n)]
        a[5] = All_Ch[random.randint(0, n)]
        a[6] = All_Ch[random.randint(0, n)]
        _max = a[1]
        for p in a:
            if Fitness(p) > Fitness(_max):
                _max = p
        parents.append(_max)

    for i in range(0, len(parents), 2):
        ch1, ch2 = Crossover(parents[i], parents[i + 1])
        All_Ch.append(ch1)
        All_Ch.append(ch2)

def Rank_based_Selection():
    pass

def Crossover(_ch1, _ch2):
    if ch_C == 1:
        return One_Point(_ch1, _ch2)
    elif ch_C == 2:
        return N_3_Point(_ch1, _ch2)
    elif ch_C == 3:
        return Uniform(_ch1, _ch2)

def One_Point(_ch1, _ch2):
    x1 = '0b' + _ch1.Var_X_B()[:3] + _ch2.Var_X_B()[3:]
    y1 = '0b' + _ch1.Var_Y_B()[:3] + _ch2.Var_Y_B()[3:]
    x2 = '0b' + _ch2.Var_X_B()[:3] + _ch1.Var_X_B()[3:]
    y2 = '0b' + _ch2.Var_Y_B()[:3] + _ch1.Var_Y_B()[3:]
    ch1 = Chromosome(int(x1, 2), int(y1, 2))
    ch2 = Chromosome(int(x2, 2), int(y2, 2))
    return ch1, ch2

def N_3_Point(_ch1, _ch2):
    x1 = '0b' + _ch1.Var_X_B()[:5] + _ch2.Var_X_B()[1:2] + _ch1.Var_X_B()[4:]
    y1 = '0b' + _ch1.Var_Y_B()[:5] + _ch2.Var_Y_B()[1:2] + _ch1.Var_Y_B()[4:]
    x2 = '0b' + _ch2.Var_X_B()[:5] + _ch1.Var_X_B()[1:2] + _ch2.Var_X_B()[4:]
    y2 = '0b' + _ch2.Var_Y_B()[:5] + _ch1.Var_Y_B()[1:2] + _ch2.Var_Y_B()[4:]
    ch1 = Chromosome(int(x1, 2), int(y1, 2))
    ch2 = Chromosome(int(x2, 2), int(y2, 2))
    return ch1, ch2

def Uniform(_ch1, _ch2):
    x1 = _ch1.Var_X_B()
    y1 = _ch1.Var_Y_B()
    x2 = _ch2.Var_X_B()
    y2 = _ch1.Var_Y_B()
    for i in range(3):
        x = random.randint(0, 6)
        x1[x], x2[x] = x2[x], x1[x]
        y1[x], y2[x] = y2[x], y1[x]
    x1 = '0b' + x1
    x2 = '0b' + x2
    y1 = '0b' + y1
    y2 = '0b' + y2
    ch1 = Chromosome(int(x1, 2), int(y1, 2))
    ch2 = Chromosome(int(x2, 2), int(y2, 2))
    return ch1, ch2

def SurvivorSelection(_ch1, _ch2):
    pass

for i in range(100):
    All_Ch.append(Chromosome(random.randint(0, 64), random.randint(0, 64)))

while 1:
    Parent_Selection()
    print("-----------")
    #Ans = input() 
