"""FILE_DESCRIPTION

Credits
=======
Created on Fri Feb 16 15:55:14 2024

@author: Lindsey Alexandre S2302371
@credits: Luca Odding S2303933, Raffaele Moreci S2304531
"""

# % [0] Imports
# Standard library imports.
import math

# Third-party librairy imports.
import numpy as np
import scipy as sp
import matplotlib as mpl
from matplotlib import pyplot as plt

# Local module imports

# Global variables
MM = {'CaO': 56, 'CH4': 16, 'H2O': 18, 'H2': 2, 'CO': 28, 'CO2': 44}
RHO = {'CaO': 1620, 'cat': 1100}
DIM = {'r': 2.4e-2, 'l': 0.29}
CPG = 8.45
CPS = 0.98
DP = 3e-3
WCAO = 83.6e-3
WCAT = 16.4e-3
KG = 2.59e-4
KS = 1e-3
UG = 1
US = 1e-3
TW = 973.15
MK = 303
NK = -13146
MB = 1.6
NB = 5649
EP = 0.5
MU = 2.8e-3
ETA = 0.3


# % [1] Main Code
def odefunction(C, z):
    global MM
    dC = np.zeros(8)

    dC[0]
    dC[1]
    dC[2]
    dC[3]
    dC[4]
    dC[5]
    dC[6]
    dC[7]

    return dC


# % [2] Testing Code
