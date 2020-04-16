from sympy import *
from math import exp, floor
import numpy as np


x = symbols('x')
na = 6.022140857*10**23
kb = 0.00008617330336

def cv_vib(thetaD, tm):    
    global na
    global kb
    for t in np.linspace(1, tm, 100):
        print(9*na*kb*((t/thetaD)**3))*integrate(x**4*exp(x)/(exp(x)-1)**2, (x, 0.01, thetaD/t))


if __name__ == "__main__": 
    print(cv_vib(376, 933))

