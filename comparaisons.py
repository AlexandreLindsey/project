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
    ax = plt.subplot(1, 1, 1)
    plt.plot(sol.t, sol.y[0], label=': CH4', linewidth=1)
    plt.plot(sol.t, sol.y[1], label=': H2O', linewidth=1)
    plt.plot(sol.t, sol.y[2], label=': H2', linewidth=1)
    plt.plot(sol.t, sol.y[3], label=': CO', linewidth=1)
    plt.plot(sol.t, sol.y[4], label=': CO2', linewidth=1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1.1), frameon=False)

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

        legend = 'us: ' + str(round_(i, 0.5))
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

    # Number of outputs:
    # Step: 1e-4, outputs: 2909
    # Step: 1e-5, outputs: 29007
    X = np.zeros((PARAM.size, 29007))
    Y0 = np.zeros((PARAM.size, 29007))
    Y1 = np.zeros((PARAM.size, 29007))
    Y2 = np.zeros((PARAM.size, 29007))
    Y3 = np.zeros((PARAM.size, 29007))
    Y4 = np.zeros((PARAM.size, 29007))
    Y6 = np.zeros((PARAM.size, 29007))
    Z = np.zeros((PARAM.size, 29007))
    for i in range(PARAM.size):
        print('3D Ode mode 2, param ' + str(PARAM[i]) + ':', end=' ')
        sol = solve_ivp(lambda x, y: ode(x, y, 2, PARAM[i]), x_int, C0,
                        max_step=1e-5, min_step=1e-5)
        print('completed.')
        print(sol.t.size)

        X[i] = sol.t
        Y0[i] = sol.y[0]
        Y1[i] = sol.y[1]
        Y2[i] = sol.y[2]
        Y3[i] = sol.y[3]
        Y4[i] = sol.y[4]
        Y6[i] = sol.y[6]
        Z[i] = np.full(29007, PARAM[i])

    xticks = np.arange(0, np.max(X)+0.05, 0.05)
    y0ticks = np.arange(0.002, np.max(Y0)+0.002, 0.002)
    y1ticks = np.arange(0.02, np.max(Y1)+0.0028, 0.0028)
    y2ticks = np.arange(0, np.max(Y2)+0.005, 0.005)
    y3ticks = np.arange(0, np.max(Y3)+0.0006, 0.0006)
    y4ticks = np.arange(0, np.max(Y4)+0.0008, 0.0008)
    y6ticks = np.arange(850, np.max(Y6)+24, 24)
    zticks = np.arange(0, np.max(Z)+0.005, 0.005)
    empty_labels_x = ["" for i in range(len(xticks))]
    empty_labels_y0 = ["" for i in range(len(y0ticks))]
    empty_labels_y1 = ["" for i in range(len(y1ticks))]
    empty_labels_y2 = ["" for i in range(len(y2ticks))]
    empty_labels_y3 = ["" for i in range(len(y3ticks))]
    empty_labels_y4 = ["" for i in range(len(y4ticks))]
    empty_labels_y6 = ["" for i in range(len(y6ticks))]
    empty_labels_z = ["" for i in range(len(zticks))]

    fig = plt.figure(23)
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(X, Z, Y0)
    ax.set_xticks(xticks, empty_labels_x)
    ax.set_yticks(zticks, empty_labels_z)
    ax.set_zticks(y0ticks, empty_labels_y0)
    plt.show()

    fig = plt.figure(24)
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(X, Z, Y1)
    ax.set_xticks(xticks, empty_labels_x)
    ax.set_yticks(zticks, empty_labels_z)
    ax.set_zticks(y1ticks, empty_labels_y1)
    plt.show()

    fig = plt.figure(25)
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(Z, Y2, X)
    ax.set_xticks(zticks, empty_labels_z)
    ax.set_yticks(y2ticks, empty_labels_y2)
    ax.set_zticks(xticks, empty_labels_x)
    plt.show()

    fig = plt.figure(26)
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(Z, -X, -Y3)
    ax.set_xticks(zticks, empty_labels_z)
    ax.set_yticks(-xticks, empty_labels_x)
    ax.set_zticks(-y3ticks, empty_labels_y3)
    plt.show()

    fig = plt.figure(27)
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(Z, Y4, X)
    ax.set_xticks(zticks, empty_labels_z)
    ax.set_yticks(y4ticks, empty_labels_y4)
    ax.set_zticks(xticks, empty_labels_x)
    plt.show()

    fig = plt.figure(28)
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(X, Z, Y6)
    ax.set_xticks(xticks, empty_labels_x)
    ax.set_yticks(zticks, empty_labels_z)
    ax.set_zticks(y6ticks, empty_labels_y6)
    plt.show()

    PARAM = np.array([0.5, 1, 1.5, 3])
    for i in PARAM:
        print('Ode mode 3, param ' + str(i) + ':', end=' ')
        sol = solve_ivp(lambda x, y: ode(x, y, 3, i), x_int, C0, rtol=0.5e-6)
        print('completed.')

        legend = 'ug: ' + str(round_(i, 0.5))
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
