import math
import sympy as sp
import numpy
from bissection import Bissection
from pointfixe import Pointfixe



#c)
def F(Q):
    return math.e**Q + Q/2 -5

print(Bissection(F,1,2,0.000005,18))
#l'erreur (err) en n = 18 est err = 3.814697E-06 = 0,3814697E-5

