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
# First-party imports
import math

# Third-party imports
import numpy as np


# %% [1] Main Code
def secant(fun, x, tol=0.5e-03, **kwargs):
    """The root of a function.

    Implementation of the secant method for approximating the root
    of a function.

    Parameters
    ----------
    fun : function
        Function to find the root from.
    x : numeric array
        Values close to the root.
    tol : numeric, *default* 0.5e-3
        Tolerance for the value of the root.

    Other Parameters
    ----------------
    **kwargs : dict, *optional*
        Extra properties. See table below.

        Properties:

    +------------+-----------------------------------------------------------+
    | Name       | Description                                               |
    +============+===========================================================+
    | ``max_i``  | Maximum number of itirations before exiting. The default  |
    |            | is 1 / ``tol``.                                           |
    +------------+-----------------------------------------------------------+
    | ``hybrid`` | ``True`` or ``False``. Whether to strictly use the        |
    |            | secant method or use a hybrid of the secante and          |
    |            | bisection method.                                         |
    +------------+-----------------------------------------------------------+

    Returns
    -------
    array
        First value is the exit state of the function: 0 for successfull,
        1 if there is an error.
        Second value is the root approximation.

    Exemple
    -------
    If the function ``fun(x)`` is defined as x**2 - 4::

        >>> secant(fun, [1, 3])
        [1.9999525931544515, 0]
    """
    i = 0
    # Checks that the inputs x[0] and x[1] have different values.
    # (Within a certain tolerance.)
    if abs(x[0] - x[1]) <= tol:
        print('x[1] et x2 ont la même valeur.')
        return [1]
    # Checks that fun(x[0]) exists.
    try:
        y0 = fun(x[0])
    except ZeroDivisionError:
        print('fun(' + str(x[0]) + ') n\'existe pas')
        return [1]
    # Checks that fun(x[1]) exists.
    try:
        y1 = fun(x[1])
    except ZeroDivisionError:
        print('fun(' + str(x[1]) + ') n\'existe pas')
        return [1]
    # Default value for max_i.
    if 'max_i' in kwargs:
        max_i = kwargs['max_i']
    else:
        max_i = 1/tol
    # Default value for hybrid.
    if 'hybrid' in kwargs:
        hybrid = kwargs['hybrid']
    else:
        hybrid = False

    # Loop until the approximation is almost equal to zero.
    # (Within a certain tolerance.)
    while abs(y1) >= tol:
        # To find the next approximation, we use the function:
        # x[1] - (y1 * (x[1] - x[0])) / (y1 - y0)
        # Firstly, we compute the numerator (num).
        num = y1 * (x[1] - x[0])
        # We check that num is different than zero. If it is not, then x[0] and
        # x[1] must have the same value. Thus, the function must not converge.
        # y1 is not equal to zero as we already checked. (See below.) (If it
        # was 0, it would also be the solution.)
        if num == 0:
            print('La fonction ne converge pas. num: ' + str(num))
            return [-1]
        # Then, we compute the denominator (den).
        den = y1 - y0
        # We check that den is different than zero. If it is not, then y0 and
        # y1 must have the same value. Thus, we can not find an intersection
        # with the x-axis.
        if den == 0:
            # If hybrid is True, then we use the "bisection" method.
            if hybrid:
                xi = (x[0] + x[1])/2
            # Otherwise, the function does not converge.
            else:
                print('La fonction ne converge pas.')
                return [-1]
        else:
            xi = x[1] - num/den
        # We swap the values around.
        x[0] = x[1]
        x[1] = xi
        y0 = y1
        # We calculate fun(xi) and check if it exists.
        try:
            y1 = fun(xi)
        except ZeroDivisionError:
            print('fun(' + str(x[1]) + ') n\'existe pas')
            return [-1]
        i += 1
        # We stop the program if it reaches the maximum number of itirations,
        # max_i.
        if i > max_i:
            print('La fonction n\'a pas convergé après ' + str(i) +
                  ' itérations.')
            return [-1]

    return [0, x[1]]


def bisection(fun, x, tol=0.5e-03):
    """The root of a function.

    Implementation of the bisection method for approximating the root of
    a function.

    Parameters
    ----------
    fun : function
        Function to find the root from.
    x : numeric array
        Values close to the root. ``fun(x[0])`` and ``fun(x[1])`` must have
        different signs.
    tol : numeric, *default* 0.5e-3
        Tolerance for the value of the root.

    Returns
    -------
    array
        First value is the exit state of the function: 0 for successfull,
        1 if there is an error.
        Second value is the root approximation.

    Exemple
    -------
    If the function ``fun(x)`` is defined as x**2 - 4::

        >>> bisection(fun, [1, 3])
        [2.00048828125, 0]

    """
    # Checks that fun(x[0]) exists.
    try:
        y0 = fun(x[0])
    except ZeroDivisionError:
        print('fun(' + str(x[0]) + ') n\'existe pas')
        return [1]
    # Checks that fun(x[1]) exists.
    try:
        y1 = fun(x[1])
    except ZeroDivisionError:
        print('fun(' + str(x[1]) + ') n\'existe pas')
        return [1]
    # Checks if y0 is the solution within a certain tolerance.
    if y0 == 0 or abs(y0) < tol:
        return [0, x[0]]
    # Checks if y1 is the solution within a certain tolerance.
    if y1 == 0 or abs(y1) < tol:
        return [0, x[1]]
    # Checks that y0 and y1 have a different sign (to satisfy the requirements
    # of the method).
    if y0 * y1 > 0:
        print('fun(x[0]) et fun(x[1]) sont du même signe.')
        return [1]
    # Checks that y0 is the negative value. If not, swaps the values of x[0]
    # and x[1].
    if y0 > y1:
        x[0], x[1] = x[1], x[0]

    # Calculates the number of itirations needed to find an approximation good
    # enough (to a tolerance). Formula from the course.
    k = np.log2(abs(x[1] - x[0])/(2*tol))

    # Loop ends at k + 1 because we need to do k itirations (it stops when
    # i = k+1).
    for i in range(math.ceil(k) + 1):
        # Calculates the next approximation of the root.
        xi = (x[0] + x[1])/2
        # Checks that fun(xi) exists.
        try:
            yi = fun(xi)
        except ZeroDivisionError:
            print('f(' + str(xi) + ') n\'existe pas')
            return [-1]
        # If yi is positive, then replace the previous positive value (x[1]).
        if yi > 0:
            x[1] = xi
        # Else, replace the previous negative value (x[0]).
        else:
            x[0] = xi
    return [0, xi]
