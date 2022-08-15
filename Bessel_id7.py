
#Bessel's identity
#(7) jn(n-1,x) - jn(n+1,x) = 2*jn'(n,x)

import numpy as np
from scipy.special import jn
from scipy.integrate import quad
from scipy.misc import derivative

n=int(input("Enter the n: "))
x=float(input("Enter the x: "))

def Bessels(x):
    return jn(n,x)
def der_Bessels(x):
    return derivative(Bessels,x,order=51)

LHS=jn(n-1,x)-jn(n+1,x)
RHS=2*der_Bessels(x)

print("LHS: ",LHS)
print("RHS: ",RHS)
