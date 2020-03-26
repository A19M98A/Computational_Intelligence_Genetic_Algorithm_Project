import math

class Chromosome:
    
    def __init__(self, var_X, var_Y):
        self.var_X = bin(var_X)
        self.var_Y = bin(var_Y)
    
    def Var_X(self):
        return int(self.var_X, 2)

    def Var_Y(self):
        return int(self.var_Y, 2)

    def Var_X_B(self):
        return str(self.var_X)[2:]

    def Var_Y_B(self):
        return str(self.var_Y)[2:]


def Fitness(_chromosome):
    ret = -20 * math.exp(-0.2 * pow((0.5 * (_chromosome.Var_X() * _chromosome.Var_X() + _chromosome.Var_Y() * _chromosome.Var_Y())), 0.5)) - math.exp(0.5 * (math.cos(2 * _chromosome.Var_X() * math.pi) + math.cos(2 * _chromosome.Var_Y() * math.pi))) + 2.7 + 20
    return ret

def ParentSelection(_ch1, _ch2):
    pass

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

while 1:
    print('Parent selection [0]')
    print('Crossover [1]')
    print('Survivor selection [2]')
    print('(1/0).(1/0).(1/0) ?')
    chromesimple = Chromosome(10, 1)
    chromesimple2 = Chromosome(1, 5)
    # print(chromesimple.Var_Y())
    # print(Fitness(chromesimple))
    ch1, ch2 = Crossover(chromesimple, chromesimple2)
    print(ch1.Var_X(), ch1.Var_Y())
    print(ch2.Var_X(), ch2.Var_Y())
    Ans = input() 
