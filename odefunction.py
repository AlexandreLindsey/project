"""FILE_DESCRIPTION

Credits
-------
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
from scipy.integrate import solve_ivp
import matplotlib as mpl
from matplotlib import pyplot as plt

# Local module imports
import constants as c


# %% [1] Main Code
def odefunction(z, C):
    dC = np.zeros(8)
    R_ = np.array([R(1, C), R(2, C), R(3, C)])
    H = np.array([c.H(1), c.H(2), c.H(3)])

    dC[0] = ((c.eta() * (1 - c.ep()) * c.rho('cat') * r('CH4', C)
             - (1 - c.ep()) * c.rho('CaO') * rcbn(C)) / c.u('g'))
    dC[1] = ((c.eta() * (1 - c.ep()) * c.rho('cat') * r('H2O', C)
             - (1 - c.ep()) * c.rho('CaO') * rcbn(C)) / c.u('g'))
    dC[2] = ((c.eta() * (1 - c.ep()) * c.rho('cat') * r('H2', C)
             - (1 - c.ep()) * c.rho('CaO') * rcbn(C)) / c.u('g'))
    dC[3] = ((c.eta() * (1 - c.ep()) * c.rho('cat') * r('CO', C)
             - (1 - c.ep()) * c.rho('CaO') * rcbn(C)) / c.u('g'))
    dC[4] = ((c.eta() * (1 - c.ep()) * c.rho('cat') * r('CO2', C)
             - (1 - c.ep()) * c.rho('CaO') * rcbn(C)) / c.u('g'))
    dC[5] = c.MM('CaO') / c.u('s') * rcbn(C)
    dC[6] = ((-(1 - c.ep()) * c.rho('cat') * c.eta() * np.sum(R_ * H)
             - (1 - c.ep()) * c.rho('CaO') * rcbn(C) * c.H('cbn') + hW(C)
             * (c.TW() - C[6]) * 4 / c.dim('r')) / ((1 - c.ep()) * c.rho('s')
             * c.u('s') * c.Cp('s') + rhog(C) * c.u('g') * c.Cp('g')))
    dC[7] = (-(rhog(C) * c.u('g')**2 * (1 - c.ep())) / (c.dp() * c.ep())
             * ((150 * (1 - c.ep()) * c.mu()) / (c.dp() * rhog(C) * c.u('g'))
             + 1.75) * 10**-5)

    return dC


# (4) (5) (6)
def R(name, C):
    if name == 1:
        # (4)
        return (c.vit(1, C[6]) / c.P('H2', C)**2.5 * (c.P('CH4', C) *
                c.P('H2O', C) - c.P('H2', C)**3 * c.P('CO', C) / c.eq(1, C[6]))
                / DEN(C)**2)
    elif name == 2:
        # (5)
        return (c.vit(2, C[6]) / c.P('H2', C)**3.5 * (c.P('CH4', C) *
                c.P('H2O', C)**2 - c.P('H2', C)**4 * c.P('CO2', C)
                / c.eq(2, C[6])) / DEN(C)**2)
    elif name == 3:
        # (6)
        return (c.vit(3, C[6]) / c.P('H2', C) * (c.P('CO', C) * c.P('H2O', C)
                - c.P('H2', C)*c.P('CO2', C)/c.eq(3, C[6])) / DEN(C)**2)
    else:
        print("Error: value for '" + str(name) + "' not found.")
        return None


# (7)
def DEN(C):
    return (1 + c.ab('CO', C[6])*c.P('CO', C) + c.ab('H2', C[6])*c.P('H2', C)
            + c.ab('CH4', C[6])*c.P('CH4', C)
            + c.ab('H2O', C[6])*c.P('H2O', C)/c.P('H2', C))


# (8) (9) (10) (11) (12)
def r(name, C):
    if name == 'CH4':
        # (8)
        return -R(1, C) - R(2, C)
    elif name == 'H2O':
        # (9)
        return -R(1, C) - 2*R(2, C) - R(3, C)
    elif name == 'H2':
        # (10)
        return 3*R(1, C) + 4*R(2, C) + R(3, C)
    elif name == 'CO':
        # (11)
        return R(1, C) - R(3, C)
    elif name == 'CO2':
        # (12)
        return R(2, C) + R(3, C)
    else:
        print("Error: value for '" + str(name) + "' not found.")
        return None


# (14)
def kc(C):
    return c.M('k') * np.exp(c.N('k') / C[6])


# (15)
def b(C):
    return c.M('b') * np.exp(c.N('b') / C[6])


# (18)
def rcbn(C):
    return (kc(C) / c.MM('CaO')) * (1 - C[5]/Xu(C))**2


# (18) bis
def Xu(C):
    return kc(C) * b(C)


# (19) bis bis
def rhog(C):
    MM = np.array([c.MM('CH4'), c.MM('H2O'), c.MM('H2'),
                   c.MM('CO'), c.MM('CO2')])
    P = np.array([c.P('CH4', C), c.P('H2O', C), c.P('H2', C),
                  c.P('CO', C), c.P('CO2', C), ])
    return 1 / (c.R() * C[6]) * np.sum(MM * P * 100000)


def hW(C):
    Rep_ = Rep(C)
    if Rep_ > 20 and c.dp()/c.dim('r') < 0.3 and c.dp()/c.dim('r') > 0.05:
        return (2.03 * c.k('g') / c.dim('r') * Rep_**0.8 * np.exp(-6 * c.dp()
                / c.dim('r')))
    elif Rep_ < 20:
        kz0 = (c.k('g') * (c.ep() + (1 - c.ep())/(0.139*c.ep() - 0.0339
               + 2/3*(c.k('g') / c.k('s')))))
        return 6.15 * (kz0 / c.dim('r'))
    else:
        print("Error: value for '" + str(Rep_) + "' not found.")
        return None


def Rep(C):
    return c.u('g') * c.ep() * rhog(C) * c.dp() / c.mu()


# %% [2] Testing Code

# ERROR: NOT WORKING...
sol = solve_ivp(odefunction, [0, c.dim('l')], [0.0927, 0.0278, 1e-1, 1e-1,
                                               1e-1, 1e-1, c.TW(),
                                               c.P('tot', 0)])

plt.figure()
plt.plot(sol.t, sol.y[0], label='CH4', linewidth=1)
plt.plot(sol.t, sol.y[1], label='H2O', linewidth=1)
plt.plot(sol.t, sol.y[2], label='H2', linewidth=1)
plt.plot(sol.t, sol.y[3], label='CO', linewidth=1)
plt.plot(sol.t, sol.y[4], label='CO2', linewidth=1)
plt.legend(loc='best')
plt.ylabel('Concentration')
plt.xlabel('z')

plt.figure()
plt.plot(sol.t, sol.y[5], label='X', linewidth=1)
plt.legend(loc='best')
plt.ylabel('Conversion fractionnaire')
plt.xlabel('z')

plt.figure()
plt.plot(sol.t, sol.y[6], label='T', linewidth=1)
plt.legend(loc='best')
plt.ylabel('Temperature')
plt.xlabel('z')

plt.figure()
plt.plot(sol.t, sol.y[7], label='P', linewidth=1)
plt.legend(loc='best')
plt.ylabel('Pression')
plt.xlabel('z')
