"""FILE_DESCRIPTION

Credits
-------
Created on Thu Mar 28 13:25:10 2024

@author: Lindsey Alexandre S2302371
@credits: Luca Odding S2303933, Raffaele Moreci S2304531
"""

# %% [0] Imports
# Third-party librairy imports.
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt

# Local module imports
from odefunction import odefunction as ode
import constants as c
from root import secant


# %% [1] Main Code
def optimise_us(Y, us, C0):
    sol = solve_ivp(lambda z, C: ode(z, C, mode=2, param=us), [0, c.dim('l')],
                    C0)
    return (sol.y[4][-1]/(sol.y[0][-1] + sol.y[2][-1] + sol.y[3][-1]
                          + sol.y[4][-1]) - Y)


# %% [2] Testing Code
if __name__ == '__main__':
    C0 = [1/4/22.4, 3/4/22.4, 1e-5, 0, 0, 0, c.TW(), 3]
    x = [0.01, 0.2]
    A = np.arange(x[0], x[1], 0.005)
    B = np.zeros(A.size)
    C = np.zeros(A.size)
    for i in range(A.size):
        B[i] = optimise_us(0.075, A[i], C0)
    plt.plot(A, B, label='us', linewidth=1)
    plt.plot(A, C, color='black', linewidth=1)
    x0 = secant(lambda us: optimise_us(0.075, us, C0), x, tol=0.5e-8,
                hybrid=True)
    y0 = optimise_us(0.075, x0[1], C0)
    print(x0)
    plt.plot(x0[1], y0, 'xr')
