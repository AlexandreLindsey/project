"""FILE_DESCRIPTION

Credits
-------
Created on Fri Mar 15 12:16:00 2024

@author: Lindsey Alexandre S2302371
@credits: Luca Odding S2303933, Raffaele Moreci S2304531
"""

# %% [0] Imports
import math

# Third-party librairy imports.
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp

# Local module imports
import constants as c
from odefunction import odefunction as ode


# %% [1] Main Code
def round_(x, n=0):
    return round(x/n, -int(math.floor(math.log10(abs(x)))))*n


# %% [2] Testing Code
if __name__ == '__main__':
    C0 = [1/4/22.4, 3/4/22.4, 1e-5, 0, 0, 0, c.TW(), 3]
    x_int = [0, c.dim('l')]

    print('Ode mode 0:', end=' ')
    sol = solve_ivp(lambda x, y: ode(x, y, 0), x_int, C0, rtol=0.5e-6)
    print('completed.')

    plt.figure(1)
    plt.plot(sol.t, sol.y[0], label='CH4', linewidth=1)
    plt.plot(sol.t, sol.y[1], label='H2O', linewidth=1)
    plt.plot(sol.t, sol.y[2], label='H2', linewidth=1)
    plt.plot(sol.t, sol.y[3], label='CO', linewidth=1)
    plt.plot(sol.t, sol.y[4], label='CO2', linewidth=1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations (mol/L)')
    plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.legend(loc='best')

    plt.figure(2)
    plt.plot(sol.t, sol.y[6], label='T', linewidth=1)
    plt.xlabel('z (m)')
    plt.ylabel('Temperature (K)')
    plt.legend(loc='best')

    print('Ode mode 1:', end=' ')
    sol = solve_ivp(lambda x, y: ode(x, y, 1), x_int, C0, rtol=0.5e-6)
    print('completed.')

    plt.figure(3)
    plt.plot(sol.t, sol.y[0], label='CH4', linewidth=1)
    plt.plot(sol.t, sol.y[1], label='H2O', linewidth=1)
    plt.plot(sol.t, sol.y[2], label='H2', linewidth=1)
    plt.plot(sol.t, sol.y[3], label='CO', linewidth=1)
    plt.plot(sol.t, sol.y[4], label='CO2', linewidth=1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations (mol/L)')
    plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.legend(loc='best')

    plt.figure(4)
    plt.plot(sol.t, sol.y[6], label='T', linewidth=1)
    plt.xlabel('z (m)')
    plt.ylabel('Temperature (K)')
    plt.legend(loc='best')

    PARAM = np.array([0.0005, 0.001, 0.005, 0.01, 0.02, 0.025])
    for i in PARAM:
        print('Ode mode 2, param ' + str(i) + ':', end=' ')
        sol = solve_ivp(lambda x, y: ode(x, y, 2, i), x_int, C0, rtol=0.5e-6)
        print('completed.')

        legend = 'us: ' + str(round_(i))
        plt.figure(5)
        plt.plot(sol.t, sol.y[0], label=legend, linewidth=1)
        plt.figure(6)
        plt.plot(sol.t, sol.y[1], label=legend, linewidth=1)
        plt.figure(7)
        plt.plot(sol.t, sol.y[2], label=legend, linewidth=1)
        plt.figure(8)
        plt.plot(sol.t, sol.y[3], label=legend, linewidth=1)
        plt.figure(9)
        plt.plot(sol.t, sol.y[4], label=legend, linewidth=1)
        plt.figure(10)
        plt.plot(sol.t, sol.y[6], label=legend, linewidth=1)

    plt.figure(5)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CH4 (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(6)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: H2O (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(7)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: H2 (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.legend(loc='best')
    plt.figure(8)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CO (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.legend(loc='best')
    plt.figure(9)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CO2 (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.legend(loc='best')
    plt.figure(10)
    plt.xlabel('z (m)')
    plt.ylabel('Temperature (K)')
    plt.legend(loc='best')

    PARAM = np.array([0.5, 1, 1.5, 3])
    for i in PARAM:
        print('Ode mode 3, param ' + str(i) + ':', end=' ')
        sol = solve_ivp(lambda x, y: ode(x, y, 3, i), x_int, C0, rtol=0.5e-6)
        print('completed.')

        legend = 'ug: ' + str(round_(i))
        plt.figure(11)
        plt.plot(sol.t, sol.y[0], label=legend, linewidth=1)
        plt.figure(12)
        plt.plot(sol.t, sol.y[1], label=legend, linewidth=1)
        plt.figure(13)
        plt.plot(sol.t, sol.y[2], label=legend, linewidth=1)
        plt.figure(14)
        plt.plot(sol.t, sol.y[3], label=legend, linewidth=1)
        plt.figure(15)
        plt.plot(sol.t, sol.y[4], label=legend, linewidth=1)
        plt.figure(16)
        plt.plot(sol.t, sol.y[6], label=legend, linewidth=1)

    plt.figure(11)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CH4 (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(12)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: H2O (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(13)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: H2 (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.legend(loc='best')
    plt.figure(14)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CO (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.legend(loc='best')
    plt.figure(15)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CO2 (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.legend(loc='best')
    plt.figure(16)
    plt.xlabel('z (m)')
    plt.ylabel('Temperature (K)')
    plt.legend(loc='best')

    C_ = [[1/4/22.4, 3/4/22.4, 1e-5, 0, 0, 0, c.TW(), 3],
          [2/3/22.4, 1/3/22.4, 1e-5, 0, 0, 0, c.TW(), 3],
          [1/2/22.4, 1/2/22.4, 1e-5, 0, 0, 0, c.TW(), 3],
          [1/3/22.4, 2/3/22.4, 1e-5, 0, 0, 0, c.TW(), 3],
          [3/4/22.4, 1/4/22.4, 1e-5, 0, 0, 0, c.TW(), 3]]
    for C0 in C_:
        print('Ode with C0 = ' + str(C0) + ':', end=' ')
        sol = solve_ivp(lambda x, y: ode(x, y, 0), x_int, C0, rtol=0.5e-6)
        print('completed.')

        legend = 'H20/CH4: ' + str(round((C0[1]/C0[0])*10)/10)
        plt.figure(17)
        plt.plot(sol.t, sol.y[0], label=legend, linewidth=1)
        plt.figure(18)
        plt.plot(sol.t, sol.y[1], label=legend, linewidth=1)
        plt.figure(19)
        plt.plot(sol.t, sol.y[2], label=legend, linewidth=1)
        plt.figure(20)
        plt.plot(sol.t, sol.y[3], label=legend, linewidth=1)
        plt.figure(21)
        plt.plot(sol.t, sol.y[4], label=legend, linewidth=1)
        plt.figure(22)
        plt.plot(sol.t, sol.y[6], label=legend, linewidth=1)

    plt.figure(17)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CH4 (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(18)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: H2O (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(19)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: H2 (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.legend(loc='best')
    plt.figure(20)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CO (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.legend(loc='best')
    plt.figure(21)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CO2 (mol/L)')
    plt.legend(loc='best')
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.legend(loc='best')
    plt.figure(22)
    plt.xlabel('z (m)')
    plt.ylabel('Temperature (K)')
    plt.legend(loc='best')
