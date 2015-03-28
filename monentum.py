#momentum equations

from sympy import *
# p = momentum
# m = mass
# v = velocity
# f = force
# I = Impulse

 p = m * v
 I = delta(p)
 I = f * delta(t)
 I = m * delta(v)
 p1 = p2 #Conservation of Momentum
 m1 * v1 + m2 * v2 = m1* v3 + m2 * v4 #Hit and Seperate
 m1 * v1 + m2* v2 = (m1 + m2) * v3 #Hit and Stick