"""Module to approximate roots.

Module containing different methods for finding an approximation to a
fucntions root.

Credits
=======
Created on Mon Feb 12 21:51:24 2024

@author: Lindsey Alexandre S2302371
"""

# %% [0] Imports
# Third-party imports
import numpy as np
from matplotlib import pyplot as plt


# %% [1] Main Code
def secant(f, x0, x1, tol=0.5e-03, **kwargs):
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
        (`max_i`), etc.

        Properties:

    +-----------+------------------------------------------------------------+
    | Name      | Description                                                |
    +===========+============================================================+
    | `max_i`   | Maximum number of itirations before exiting. The default   |
    |           | is 1 / `tol`.                                              |
    +-----------+------------------------------------------------------------+

    Returns
    -------
    array
        First value is the root approximation.
        Second value is the exit state of the function: 0 for successfull,
        -1 for exit because `max_i` was reached.

    Exemple
    -------
    If the function `f(x)` is defined as x**2 - 4::

        >>> secant(f, 1, 3)
        [1.9999525931544515, 0]
    """

    i = 0
    y0 = f(x0)
    y1 = f(x1)
    if 'max_i' in kwargs:
        max_i = kwargs.max_i
    else:
        max_i = 1/tol

    while abs(x0 - x1) >= tol and abs(y1) >= tol:
        num = y1*(x1 - x0)
        if num == 0:
            return [x1, 0]
        den = y1 - y0
        if den == 0:
            pti = (x0 + x1)/2
        else:
            pti = x1 - num/den
        x0 = x1
        x1 = pti
        y0 = y1
        y1 = f(pti)
        i += 1
        if i > max_i:
            return [x0, -1]

    return [x1, 0]


def bisection(f, x0, x1, tol=0.5e-03):
    """The root of a function.

    Implementation of the bisection methode for approximating the root of
    a function.

    Parameters
    ----------
    f : function
        Function to find the root from.
    x0, x1 : numeric
        Values close to the root. `f(x0)` and `f(x1)` must have
        different signs.
    tol : numeric, *default* 0.5e-3
        Tolerance for the value of the root.

    Returns
    -------
    array
        First value is the root approximation.
        Second value is the exit state of the function: 0 for successfull,
        -1 for exit because `max_i` was reached.

    Exemple
    -------
    If the function `f(x)` is defined as x**2 - 4::

        >>> bisection(f, 1, 3)
        [2.00048828125, 0]

    """
    y0 = f(x0)
    y1 = f(x1)
    if y0 == 0:
        return [x0, 0]
    if y1 == 0:
        return [x1, 0]
    if y0 * y1 > 0:
        return [0, -1]
    if y0 > y1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    k = np.log2((x1 - x0)/(2*tol))
    i = 0

    while True:
        pti = (x0 + x1)/2

        if f(pti) > 0:
            x1 = pti
        else:
            x0 = pti

        if i > k:
            return [pti, 0]
        i += 1


# %% [2] Testing Code
if __name__ == '__main__':
    def f(x):
        """
        A test function that outputs x**2 - 4.
        """
        return x**2 - 4

    A = np.linspace(-2.5, 2.5)

    plt.plot(A, f(A), label='f(x)', linewidth=1)
    plt.plot([-2.5, 2.5], [0, 0], 'g--', linewidth=1)

    secant_root = secant(f, -3, 3)
    bisection_root = bisection(f, 0, 3)

    print(secant_root)
    print(bisection_root)

    if secant_root[1] == 0:
        plt.plot(secant_root[0], f(secant_root[0]), '+r', label='secant')
    if bisection_root[1] == 0:
        plt.plot(bisection_root[0], f(bisection_root[0]), 'xy',
                 label='bissection')
    plt.legend(loc='best')
