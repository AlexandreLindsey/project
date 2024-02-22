"""Module containing all of the values of the constants.

This module contains all values that are given in the project's
documentation. They are all accessible through the different functions of
the module (see table below).

+-----------+------------+-----------------------------------------------+
| function  | parameters | description                                   |
+===========+============+===============================================+
| ``R()``   | *none*     | Returns the value of the perfect gasse's      |
|           |            | universall constant, in 8.314 J/mol/K.        |
+-----------+------------+-----------------------------------------------+
| ``dp()``  | *none*     | Returns the diameter of the pellets of CaO,   |
|           |            | 3e-3 in m.                                    |
+-----------+------------+-----------------------------------------------+
| ``TW()``  | *none*     | Returns the value of the gasses' temperature  |
|           |            | at the entrance, 973.15 in K.                 |
+-----------+------------+-----------------------------------------------+
| ``ep()``  | *none*     | Returns the value of epsilon, 0.5.            |
+-----------+------------+-----------------------------------------------+
| ``eta()`` | *none*     | Returns the value of eta, 0.3.                |
+-----------+------------+-----------------------------------------------+
| ``mu()``  | *none*     | Returns the value of mu, 2.8e-3 in Pa*s.      |
+-----------+------------+-----------------------------------------------+
| ``rho()`` | ``name``   | Returns the value of ``name``'s density, 1620 |
|           |            | for ``CaO`` and 1100 for ``catalyst`` (can be |
|           |            | shortened) in kg/m^3.                         |
+-----------+------------+-----------------------------------------------+
| ``MM()``  | ``name``   | Returns the value of ``name``'s molar mass,   |
|           |            | 56 for ``CaO``, 16 for ``CH4``, 18 for        |
|           |            | ``H2O``, 2 for ``H2``, 28 for ``CO`` and 44   |
|           |            | for ``CO2`` in kg/kmol.                       |
+-----------+------------+-----------------------------------------------+
| ``H()``   | ``name``   | Returns the value of the ``name`` reaction's  |
|           |            | enthalpy, 206e3 for ``1``, 164.9e3 for ``2``, |
|           |            | -41.1e3 for ``3`` and -178.8e3 for ``cbn`` in |
|           |            | kJ/kmol.                                      |
+-----------+------------+-----------------------------------------------+
| ``dim()`` | ``name``   | Returns the value of the reactors ``name``,   |
|           |            | 2.4e-2 for ``radius`` (can be shortened) and  |
|           |            | 0.29 for ``length`` (can be shortened) in m.  |
+-----------+------------+-----------------------------------------------+
| ``Cp()``  | ``name``   | Returns the value of thermal capacity of      |
|           |            | ``name``, 8.45 for ``g`` and 0.98 for ``s``   |
|           |            | in kJ/kg/K.                                   |
+-----------+------------+-----------------------------------------------+
| ``k()``   | ``name``   | Returns the value of thermal conductivities   |
|           |            | of ``name``, 2.59e-4 for ``g`` and 1e-3 for   |
|           |            | ``s`` in kJ/m/s/K.                            |
+-----------+------------+-----------------------------------------------+
| ``u()``   | ``name``   | Returns the value of the speed of ``name``,   |
|           |            | 1 for ``g`` and 1e-3 for ``s`` in m/s.        |
+-----------+------------+-----------------------------------------------+
| ``W()``   | ``name``   | Returns the value of ``name``'s mass flow,    |
|           |            | 83.6e-3 for ``CaO`` and 16.4e-3 for           |
|           |            | ``catalyst`` (can be shortened) in kg/h.      |
+-----------+------------+-----------------------------------------------+
| ``M()``   | ``name``   | Returns the value of ``name``'s "M"           |
|           |            | parameter, 303 for ``k`` and 1.6 for ``b``.   |
+-----------+------------+-----------------------------------------------+
| ``N()``   | ``name``   | Returns the value of ``name``'s "M"           |
|           |            | parameter,-13146 for ``k`` and 5649 for       |
|           |            | ``b``.                                        |
+-----------+------------+-----------------------------------------------+
| ``eq()``  | ``name``,  | Returns the value of the ``name`` reaction's  |
|           | ``T``      | equilibrium constant based on the temperature |
|           |            | ``T``.                                        |
+-----------+------------+-----------------------------------------------+
| ``vit()`` | ``name``,  | Returns the value of the ``name`` reaction's  |
|           | ``T``      | speed constant based on the temperature       |
|           |            | ``T``.                                        |
+-----------+------------+-----------------------------------------------+
| ``ab()``  | ``name``,  | Returns the value of the ``name`` reaction's  |
|           | ``T``      | absorption constant based on the temperature  |
|           |            | ``T``.                                        |
+-----------+------------+-----------------------------------------------+
| ``P()``   | *none*     | Returns the value of the total pressure, 3 in |
|           |            | bars.                                         |
+-----------+------------+-----------------------------------------------+

Credits
-------
Created on Thu Feb 22 15:04:20 2024

@author: Lindsey Alexandre S2302371
@credits: Luca Odding S2303933, Raffaele Moreci S2304531
"""

# %% [0] Imports

# Third-party librairy imports.
import numpy as np


# %% [1] Main Code
def R():
    """Value of R.

    Returns
    -------
    numeric
        Returns the value of the perfect gasse's universall constant,
        8.314 in J/mol/K.
    """
    return 8.314


def dp():
    """Value of dp.

    Returns
    -------
    numeric
        Returns the diameter of the pellets of CaO, in 3e-3 m.
    """
    return 3e-3


def TW():
    """Value of TW.

    Returns
    -------
    numeric
        Returns the value of the gasses' temperature at the entrance,
        973.15 in K.
    """
    return 973.15


def ep():
    """Value of epsilon.

    Returns
    -------
    numeric
        Returns the value of epsilon, 0.5.
    """
    return 0.5


def eta():
    """Value of eta.

    Returns
    -------
    numeric
        Returns the value of eta, 0.3.
    """
    return 0.3


def mu():
    """Value of mu.

    Returns
    -------
    numeric
        Returns the value of mu, 2.8e-3 in Pa*s.
    """
    return 2.8e-3


def rho(name):
    """Values of the densities.

    Parameters
    ----------
    name : string
        ``CaO`` or ``catalyst`` (can be shortened).

    Returns
    -------
    numeric
        Returns the value of ``name``'s density, 1620 for ``CaO`` and 1100
        for ``catalyst`` in kg/m^3.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if name == 'CaO':
        return 1620
    elif 'catalyst'.startswith(name.lower()):
        return 1100
    elif name == 's':
        num = W('cat') + W('CaO')
        den = W('cat')/rho('cat') + W('CaO')/rho('CaO')
        return num / den
    else:
        print("Error: value for '" + name + "' not found.")
        return None


def MM(name):
    """Values of the molar masses.

    Parameters
    ----------
    name : string
        ``CaO``, ``CH4``, ``H2O``, ``H2``, ``CO`` or ``CO2``.

    Returns
    -------
    numeric
        Returns the value of ``name``'s molar mass, 56 for ``CaO``, 16 for
        ``CH4``, 18 for ``H2O``, 2 for ``H2``, 28 for ``CO`` and 44 for
        ``CO2`` in kg/kmol.
        Returns ``None`` if an incorrect parameter is passed through.
    """
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
        return None


def H(name):
    """Values of the reactions' enthalpy.

    Parameters
    ----------
    name : string
        ``1``, ``2``, ``3`` or ``cbn``.

    Returns
    -------
    numeric
        Returns the value of the ``name`` reaction's enthalpy, 206e3 for
        ``1``, 164.9e3 for ``2``, -41.1e3 for ``3`` and -178.8e3 for
        ``cbn`` in kJ/kmol.
        Returns ``None`` if an incorrect parameter is passed through.
    """
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
        return None


def dim(name):
    """Values of the reactor's dimensions.

    Parameters
    ----------
    name : string
        ``radius`` (can be shortened) or ``length`` (can be shortened).

    Returns
    -------
    numeric
        Returns the value of the reactors ``name``, 2.4e-2 for ``radius``
        and 0.29 for ``length`` in m.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if 'radius'.startswith(name.lower()):
        return 2.4e-2
    elif 'length'.startswith(name.lower()):
        return 0.29
    else:
        print("Error: value for '" + name + "' not found.")
        return None


def Cp(name):
    """Values of the thermal capacities.

    Parameters
    ----------
    name : string
        ``g`` or ``s``.

    Returns
    -------
    numeric
        Returns the value of thermal capacity of ``name``, 8.45 for ``g``
        and 0.98 for ``s`` in kJ/kg/K.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if name == 'g':
        return 8.45
    elif name == 's':
        return 0.98
    else:
        print("Error: value for '" + name + "' not found.")
        return None


def k(name):
    """Values of the thermal conductivities.

    Parameters
    ----------
    name : string
        ``g`` or ``s``.

    Returns
    -------
    numeric
        Returns the value of thermal conductivities of ``name``, 2.59e-4
        for ``g`` and 1e-3 for ``s`` in kJ/m/s/K.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if name == 'g':
        return 2.59e-4
    elif name == 's':
        return 1e-3
    else:
        print("Error: value for '" + name + "' not found.")
        return None


def u(name):
    """Values of the speeds.

    Parameters
    ----------
    name : string
        ``g`` or ``s``.

    Returns
    -------
    numeric
        Returns the value of the speed of ``name``, 1 for ``g`` and 1e-3
        for ``s`` in m/s.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if name == 'g':
        return 1
    elif name == 's':
        return 1e-3
    else:
        print("Error: value for '" + name + "' not found.")
        return None


def W(name):
    """Value of the mass flows.

    Parameters
    ----------
    name : string
        ``CaO`` or ``catalyst`` (can be shortened).

    Returns
    -------
    numeric
        Returns the value of ``name``'s mass flow, 83.6e-3 for ``CaO`` and
        16.4e-3 for ``catalyst`` (can be shortened) in kg/h.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if name == 'CaO':
        return 83.6e-3
    elif 'catalyst'.startswith(name.lower()):
        return 16.4e-3
    else:
        print("Error: value for '" + name + "' not found.")
        return None


def M(name):
    """Values of the "M" parameters.

    Parameters
    ----------
    name : string
        ``k`` or ``b``.

    Returns
    -------
    numeric
        Returns the value of ``name``'s "M" parameter, 303 for ``k`` and
        1.6 for ``b``.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if name == 'k':
        return 303
    elif name == 'b':
        return 1.6
    else:
        print("Error: value for '" + name + "' not found.")
        return None


def N(name):
    """Values of the "M" parameters.

    Parameters
    ----------
    name : string
        ``k`` or ``b``.

    Returns
    -------
    numeric
        Returns the value of ``name``'s "M" parameter, -13146 for ``k``
        and 5649 for ``b``.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if name == 'k':
        return -13146
    elif name == 'b':
        return 5649
    else:
        print("Error: value for '" + name + "' not found.")
        return None


def eq(name, T):
    """Values of the reactions' equilibrium constant.

    Parameters
    ----------
    name : string
        ``1``, ``2`` or ``3``.
    T : numeric
        Value of the temperature.

    Returns
    -------
    numeric
        Returns the value of the ``name`` reactions's equilibrium constant
        based on the temperature ``T``.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if name == 1:
        return 4.707e12 * np.exp(-224000 / (R() * T))
    elif name == 2:
        return k(1) * k(3)
    elif name == 3:
        return 1.142e-2 * np.exp(37300 / (R() * T))
    else:
        print("Error: value for '" + name + "' not found.")
        return None


def vit(name, T):
    """Values of the reactions' speed constant.

    Parameters
    ----------
    name : string
        ``1``, ``2`` or ``3``.
    T : numeric
        Value of the temperature.

    Returns
    -------
    numeric
        Returns the value of the ``name`` reactions's speed constant based
        on the temperature ``T``.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if name == 1:
        return 1.842e-4 / 3600 * np.exp((-240100 / R()) * (1/T - 1/648))
    elif name == 2:
        return 2.193e-5 / 3600 * np.exp((-243900 / R()) * (1/T - 1/648))
    elif name == 3:
        return 7.558 / 3600 * np.exp((-67130 / R()) * (1/T - 1/648))
    else:
        print("Error: value for '" + name + "' not found.")
        return None


def ab(name, T):
    """Values of the reactions' absorption constant.

    Parameters
    ----------
    name : string
        ``CH4``, ``H2O``, ``H2`` or ``CO``.
    T : numeric
        Value of the temperature.

    Returns
    -------
    numeric
        Returns the value of the ``name`` reactions's absorption constant
        based on the temperature ``T``.
        Returns ``None`` if an incorrect parameter is passed through.
    """
    if name == 'CH4':
        return 0.179 * np.exp((38280 / R()) * (1/T - 1/823))
    elif name == 'H2O':
        return 0.4152 * np.exp((-88680 / R()) * (1/T - 1/823))
    elif name == 'H2':
        return 0.0296 * np.exp((82900 / R()) * (1/T - 1/648))
    elif name == 'CO':
        return 40.91 * np.exp((70650 / R()) * (1/T - 1/648))
    else:
        print("Error: value for '" + name + "' not found.")
        return None


def P():
    """Value of the total pressure.

    Returns
    -------
    numeric
        Returns the value of the total pressure, 3 in bars.
    """
    return 3


# %% [2] Testing Code
