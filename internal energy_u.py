from scipy.integrate import quad
import math
import numpy as np

na = 6.022140857*10**23
kb = 1.380649*10**(-23)

def debye(x):
    return (x**3)/(((np.exp(x)-1)))

def u(t, thetaD):
    return 9*na*kb*t*((t/thetaD)**3)*quad(debye, 0, thetaD/t)[0]

vec_u = np.vectorize(u)

def u_vib(thetaD, tm):
    return(vec_u(np.arange(1.0, tm, 10), thetaD))

print(u_vib(376, 933))
