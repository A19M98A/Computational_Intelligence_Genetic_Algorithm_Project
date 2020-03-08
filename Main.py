import math

class Chromosome:
    pass

def Fitness(x, y):
    ret = -20 * math.exp(-0.2 * pow((0.5 * (x * x + y * y)), 0.5)) - math.exp(0.5 * (math.cos(2 * x * math.pi) + math.cos(2 * y * math.pi))) + 2.7 + 20
    return ret

while 1:
    print('Parent selection [0]')
    print('Crossover [1]')
    print('Survivor selection [2]')
    print('(1/0).(1/0).(1/0) ?')
    print(Fitness(1, 2))
    Ans = input() 
