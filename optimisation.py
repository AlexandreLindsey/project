"""FILE_DESCRIPTION

Credits
-------
Created on Thu Mar 28 13:25:10 2024

@author: Lindsey Alexandre S2302371
@credits: Luca Odding S2303933, Raffaele Moreci S2304531
"""

# %% [0] Imports
# Third-party librairy imports.
import numpy as np
from scipy.integrate import solve_ivp
from matplotlib import pyplot as plt

# Local module imports
from odefunction import odefunction as ode
import constants as c
from root import secant


# %% [1] Main Code
def optimise_us(Y, us, C0, mode_=2, param1=0):
    if mode_ == 4:
        param_ = [us, param1]
    else:
        param_ = us
    sol = solve_ivp(lambda z, C: ode(z, C, mode=mode_, param=param_),
                    [0, c.dim('l')], C0)
    # Returns the percentage of the concentration of CO_2 among the
    # concentrations of dry gases minus Y.
    # (Cf(CO_2)/Cf(CH_4) + Cf(H_2) + Cf(CO) + Cf(CO_2)) - Y
    return (sol.y[4][-1]/(sol.y[0][-1] + sol.y[2][-1] + sol.y[3][-1]
                          + sol.y[4][-1]) - Y)


# %% [2] Testing Code
if __name__ == '__main__':
    C0 = [1/4/22.4, 3/4/22.4, 1e-5, 0, 0, 0, c.TW(), 3]
    x = [0.01, 0.2]
    Y = 0.075
    A = np.arange(x[0], x[1], 0.005)
    B = np.zeros(A.size)
    C = np.zeros(A.size)
    for i in range(A.size):
        B[i] = optimise_us(Y, A[i], C0)
    plt.figure(1)
    plt.plot(A, B, label='us', linewidth=1)
    plt.plot(A, C, color='black', linewidth=1)
    plt.ylabel('us - Y (m/s)')
    plt.xlabel('% CO_2')
    x0 = secant(lambda us: optimise_us(Y, us, C0), x, tol=0.5e-8,
                hybrid=True)
    y0 = optimise_us(Y, x0[1], C0)
    print(x0)
    plt.plot(x0[1], y0, 'xr')
    plt.show()

    PARAM4 = np.arange(960, 1036, 1)
    D = np.zeros(PARAM4.size)
    x = [0.01, 0.5]
    for i in range(PARAM4.size):
        C0 = [1/4/22.4, 3/4/22.4, 1e-5, 0, 0, 0, PARAM4[i], 3]
        D[i] = secant(lambda us: optimise_us(Y, us, C0, mode_=4,
                      param1=PARAM4[i]), x, tol=0.5e-8, hybrid=True)[1]
        print(str(PARAM4[i]) + ": " + str(D[i]))
    plt.figure(2)
    plt.plot(PARAM4, D, linewidth=1)
    plt.show()
