from scipy.integrate import quad
import math
import numpy as np

na = 6.022140857*10**23
kb = 1.380649*10**(-23)

def debye(x):
    return (x**4)*np.exp(x)/(((np.exp(x)-1)**2))

def cv(t, thetaD):
    return 9*na*kb*((t/thetaD)**3)*quad(debye, 0, thetaD/t)[0]

vec_cv = np.vectorize(cv)

def cv_vib(thetaD, tm):
    return(vec_cv(np.arange(1.0, tm, 10), thetaD))

print(cv_vib(376, 933))
