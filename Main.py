import math

class Chromosome:
    
    def __init__(self, var_X, var_Y):
        self.var_X = bin(var_X)
        self.var_Y = bin(var_Y)
    
    def Var_X(self):
        return int(self.var_X, 2)

    def Var_Y(self):
        return int(self.var_Y, 2)


def Fitness(_chromosome):
    ret = -20 * math.exp(-0.2 * pow((0.5 * (_chromosome.Var_X() * _chromosome.Var_X() + _chromosome.Var_Y() * _chromosome.Var_Y())), 0.5)) - math.exp(0.5 * (math.cos(2 * _chromosome.Var_X() * math.pi) + math.cos(2 * _chromosome.Var_Y() * math.pi))) + 2.7 + 20
    return ret

def ParentSelection(_ch1, _ch2):
    pass

def Crossover(_ch1, _ch2):
    pass

zsh:1: command not found: :wq
    pass

while 1:
    print('Parent selection [0]')
    print('Crossover [1]')
    print('Survivor selection [2]')
    print('(1/0).(1/0).(1/0) ?')
    chromesimple = Chromosome(10, 10)
    # print(chromesimple.Var_Y())
    print(Fitness(chromesimple))
    Ans = input() 
