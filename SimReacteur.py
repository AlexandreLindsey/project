"""FILE_DESCRIPTION

Credits
-------
Created on Fri Mar 8 10:53:03 2024

@author: Odding Luca s2303933, Raffaele Moreci S2304531
@credits: Lindsey Alexandre S2302371
"""

# %% [0] Imports
# Third-party librairy imports.
import numpy as np
from scipy.integrate import solve_ivp

# Local module imports
from odefunction import odefunction


# %% [1] Main Code
def calculConcentrationsIVP(Z, C0):
    sol = solve_ivp(odefunction, Z, C0, rtol=1e-5)
    return [sol.t, sol.y]


def calculConcentrationsEuler(Z, C0):
    Z = np.array(Z)
    if type(C0) is int:
        C0 = np.array([C0])
    else:
        C0 = np.array(C0)
    h = 10e-8
    abscisse = np.arange(Z[0], Z[1], h)
    n = abscisse.size
    C = np.zeros((C0.shape[0], n))
    xappr = C0
    for i in range(n):
        zi = abscisse[i]
        f = odefunction(zi, xappr)
        C.T[i] = xappr
        xappr = xappr + h*f
    return [abscisse, C]
