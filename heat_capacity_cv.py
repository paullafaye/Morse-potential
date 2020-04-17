from scipy.integrate import quad
import numpy as np

na = 6.022140857*10**23
kb = 1.38064852*10**(-23)

def cv_vib(tD, tm):
    result = [0]
    temperature = [0]
    debye = lambda x:(x**4)*np.exp(x)/(((np.exp(x)-1)**2))
    
    for t in np.arange(1, tm, 10):
        temperature.append(t)
        integral_x = quad(debye, 0, tD/t)[0]
        result.append(9*na*kb*((t/tD)**3)*integral_x)
        
    return temperature, result

if __name__ == "__main__": 
    print (cv_vib(376.447744459516, 933))



