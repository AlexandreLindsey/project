"""FILE_DESCRIPTION

Credits
-------
Created on Fri Mar 15 12:16:00 2024

@author: Lindsey Alexandre S2302371
@credits: Luca Odding S2303933, Raffaele Moreci S2304531
"""

# %% [0] Imports
# Third-party librairy imports.
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp

# Local module imports
import constants as c
from odefunction import odefunction as ode

# %% [1] Main Code


# %% [2] Testing Code
if __name__ == '__main__':
    C0 = [1/4/22.4, 3/4/22.4, 1e-5, 0, 0, 0, c.TW(), c.P('tot', 0)]
    x_int = [0, c.dim('l')]

    sol = solve_ivp(lambda x, y: ode(x, y, 0), x_int, C0, rtol=0.5e-6)

    print('Ode mode 0:')

    plt.figure()
    plt.plot(sol.t, sol.y[0], label='CH4', linewidth=1)
    plt.plot(sol.t, sol.y[1], label='H2O', linewidth=1)
    plt.plot(sol.t, sol.y[2], label='H2', linewidth=1)
    plt.plot(sol.t, sol.y[3], label='CO', linewidth=1)
    plt.plot(sol.t, sol.y[4], label='CO2', linewidth=1)
    plt.ylabel('z')
    plt.ylabel('Concentrations')
    plt.legend(loc='best')

    figure, axis = plt.subplots(2, 2)

    axis[0, 1].plot(sol.t, sol.y[5], label='X', linewidth=1)
    axis[0, 1].set_title('Conversion fractionnaire')

    axis[1, 0].plot(sol.t, sol.y[6], label='T', linewidth=1)
    axis[1, 0].set_title('Temperature')

    axis[1, 1].plot(sol.t, sol.y[7], label='P', linewidth=1)
    axis[1, 1].set_title('Pression')

    sol = solve_ivp(lambda x, y: ode(x, y, 1), x_int, C0, rtol=0.5e-6)

    print('Ode mode 1:')

    plt.figure()
    plt.plot(sol.t, sol.y[0], label='CH4', linewidth=1)
    plt.plot(sol.t, sol.y[1], label='H2O', linewidth=1)
    plt.plot(sol.t, sol.y[2], label='H2', linewidth=1)
    plt.plot(sol.t, sol.y[3], label='CO', linewidth=1)
    plt.plot(sol.t, sol.y[4], label='CO2', linewidth=1)
    plt.ylabel('z')
    plt.ylabel('Concentrations')
    plt.legend(loc='best')

    figure, axis = plt.subplots(2, 2)

    axis[0, 1].plot(sol.t, sol.y[5], label='X', linewidth=1)
    axis[0, 1].set_title('Conversion fractionnaire')

    axis[1, 0].plot(sol.t, sol.y[6], label='T', linewidth=1)
    axis[1, 0].set_title('Temperature')

    axis[1, 1].plot(sol.t, sol.y[7], label='P', linewidth=1)
    axis[1, 1].set_title('Pression')

    PARAM = np.arange(0.01, 0.1, 0.01)
    for i in PARAM:
        sol = solve_ivp(lambda x, y: ode(x, y, 2, i), x_int, C0, rtol=0.5e-6)

        print('Ode mode 2, param ' + str(i) + ':')

        plt.figure()
        plt.plot(sol.t, sol.y[0], label='CH4', linewidth=1)
        plt.plot(sol.t, sol.y[1], label='H2O', linewidth=1)
        plt.plot(sol.t, sol.y[2], label='H2', linewidth=1)
        plt.plot(sol.t, sol.y[3], label='CO', linewidth=1)
        plt.plot(sol.t, sol.y[4], label='CO2', linewidth=1)
        plt.ylabel('z')
        plt.ylabel('Concentrations')
        plt.legend(loc='best')

        figure, axis = plt.subplots(2, 2)

        axis[0, 1].plot(sol.t, sol.y[5], label='X', linewidth=1)
        axis[0, 1].set_title('Conversion fractionnaire')

        axis[1, 0].plot(sol.t, sol.y[6], label='T', linewidth=1)
        axis[1, 0].set_title('Temperature')

        axis[1, 1].plot(sol.t, sol.y[7], label='P', linewidth=1)
        axis[1, 1].set_title('Pression')
