"""Module to approximate roots.

Module containing different methods for finding an approximation to a
fucntions root.

Credits
-------
Created on Mon Feb 12 21:51:24 2024

@author: Lindsey Alexandre S2302371
@credits: Luca Odding S2303933, Raffaele Moreci S2304531
"""

# %% [0] Imports
# Third-party imports
import numpy as np


# %% [1] Main Code
def secante(f, x0, x1, tol=0.5e-03, **kwargs):
    """The root of a function.

    Implementation of the secant methode for approximating the root
    of a function.

    Parameters
    ----------
    f : function
        Function to find the root from.
    x0, x1 : numeric
        Values close to the root.
    tol : numeric, *default* 0.5e-3
        Tolerance for the value of the root.

    Other Parameters
    ----------------
    **kwargs : dict, *optional*
        Extra properties such as the maximum number of iterations
        (``max_i``), etc.

        Properties:

    +-----------+------------------------------------------------------------+
    | Name      | Description                                                |
    +===========+============================================================+
    | ``max_i`` | Maximum number of itirations before exiting. The default   |
    |           | is 1 / ``tol``.                                            |
    +-----------+------------------------------------------------------------+

    Returns
    -------
    array
        First value is the root approximation.
        Second value is the exit state of the function: 0 for successfull,
        1 if there is an error.

    Exemple
    -------
    If the function ``f(x)`` is defined as x**2 - 4::

        >>> secant(f, 1, 3)
        [1.9999525931544515, 0]
    """

    i = 0
    if x0 == x1:
        print('x1 et x2 ont la même valeur.')
        return [0, 1]
    try:
        y0 = f(x0)
    except ZeroDivisionError:
        print('f(' + str(x0) + ') n\'existe pas')
        return [0, 1]
    try:
        y1 = f(x1)
    except ZeroDivisionError:
        print('f(' + str(x1) + ') n\'existe pas')
        return [0, 1]
    if 'max_i' in kwargs:
        max_i = kwargs.max_i
    else:
        max_i = 1/tol

    while abs(y1) >= tol:
        num = y1*(x1 - x0)
        if num == 0:
            print('La fonction ne converge pas.')
            return [x0, -1]
        den = y1 - y0
        if den == 0:
            xi = (x0 + x1)/2
        else:
            xi = x1 - num/den
        x0 = x1
        x1 = xi
        y0 = y1
        try:
            y1 = f(xi)
        except ZeroDivisionError:
            print('f(' + str(x1) + ') n\'existe pas')
            return [0, -1]
        i += 1
        if i > max_i:
            print('La fonction n\'a pas convergé après ' + str(i) +
                  ' itérations.')
            return [x0, -1]

    return [x1, 0]


def bissection(f, x0, x1, tol=0.5e-03):
    """The root of a function.

    Implementation of the bisection methode for approximating the root of
    a function.

    Parameters
    ----------
    f : function
        Function to find the root from.
    x0, x1 : numeric
        Values close to the root. ``f(x0)`` and ``f(x1)`` must have
        different signs.
    tol : numeric, *default* 0.5e-3
        Tolerance for the value of the root.

    Returns
    -------
    array
        First value is the root approximation.
        Second value is the exit state of the function: 0 for successfull,
        1 if there is an error.

    Exemple
    -------
    If the function ``f(x)`` is defined as x**2 - 4::

        >>> bisection(f, 1, 3)
        [2.00048828125, 0]

    """
    try:
        y0 = f(x0)
    except ZeroDivisionError:
        print('f(' + str(x0) + ') n\'existe pas')
        return [0, 1]
    try:
        y1 = f(x1)
    except ZeroDivisionError:
        print('f(' + str(x1) + ') n\'existe pas')
        return [0, 1]
    if y0 == 0 or abs(y0) < tol:
        return [x0, 0]
    if y1 == 0 or abs(y1) < tol:
        return [x1, 0]
    if y0 * y1 > 0:
        print('f(x0) et f(x1) sont du même sign.')
        return [0, 1]
    if y0 > y1:
        x0, x1 = x1, x0

    k = np.log2((x1 - x0)/(2*tol))
    i = 0

    while True:
        xi = (x0 + x1)/2
        try:
            yi = f(xi)
        except ZeroDivisionError:
            print('f(' + str(xi) + ') n\'existe pas')
            return [0, -1]

        if yi > 0:
            x1 = xi
        else:
            x0 = xi

        if i > k:
            return [xi, 0]
        i += 1
