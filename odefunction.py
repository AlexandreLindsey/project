"""FILE_DESCRIPTION

Credits
=======
Created on Fri Feb 16 15:55:14 2024

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


class constant():
    def R(self):
        return 8.314

    def dp(self):
        return 3e-3

    def TW(self):
        return 973.15

    def ep(self):
        return 0.5

    def eta(self):
        return 0.3

    def mu(self):
        return 2.8e-3

    def rho(self, name):
        if name == 'CaO':
            return 1620
        elif 'catalyst'.startswith(name.lower()):
            return 1100
        elif name == 's':
            num = self.W('cat') + self.W('CaO')
            den = self.W('cat')/self.rho('cat') + self.W('CaO')/self.rho('CaO')
            return num / den
        else:
            print("Error: value for '" + name + "' not found.")
            return -1

    def MM(self, name):
        if name == 'CaO':
            return 56
        elif name == 'CH4':
            return 16
        elif name == 'H2O':
            return 18
        elif name == 'H2':
            return 2
        elif name == 'CO':
            return 28
        elif name == 'CO2':
            return 44
        else:
            print("Error: value for '" + name + "' not found.")
            return -1

    def H(self, name):
        if name == 1:
            return 206e3
        elif name == 2:
            return 164.9e3
        elif name == 3:
            return -41.1e3
        elif name == 'cbn':
            return -178.8e3
        else:
            print("Error: value for '" + name + "' not found.")
            return -1

    def dim(self, name):
        if 'radius'.startswith(name.lower()):
            return 2.4e-2
        elif 'length'.startswith(name.lower()):
            return 0.29
        else:
            print("Error: value for '" + name + "' not found.")
            return -1

    def Cp(self, name):
        if name == 'g':
            return 8.45
        elif name == 's':
            return 0.98
        else:
            print("Error: value for '" + name + "' not found.")
            return -1

    def K(self, name):
        if name == 'g':
            return 2.59e-4
        elif name == 's':
            return 1e-3
        else:
            print("Error: value for '" + name + "' not found.")
            return -1

    def u(self, name):
        if name == 'g':
            return 1
        elif name == 's':
            return 1e-3
        else:
            print("Error: value for '" + name + "' not found.")
            return -1

    def W(self, name):
        if name == 'CaO':
            return 83.6e-3
        elif 'catalyst'.startswith(name.lower()):
            return 16.4e-3
        else:
            print("Error: value for '" + name + "' not found.")
            return -1

    def M(self, name):
        if name == 'k':
            return 303
        elif name == 'b':
            return 1.6
        else:
            print("Error: value for '" + name + "' not found.")
            return -1

    def N(self, name):
        if name == 'k':
            return -13146
        elif name == 'b':
            return 5649
        else:
            print("Error: value for '" + name + "' not found.")
            return -1


class variables():
    def __init__(self):
        c = constant()
        self.R = c.R()
        self.TW = c.TW()

    def eq(self, name, T):
        R = self.R
        if name == 1:
            return 4.707e12 * np.exp(-224000 / (R * T))
        elif name == 2:
            return self.K(1) * self.K(3)
        elif name == 3:
            return 1.142e-2 * np.exp(37300 / (R * T))
        else:
            print("Error: value for '" + name + "' not found.")
            return -1

    def vit(self, name, T):
        R = self.R
        if name == 1:
            return 1.842e-4 / 3600 * np.exp((-240100 / R) * (1/T - 1/648))
        elif name == 2:
            return 2.193e-5 / 3600 * np.exp((-243900 / R) * (1/T - 1/648))
        elif name == 3:
            return 7.558 / 3600 * np.exp((-67130 / R) * (1/T - 1/648))
        else:
            print("Error: value for '" + name + "' not found.")
            return -1

    def ab(self, name, T):
        R = self.R
        if name == 'CH4':
            return 0.179 * np.exp((38280 / R) * (1/T - 1/823))
        elif name == 'H2O':
            return 0.4152 * np.exp((-88680 / R) * (1/T - 1/823))
        elif name == 'H2':
            return 0.0296 * np.exp((82900 / R) * (1/T - 1/648))
        elif name == 'CO':
            return 40.91 * np.exp((70650 / R) * (1/T - 1/648))
        else:
            print("Error: value for '" + name + "' not found.")
            return -1


# Global variables
c = constant()
k = variables()


# %% [1] Main Code
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


# %% [2] Testing Code
