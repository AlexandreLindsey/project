"""FILE_DESCRIPTION

Credits
-------
Created on Fri Mar 8 10:53:03 2024

@author: Odding Luca S2303933, Raffaele Moreci S2304531
@credits: Lindsey Alexandre S2302371
"""

# %% [0] Imports
# Third-party librairy imports.
import numpy as np
from scipy.integrate import solve_ivp

# Local module imports
from odefunction import odefunction


# %% [1] Main Code
def calculConcentrationsIVP(x_int, y0):
    sol = solve_ivp(odefunction, x_int, y0, dense_output=True, rtol=0.5e-6)
    return [sol.t, sol.y]


def calculConcentrationsEuler(x_int, y0, step=5e-8):
    # Generalisation to work with a system of equations:
    # Makes sure that y0 is a numpy array.
    if type(y0) is int:
        y0 = np.array([y0])
    else:
        y0 = np.array(y0)
    # Initiates the x-axis array.
    x = np.arange(x_int[0], x_int[1], step)
    # The number of itirations to do (x's size).
    n = x.size
    # Initiates the y-axis array (the solution).
    # The matrix is created in it's transposed state to optimise for speed.
    y = np.zeros((n, y0.shape[0]))
    y[0] = y0
    # Loop ends at n - 1 beacause y[0] is already initialised.
    for i in range(n - 1):
        # Equation from the course for an approximation of the solution:
        # x_i+1 = x_i + h * f(x_i, t_i)
        y[i + 1] = y[i] + step*odefunction(x[i], y[i])
    # Returns the array of the x-axis (x) and the transposed of the y-axis (y).
    # See why above.
    return [x, y.T]
