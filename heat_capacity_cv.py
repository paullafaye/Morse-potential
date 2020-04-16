from scipy.integrate import quad
from math import *
import numpy as np


na = 6.022140857*10**23
kb = 0.00008617330336

def cv_vib(thetaD, tm):    
    global na
    global kb
    for t in np.linspace(0, floor(tm), 100):
        return t

# 9*na*kb*((t/thetaD)**3)*quad((x**4*np.exp(x))/((np.exp(x)-1)**2), 0, thetaD/t)
print(cv_vib(376, 933))