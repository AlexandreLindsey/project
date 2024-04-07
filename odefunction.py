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
# First-party librairy imports.
import math

# Third-party librairy imports.
import numpy as np

# Local module imports
import constants as c


# %% [1] Main Code
def odefunction(z, C, mode=0, param=0):
    """Values of the differential equation.

    Parameters
    ----------
    z : numeric
        Value of the axial distance.
    C : array, shape(8)
        Array of the concentrations of ``CH4``, ``H2O``, ``H2``, ``CO``
        and ``CO2``, the conversion fraction (``X``), the temperature (``T``)
        and the pressure (``P``): [``C``:sub:`CH4`, ``C``:sub:`H2O`,
        ``C``:sub:`H2`, ``C``:sub:`CO`, ``C``:sub:`CO2`, ``X``, ``T``, ``P``].
    mode : numeric, *default* 0
        Different modes for odefuncion (see table below).
    param : numeric, *default* 0
        Parameter value used in certain modes (see table below).

    +-------+----------------------------------------------------------------+
    | mode  |  Description                                                   |
    +=======+================================================================+
    | ``0`` | Default mode of odefuncion. ``param`` is not used.             |
    +-------+----------------------------------------------------------------+
    | ``1`` | Odefunction with no carbonation: ``rcbn`` = 0, ``dC[5]`` = 0    |
    |       | and ``c.u('s')`` = 0. ``param`` is not used.                   |
    +-------+----------------------------------------------------------------+
    | ``2`` | Changes the value of ``c.u('s')`` to ``param``.                |
    +-------+----------------------------------------------------------------+
    | ``3`` | Changes the value of ``c.u('g')`` to ``param``.                |
    +-------+----------------------------------------------------------------+
    | ``4`` | Changes the value of ``c.u('s') and ``c.TW()`` to ``param[0]`` |
    |       | and ``param[1]`` respectively.                                 |
    +-------+----------------------------------------------------------------+

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
               * c.rho('CaO') * rcbn(C, mode)) / c.u('g', mode, param))
    # Equation (17): dX/dz
    if mode == 1:
        dC[5] = 0
    else:
        dC[5] = c.MM('CaO') / c.u('s', mode, param) * rcbn(C, mode)
    # Equation (19): dT/dz
    dC[6] = ((-(1 - c.ep()) * c.rho('cat') * c.eta() * sum(R_ * H_)
             - (1 - c.ep()) * c.rho('CaO') * rcbn(C, mode) * c.H('cbn')
             + hW(C, mode, param) * (c.TW(mode, param) - C[6]) * 4
             / c.dim('r')) / ((1 - c.ep()) * c.rho('s') * c.u('s', mode, param)
             * c.Cp('s') + rhog(C) * c.u('g', mode, param) * c.Cp('g')))
    # Equation (20): dP/dz
    dC[7] = (-(rhog(C) * c.u('g', mode, param)**2 * (1 - c.ep())) / (c.dp()
             * c.ep()) * ((150 * (1 - c.ep()) * c.mu()) / (c.dp() * rhog(C)
             * c.u('g', mode, param)) + 1.75) * 1e-5)
    return dC


# Equations (4), (5) and (6)
def R(name, C):
    """Values of the reactions' speed.

    Parameters
    ----------
    name : string
        ``1``, ``2`` or ``3``.
    C : array, shape(8)
        Array of the concentrations of ``CH4``, ``H2O``, ``H2``, ``CO``
        and ``CO2``, the conversion fraction (``X``), the temperature (``T``)
        and the pressure (``P``): [``C``:sub:`CH4`, ``C``:sub:`H2O`,
        ``C``:sub:`H2`, ``C``:sub:`CO`, ``C``:sub:`CO2`, ``X``, ``T``, ``P``].

    Returns
    -------
    numeric
        Returns the value of the ``name`` equation's reaction speed.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if str(name) == '1':
        # Equation (4)
        out = (c.vit(1, C[6]) / c.P('H2', C)**2.5 * (c.P('CH4', C) *
               c.P('H2O', C) - c.P('H2', C)**3 * c.P('CO', C) / c.eq(1, C[6]))
               / DEN(C)**2)
        try:
            if math.isnan(out):
                raise ValueError
        except ValueError:
            print('')
            print('')
            print('')
            print('Error: value for \'' + str(name) + '\' in R() was \''
                  + str(out) + '\'.')
            print('The input values were \'' + str(C) + '\'.')
            print('')
            raise
        return out
    elif str(name) == '2':
        # Equation (5)
        out = (c.vit(2, C[6]) / c.P('H2', C)**3.5 * (c.P('CH4', C) *
               c.P('H2O', C)**2 - c.P('H2', C)**4 * c.P('CO2', C)
               / c.eq(2, C[6])) / DEN(C)**2)
        try:
            if math.isnan(out):
                raise ValueError
        except ValueError:
            print('')
            print('')
            print('')
            print('Error: value for \'' + str(name) + '\' in R() was \''
                  + str(out) + '\'.')
            print('The input values were \'' + str(C) + '\'.')
            print('')
            raise
        return out
    elif str(name) == '3':
        # Equation (6)
        out = (c.vit(3, C[6]) / c.P('H2', C) * (c.P('CO', C) * c.P('H2O', C)
               - c.P('H2', C)*c.P('CO2', C)/c.eq(3, C[6])) / DEN(C)**2)
        try:
            if math.isnan(out):
                raise ValueError
        except ValueError:
            print('')
            print('')
            print('')
            print('Error: value for \'' + str(name) + '\' in R() was \''
                  + str(out) + '\'.')
            print('The input values were \'' + str(C) + '\'.')
            print('')
            raise
        return out
    else:
        try:
            raise NameError()
        except NameError:
            print('')
            print('')
            print('')
            print('Error: value for \'' + str(name) + '\' not found in R().')
            print('The input values were \'' + str(C) + '\'.')
            print('')
            raise


# Equation (7)
def DEN(C):
    """Value of the denominator for R().

    Parameters
    ----------
    C : array, shape(8)
        Array of the concentrations of ``CH4``, ``H2O``, ``H2``, ``CO``
        and ``CO2``, the conversion fraction (``X``), the temperature (``T``)
        and the pressure (``P``): [``C``:sub:`CH4`, ``C``:sub:`H2O`,
        ``C``:sub:`H2`, ``C``:sub:`CO`, ``C``:sub:`CO2`, ``X``, ``T``, ``P``].

    Returns
    -------
    numeric
        Returns the value of the denominator used in the equations in R().
    """
    out = (1 + c.ab('CO', C[6])*c.P('CO', C) + c.ab('H2', C[6])*c.P('H2', C)
           + c.ab('CH4', C[6])*c.P('CH4', C)
           + c.ab('H2O', C[6])*c.P('H2O', C)/c.P('H2', C))
    try:
        if math.isnan(out):
            raise ValueError
    except ValueError:
        print('')
        print('')
        print('')
        print('Error: value in DEN() was \'' + str(out) + '\'.')
        print('The input values were \'' + str(C) + '\'.')
        print('')
        raise
    return out


# Equations (8), (9), (10), (11) and (12)
def r(name, C):
    """Values of the formation/consomation rates.

    Parameters
    ----------
    name : string
        ``CH4``, ``H2O``, ``H2``, ``CO`` or ``CO2``
    C : array, shape(8)
        Array of the concentrations of ``CH4``, ``H2O``, ``H2``, ``CO``
        and ``CO2``, the conversion fraction (``X``), the temperature (``T``)
        and the pressure (``P``): [``C``:sub:`CH4`, ``C``:sub:`H2O`,
        ``C``:sub:`H2`, ``C``:sub:`CO`, ``C``:sub:`CO2`, ``X``, ``T``, ``P``].

    Returns
    -------
    numeric
        Returns the values of ``name``'s formation/consomation rate.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if str(name) == 'CH4':
        # Equation (8)
        out = -R(1, C) - R(2, C)
        try:
            if math.isnan(out):
                raise ValueError
        except ValueError:
            print('')
            print('')
            print('')
            print('Error: value for \'' + str(name) + '\' in r() was \''
                  + str(out) + '\'.')
            print('The input values were \'' + str(C) + '\'.')
            print('')
            raise
        return out
    elif str(name) == 'H2O':
        # Equation (9)
        out = -R(1, C) - 2*R(2, C) - R(3, C)
        try:
            if math.isnan(out):
                raise ValueError
        except ValueError:
            print('')
            print('')
            print('')
            print('Error: value for \'' + str(name) + '\' in r() was \''
                  + str(out) + '\'.')
            print('The input values were \'' + str(C) + '\'.')
            print('')
            raise
        return out
    elif str(name) == 'H2':
        # Equation (10)
        out = 3*R(1, C) + 4*R(2, C) + R(3, C)
        try:
            if math.isnan(out):
                raise ValueError
        except ValueError:
            print('')
            print('')
            print('')
            print('Error: value for \'' + str(name) + '\' in r() was \''
                  + str(out) + '\'.')
            print('The input values were \'' + str(C) + '\'.')
            print('')
            raise
        return out
    elif str(name) == 'CO':
        # Equation (11)
        out = R(1, C) - R(3, C)
        try:
            if math.isnan(out):
                raise ValueError
        except ValueError:
            print('')
            print('')
            print('')
            print('Error: value for \'' + str(name) + '\' in r() was \''
                  + str(out) + '\'.')
            print('The input values were \'' + str(C) + '\'.')
            print('')
            raise
        return out
    elif str(name) == 'CO2':
        # Equation (12)
        out = R(2, C) + R(3, C)
        try:
            if math.isnan(out):
                raise ValueError
        except ValueError:
            print('')
            print('')
            print('')
            print('Error: value for \'' + str(name) + '\' in r() was \''
                  + str(out) + '\'.')
            print('The input values were \'' + str(C) + '\'.')
            print('')
            raise
        return out
    else:
        try:
            raise NameError()
        except NameError:
            print('')
            print('')
            print('')
            print('Error: value for \'' + str(name) + '\' not found in r().')
            print('The input values were \'' + str(C) + '\'.')
            print('')
            raise


# Equation (14)
def kc(C):
    """Value of the apparent rate of carbonation.

    Parameters
    ----------
    C : array, shape(8)
        Array of the concentrations of ``CH4``, ``H2O``, ``H2``, ``CO``
        and ``CO2``, the conversion fraction (``X``), the temperature (``T``)
        and the pressure (``P``): [``C``:sub:`CH4`, ``C``:sub:`H2O`,
        ``C``:sub:`H2`, ``C``:sub:`CO`, ``C``:sub:`CO2`, ``X``, ``T``, ``P``].

    Returns
    -------
    numeric
        Returns the value of the apparent rate of carbonation.
    """
    out = c.M('k') * np.exp(c.N('k') / C[6])
    try:
        if math.isnan(out):
            raise ValueError
    except ValueError:
        print('')
        print('')
        print('')
        print('Error: value for in kc() was \'' + str(out) + '\'.')
        print('The input values were \'' + str(C) + '\'.')
        print('')
        raise
    return out


# Equation (15)
def b(C):
    """Value of the time to get halfway to Xu.

    Parameters
    ----------
    C : array, shape(8)
        Array of the concentrations of ``CH4``, ``H2O``, ``H2``, ``CO``
        and ``CO2``, the conversion fraction (``X``), the temperature (``T``)
        and the pressure (``P``): [``C``:sub:`CH4`, ``C``:sub:`H2O`,
        ``C``:sub:`H2`, ``C``:sub:`CO`, ``C``:sub:`CO2`, ``X``, ``T``, ``P``].

    Returns
    -------
    numeric
        Returns the value of the time to get halfway to the ultimate
        fractional conversion of CaO, Xu.
    """
    out = c.M('b') * np.exp(c.N('b') / C[6])
    try:
        if math.isnan(out):
            raise ValueError
    except ValueError:
        print('')
        print('')
        print('')
        print('Error: value for in b() was \'' + str(out) + '\'.')
        print('The input values were \'' + str(C) + '\'.')
        print('')
        raise
    return out


# Equation (18)
def rcbn(C, mode):
    """Value of the rate of consomation of CO2 by carbonation.

    Parameters
    ----------
    C : array, shape(8)
        Array of the concentrations of ``CH4``, ``H2O``, ``H2``, ``CO``
        and ``CO2``, the conversion fraction (``X``), the temperature (``T``)
        and the pressure (``P``): [``C``:sub:`CH4`, ``C``:sub:`H2O`,
        ``C``:sub:`H2`, ``C``:sub:`CO`, ``C``:sub:`CO2`, ``X``, ``T``, ``P``].

    Returns
    -------
    numeric
        Returns the value of the rate of consomation of CO2 by carbonation.
    """
    if mode == 1:
        return 0
    else:
        out = (kc(C) / c.MM('CaO')) * (1 - C[5]/Xu(C))**2
        try:
            if math.isnan(out):
                raise ValueError
        except ValueError:
            print('')
            print('')
            print('')
            print('Error: value for in rcbn() was \'' + str(out) + '\'.')
            print('The input values were \'' + str(C) + '\'.')
            print('')
            raise
        return out


# Equation (18) bis
def Xu(C):
    """Value of the ultimate fractional conversion of CaO.

    Parameters
    ----------
    C : array, shape(8)
        Array of the concentrations of ``CH4``, ``H2O``, ``H2``, ``CO``
        and ``CO2``, the conversion fraction (``X``), the temperature (``T``)
        and the pressure (``P``): [``C``:sub:`CH4`, ``C``:sub:`H2O`,
        ``C``:sub:`H2`, ``C``:sub:`CO`, ``C``:sub:`CO2`, ``X``, ``T``, ``P``].

    Returns
    -------
    numeric
        Returns the value of the ultimate fractional conversion of CaO.
    """
    out = kc(C) * b(C)
    try:
        if math.isnan(out):
            raise ValueError
    except ValueError:
        print('')
        print('')
        print('')
        print('Error: value for in Xu() was \'' + str(out) + '\'.')
        print('The input values were \'' + str(C) + '\'.')
        print('')
        raise
    return out


# Equation (19) bis bis
def rhog(C):
    """Value of the gas phase's density.

    Parameters
    ----------
    C : array, shape(8)
        Array of the concentrations of ``CH4``, ``H2O``, ``H2``, ``CO``
        and ``CO2``, the conversion fraction (``X``), the temperature (``T``)
        and the pressure (``P``): [``C``:sub:`CH4`, ``C``:sub:`H2O`,
        ``C``:sub:`H2`, ``C``:sub:`CO`, ``C``:sub:`CO2`, ``X``, ``T``, ``P``].

    Returns
    -------
    numeric
        Returns the value of the gas phase's density.
    """
    MM = np.array([c.MM('CH4'), c.MM('H2O'), c.MM('H2'),
                   c.MM('CO'), c.MM('CO2')])
    P = np.array([c.P('CH4', C), c.P('H2O', C), c.P('H2', C),
                  c.P('CO', C), c.P('CO2', C), ])
    out = 1 / (c.R() * C[6]) * sum(MM * P * 100000)
    try:
        if math.isnan(out):
            raise ValueError
    except ValueError:
        print('')
        print('')
        print('')
        print('Error: value for in rhog() was \'' + str(out) + '\'.')
        print('The input values were \'' + str(C) + '\'.')
        print('')
        raise
    return out


# Equation of the reactor's energy balance
def hW(C, mode, param):
    """Value of the reactor's wall heat transfer coefficient.

    Parameters
    ----------
    C : array, shape(8)
        Array of the concentrations of ``CH4``, ``H2O``, ``H2``, ``CO``
        and ``CO2``, the conversion fraction (``X``), the temperature (``T``)
        and the pressure (``P``): [``C``:sub:`CH4`, ``C``:sub:`H2O`,
        ``C``:sub:`H2`, ``C``:sub:`CO`, ``C``:sub:`CO2`, ``X``, ``T``, ``P``].

    Returns
    -------
    numeric
        Returns the value of the reactor's wall heat transfer coefficient.
    """
    Rep = c.u('g', mode, param) * c.ep() * rhog(C) * c.dp() / c.mu()
    if Rep > 20 and 0.05 < c.dp()/c.dim('r') < 0.3:
        out = (2.03 * c.k('g') / c.dim('r') * Rep**0.8 * np.exp(-6 * c.dp()
               / c.dim('r')))
        try:
            if math.isnan(out):
                raise ValueError
        except ValueError:
            print('')
            print('')
            print('')
            print('Error: value for in hW() was \'' + str(out) + '\'.')
            print('The input values were \'' + str(C) + '\'.')
            print('')
            raise
        return out
    elif Rep <= 20:
        kz0 = (c.k('g') * (c.ep() + (1 - c.ep())/(0.139*c.ep() - 0.0339
               + 2/3*(c.k('g') / c.k('s')))))
        out = 6.15 * (kz0 / c.dim('r'))
        try:
            if math.isnan(out):
                raise ValueError
        except ValueError:
            print('')
            print('')
            print('')
            print('Error: value for in hW() was \'' + str(out) + '\'.')
            print('The input values were \'' + str(C) + '\'.')
            print('')
            raise
        return out
    else:
        try:
            raise ValueError()
        except ValueError:
            print('')
            print('')
            print('')
            print('Error in hW().')
            print('The input values were \'' + str(C) + '\'.')
            print('Odefunction was in mode \'' + str(mode) + '\'.')
            print('The value of param was \'' + str(param) + '\'.')
            print('')
            raise
