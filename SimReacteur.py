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
    # Just to be general and workwith a 1 equation system.
    if type(y0) is int:
        y0 = np.array([y0])
    else:
        y0 = np.array(y0)
    # Initiate the x-axis array.
    x = np.arange(x_int[0], x_int[1], step)
    n = x.size
    # Initialization with (n, y0.shape[0]) instead of (y0.shape[0], n)
    # to transpose the matrix.
    y = np.zeros((n, y0.shape[0]))
    y[0] = y0
    # Loop ends at n - 1 beacause y[0] is already initialised.
    for i in range(n - 1):
        # Equation from the course : x_i+1 = x_i + h * f(x_i; t_i).
        y[i + 1] = y[i] + step*odefunction(x[i], y[i])
    # Return the array of the x-axis (z) and the y-axis (C) transposed.
    # See reason above.
    return [x, y.T]
