import math

from bissection import Bissection
from pointfixe import Pointfixe



#c)
def F(Q):
    return math.e**Q + Q/2 -5

#print(Bissection(F,1,2,0.00005,15))

def g1(Q):
    return math.log(-Q / 2 + 5)

print("--- Test de convergence pour g1(Q) ---")
iterations_g1 = Pointfixe(g1, 1.0, 1e-8, 150)