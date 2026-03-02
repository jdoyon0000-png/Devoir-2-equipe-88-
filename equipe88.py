import math

from bissection import Bissection
from pointfixe import Pointfixe




def F(Q):
    return math.e**Q + Q/2 -5

iterartion_biss = Bissection(F,1,2,0.00005,15)

def g1(Q):
    return math.log(-Q / 2 + 5)
iterations_g1 = Pointfixe(g1, 1.0, 1e-8, 150)

def g2(Q):
    return 10 - 2 * math.exp(Q)
iterations_g2 = Pointfixe(g2, 1.0, 1e-8, 5)

def gN(Q):
    fq = math.exp(Q) + (Q / 2) - 5

    drvfq = math.exp(Q) + (1 / 2)

    return Q - (fq / drvfq)

iterations_g3 = Pointfixe(gN, 1.0, 1e-8, 150)


def gsteffa1(Q):
    def g1(x):
        return math.log((-x / 2) + 5)
    g1Q = g1(Q)
    g1g1Q = g1(g1Q)
    
    a = (g1Q - Q)**2
    b = g1g1Q - (2 * g1Q) + Q
    
    return Q - (a / b)

iterations_steffa1 = Pointfixe(gsteffa1, 1.0, 1e-8, 150)




def gsteffa2(Q):

    def g2(x):
        return 10 - 2 * math.exp(x)
    
    g2Q = g2(Q)
    g2g2Q = g2(g2Q)

    a = (g2Q - Q)**2
    b = g2g2Q - (2 * g2Q) + Q
    
    return Q - (a / b)

iterations_steffa2 = Pointfixe(gsteffa2, 1.0, 1e-8, 150)



def gsteffaN(Q):

    def gN(x):
        fx = math.exp(x) + (x / 2) - 5
        drvfx = math.exp(x) + 0.5
        return x - (fx / drvfx)
    
    qn_1 = gN(Q)
    qn_2 = gN(qn_1)
    
    return Q - ((qn_1 - Q)**2 / (qn_2 - 2 * qn_1 + Q))

iterations_steffaN = Pointfixe(gsteffaN, 1.0, 1e-8, 150)
