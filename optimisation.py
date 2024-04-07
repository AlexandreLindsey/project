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
    # Formats odefunctions mode and param correctly
    if mode_ == 4:
        param_ = [us, param1]
    else:
        param_ = us

    # Solves the differential equation for a given us
    sol = solve_ivp(lambda z, C: ode(z, C, mode=mode_, param=param_),
                    [0, c.dim('l')], C0)
    # Returns the CO2 precentage in the output's dry gases for a given us
    # minus Y, the desired target of CO2 precentage in the output's dry gases.
    return (sol.y[4][-1]/(sol.y[0][-1] + sol.y[2][-1] + sol.y[3][-1]
                          + sol.y[4][-1]) - Y)


# %% [2] Testing Code
if __name__ == '__main__':
    # Initial conditions for odefunction.
    C0 = [1/4/22.4, 3/4/22.4, 1e-5, 0, 0, 0, c.TW(), 3]
    # Initial values for the secant methode.
    x = [0.01, 0.2]
    # CO2 percentage to aim for in optimise_us.
    Y = 0.075
    # Values of the x-axis to plot the fonction of optimise_us.
    A = np.arange(x[0], x[1], 0.005)
    # Array to store the y-axis values.
    B = np.zeros(A.size)
    # Array to plot the zero line/the Y line.
    C = np.zeros(A.size)
    # Calculates and stores all of the values of optimise_us.
    for i in range(A.size):
        # If us is close to zero, 
        if A[i] > 1e-8:
            B[i] = optimise_us(Y, A[i], C0)

    # Calculates the optimal us
    x0 = secant(lambda us: optimise_us(Y, us, C0), x, tol=0.5e-8,
                hybrid=True)
    # Calculates the CO2 percentage for the optimal_us (should be equal to Y).
    y0 = optimise_us(Y, x0[1], C0)
    print(x0)

    # Plots the raw results.
    plt.figure(1)
    ax = plt.subplot(1, 1, 1)
    plt.plot(A, B, linewidth=1)
    plt.plot(A, C, color='black', linewidth=1)
    plt.plot(x0[1], y0, 'xr', label=': us optimal')
    plt.xlabel('us (m/s)')
    plt.ylabel('Concentration de CO2 (%) - Y')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1), frameon=False)

    # Plots the results + Y.
    plt.figure(2)
    ax = plt.subplot(1, 1, 1)
    plt.plot(A, B+Y, linewidth=1)
    plt.plot(A, C+Y, color='black', linewidth=1)
    plt.plot(x0[1], y0+Y, 'xr', label=': us optimal')
    plt.xlabel('us (m/s)')
    plt.ylabel('Concentration de CO2 (%)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1), frameon=False)
    plt.show()

    # Array of the temperture range to find an optimal us in.
    PARAM4 = np.arange(960, 1036, 1)
    # Array to stock the optimal us values in.
    D = np.zeros(PARAM4.size)
    # Initial values for the secant methode.
    x = [0.01, 0.5]
    # Calculates and stores all of the optimal us.
    for i in range(PARAM4.size):
        C0 = [1/4/22.4, 3/4/22.4, 1e-5, 0, 0, 0, PARAM4[i], 3]
        D[i] = secant(lambda us: optimise_us(Y, us, C0, mode_=4,
                      param1=PARAM4[i]), x, tol=0.5e-8, hybrid=True)[1]
        print(str(PARAM4[i]) + ': ' + str(D[i]))

    # Plots the results of the effects of the temperture on the optimal us.
    plt.figure(3)
    ax = plt.subplot(1, 1, 1)
    plt.plot(PARAM4, D, linewidth=1)
    plt.xlabel('Temperature (K)')
    plt.ylabel('us (m/s)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.show()
