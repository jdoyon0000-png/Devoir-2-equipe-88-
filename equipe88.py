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
    g1_Q = g1(Q)
    g1_g1_Q = g1(g1_Q)
    
    numerateur = (g1_Q - Q)**2
    denominateur = g1_g1_Q - (2 * g1_Q) + Q
    
    return Q - (numerateur / denominateur)

iterations_steffa1 = Pointfixe(gsteff1, 1.0, 1e-8, 150)




def gsteffa2(Q):

    def g2(x):
        return 10 - 2 * math.exp(x)
    
    val_g2 = g2(Q)
    val_g2_g2 = g2(val_g2)

    numerateur = (val_g2 - Q)**2
    denominateur = val_g2_g2 - (2 * val_g2) + Q
    
    return Q - (numerateur / denominateur)

iterations_steffa2 = Pointfixe(gsteff2, 1.0, 1e-8, 150)



def gsteffaN(Q):

    def gN(x):
        fx = math.exp(x) + (x / 2) - 5
        drvfx = math.exp(x) + 0.5
        return x - (fx / drvfx)
    
    qn_1 = gN(Q)
    qn_2 = gN(qn_1)
    
    return Q - ((qn_1 - Q)**2 / (qn_2 - 2 * qn_1 + Q))

iterations_steffa2 = Pointfixe(gsteffaN, 1.0, 1e-8, 150)
