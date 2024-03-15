"""Module containing odefunction.

This module contains the function odefunction which returns the differential
equation of dC/dz. It also contains all of the different sub-equations needed
in the differential equations and depends on all of the constants in the file
``constants.py``

Credits
-------
Created on Fri Feb 16 15:55:14 2024

@author: Lindsey Alexandre S2302371
@credits: Luca Odding S2303933, Raffaele Moreci S2304531
"""

# %% [0] Imports

# Third-party librairy imports.
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt

# Local module imports
import constants as c


# %% [1] Main Code
def odefunction(z, C):
    """Values of the differential equation.

    Parameters
    ----------
    z : numeric
        Value of the axial distance.
    C : array, shape(8)
        Array of the concentrations of CH4, H2O, H2, CO and CO2, the conversion
        fraction, the temperature and the pressure: [C, C, C, C, C, X, T, P].

    Returns
    -------
    dC : array, shape(8)
        Returns the values of the 8 differential equations: [dC/dz, dC/dz,
        dC/dz, dC/dz, dC/dz, dX/dz, dT/dz, dP/dz].
    """
    # Creates all of the necessary arrays to be used in the equations below.
    dC = np.zeros(8)
    r_ = np.array([r('CH4', C), r('H2O', C), r('H2', C),
                   r('CO', C), r('CO2', C)])
    R_ = np.array([R(1, C), R(2, C), R(3, C)])
    H_ = np.array([c.H(1), c.H(2), c.H(3)])

    # Equation (16): dC/dz of the different elements (CH4, H2O, H2, CO and CO2)
    dC[:5] = ((c.eta() * (1 - c.ep()) * c.rho('cat') * r_ - (1 - c.ep())
               * c.rho('CaO') * rcbn(C)) / c.u('g'))
    # Equation (17): dX/dz
    dC[5] = c.MM('CaO') / c.u('s') * rcbn(C)
    # Equation (19): dT/dz
    dC[6] = ((-(1 - c.ep()) * c.rho('cat') * c.eta() * sum(R_ * H_)
             - (1 - c.ep()) * c.rho('CaO') * rcbn(C) * c.H('cbn') + hW(C)
             * (c.TW() - C[6]) * 4 / c.dim('r')) / ((1 - c.ep()) * c.rho('s')
             * c.u('s') * c.Cp('s') + rhog(C) * c.u('g') * c.Cp('g')))
    # Equation (20): dP/dz
    dC[7] = (-(rhog(C) * c.u('g')**2 * (1 - c.ep())) / (c.dp() * c.ep())
             * ((150 * (1 - c.ep()) * c.mu()) / (c.dp() * rhog(C) * c.u('g'))
             + 1.75) * 1e-5)
    return dC


# Equations (4), (5) and (6)
def R(name, C):
    """Values of the reactions' speed.

    Parameters
    ----------
    name : string
        ``1``, ``2`` or ``3``.
    C : array, shape(8)
        Array of the concentrations of CH4, H2O, H2, CO and CO2, the conversion
        fraction, the temperature and the pressure: [C, C, C, C, C, X, T, P].

    Returns
    -------
    numeric
        Returns the value of the ``name`` equation's reaction speed.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if str(name) == '1':
        # Equation (4)
        return (c.vit(1, C[6]) / c.P('H2', C)**2.5 * (c.P('CH4', C) *
                c.P('H2O', C) - c.P('H2', C)**3 * c.P('CO', C) / c.eq(1, C[6]))
                / DEN(C)**2)
    elif str(name) == '2':
        # Equation (5)
        return (c.vit(2, C[6]) / c.P('H2', C)**3.5 * (c.P('CH4', C) *
                c.P('H2O', C)**2 - c.P('H2', C)**4 * c.P('CO2', C)
                / c.eq(2, C[6])) / DEN(C)**2)
    elif str(name) == '3':
        # Equation (6)
        return (c.vit(3, C[6]) / c.P('H2', C) * (c.P('CO', C) * c.P('H2O', C)
                - c.P('H2', C)*c.P('CO2', C)/c.eq(3, C[6])) / DEN(C)**2)
    else:
        print("Error: value for '" + str(name) + "' not found in R().")
        print("The input values were '" + str(C) + "'.")
        return None


# Equation (7)
def DEN(C):
    """Value of the denominator for R().

    Parameters
    ----------
    C : array, shape(8)
        Array of the concentrations of CH4, H2O, H2, CO and CO2, the conversion
        fraction, the temperature and the pressure: [C, C, C, C, C, X, T, P].

    Returns
    -------
    numeric
        Returns the value of the denominator used in the equations in R().
    """
    return (1 + c.ab('CO', C[6])*c.P('CO', C) + c.ab('H2', C[6])*c.P('H2', C)
            + c.ab('CH4', C[6])*c.P('CH4', C)
            + c.ab('H2O', C[6])*c.P('H2O', C)/c.P('H2', C))


# Equations (8), (9), (10), (11) and (12)
def r(name, C):
    """Values of the formation/consomation rates.

    Parameters
    ----------
    name : string
        ``CH4``, ``H2O``, ``H2``, ``CO`` or ``CO2``
    C : array, shape(8)
        Array of the concentrations of CH4, H2O, H2, CO and CO2, the conversion
        fraction, the temperature and the pressure: [C, C, C, C, C, X, T, P].

    Returns
    -------
    numeric
        Returns the values of ``name``'s formation/consomation rate.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if str(name) == 'CH4':
        # Equation (8)
        return -R(1, C) - R(2, C)
    elif str(name) == 'H2O':
        # Equation (9)
        return -R(1, C) - 2*R(2, C) - R(3, C)
    elif str(name) == 'H2':
        # Equation (10)
        return 3*R(1, C) + 4*R(2, C) + R(3, C)
    elif str(name) == 'CO':
        # Equation (11)
        return R(1, C) - R(3, C)
    elif str(name) == 'CO2':
        # Equation (12)
        return R(2, C) + R(3, C)
    else:
        print("Error: value for '" + str(name) + "' not found in r().")
        print("The input values were '" + str(C) + "'.")
        return None


# Equation (14)
def kc(C):
    """Value of the apparent rate of carbonation.

    Parameters
    ----------
    C : array, shape(8)
        Array of the concentrations of CH4, H2O, H2, CO and CO2, the conversion
        fraction, the temperature and the pressure: [C, C, C, C, C, X, T, P].

    Returns
    -------
    numeric
        Returns the value of the apparent rate of carbonation.
    """
    return c.M('k') * np.exp(c.N('k') / C[6])


# Equation (15)
def b(C):
    """Value of the time to get halfway to Xu.

    Parameters
    ----------
    C : array, shape(8)
        Array of the concentrations of CH4, H2O, H2, CO and CO2, the conversion
        fraction, the temperature and the pressure: [C, C, C, C, C, X, T, P].

    Returns
    -------
    numeric
        Returns the value of the time to get halfway to the ultimate
        fractional conversion of CaO, Xu.
    """
    return c.M('b') * np.exp(c.N('b') / C[6])


# Equation (18)
def rcbn(C):
    """Value of the rate of consomation of CO2 by carbonation.

    Parameters
    ----------
    C : array, shape(8)
        Array of the concentrations of CH4, H2O, H2, CO and CO2, the conversion
        fraction, the temperature and the pressure: [C, C, C, C, C, X, T, P].

    Returns
    -------
    numeric
        Returns the value of the rate of consomation of CO2 by carbonation.
    """
    return (kc(C) / c.MM('CaO')) * (1 - C[5]/Xu(C))**2


# Equation (18) bis
def Xu(C):
    """Value of the ultimate fractional conversion of CaO.

    Parameters
    ----------
    C : array, shape(8)
        Array of the concentrations of CH4, H2O, H2, CO and CO2, the conversion
        fraction, the temperature and the pressure: [C, C, C, C, C, X, T, P].

    Returns
    -------
    numeric
        Returns the value of the ultimate fractional conversion of CaO.
    """
    return kc(C) * b(C)


# Equation (19) bis bis
def rhog(C):
    """Value of the gas phase's density.

    Parameters
    ----------
    C : array, shape(8)
        Array of the concentrations of CH4, H2O, H2, CO and CO2, the conversion
        fraction, the temperature and the pressure: [C, C, C, C, C, X, T, P].

    Returns
    -------
    numeric
        Returns the value of the gas phase's density.
    """
    MM = np.array([c.MM('CH4'), c.MM('H2O'), c.MM('H2'),
                   c.MM('CO'), c.MM('CO2')])
    P = np.array([c.P('CH4', C), c.P('H2O', C), c.P('H2', C),
                  c.P('CO', C), c.P('CO2', C), ])
    return 1 / (c.R() * C[6]) * sum(MM * P * 100000)


# Equation of the reactor's energy balance
def hW(C):
    """Value of the reactor's wall heat transfer coefficient.

    Parameters
    ----------
    C : array, shape(8)
        Array of the concentrations of CH4, H2O, H2, CO and CO2, the conversion
        fraction, the temperature and the pressure: [C, C, C, C, C, X, T, P].

    Returns
    -------
    numeric
        Returns the value of the reactor's wall heat transfer coefficient.
    """
    Rep = c.u('g') * c.ep() * rhog(C) * c.dp() / c.mu()
    if Rep > 20 and 0.05 < c.dp()/c.dim('r') < 0.3:
        return (2.03 * c.k('g') / c.dim('r') * Rep**0.8 * np.exp(-6 * c.dp()
                / c.dim('r')))
    elif Rep <= 20:
        kz0 = (c.k('g') * (c.ep() + (1 - c.ep())/(0.139*c.ep() - 0.0339
               + 2/3*(c.k('g') / c.k('s')))))
        return 6.15 * (kz0 / c.dim('r'))
    else:
        print("Error in hW().")
        print("The input values were '" + str(C) + "'.")
        return None
