"""FILE_DESCRIPTION

Credits
-------
Created on Thu Apr  4 14:36:28 2024

@author: Lindsey Alexandre S2302371
@credits: Luca Odding S2303933, Raffaele Moreci S2304531
"""

# %% [0] Imports
# Standard library imports.
import math

# Third-party librairy imports.
import numpy as np
import scipy as sp
import matplotlib as mpl
from matplotlib import pyplot as plt

# Local module imports


# %% [1] Main Code
def exp(x):
    return 10**(-x)


def out(x, coeff):
    return coeff[0]*np.exp(coeff[1]*x)


# %% [2] Testing Code
if __name__ == "__main__":
    x = [0, 1, 2, 3, 4, 5, 6]
    y = [0, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]
    A = np.arange(0, 6, 0.01)
    B = np.zeros(A.size)
    for i in range(A.size):
        B[i] = exp(A[i])
    plt.plot(A, B, linewidth=1)
    coeff = sp.optimize.curve_fit(lambda x, a, b: a*np.exp(b*x), x, y)
    print(coeff)
    C = np.zeros(A.size)
    for i in range(A.size):
        C[i] = out(A[i], coeff[0])
    plt.plot(A, C, linewidth=1)
