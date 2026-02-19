import math
import sympy as sp
import numpy
from bissection import Bissection
from pointfixe import Pointfixe



#c)
Q = sp.symbols('Q')
FQ = (math.e**Q) + (Q/2) - 5
print(Bissection(FQ,1,2,0.5*(10**-5),18))

