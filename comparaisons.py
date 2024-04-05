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
    PARAM2 = np.array([0.001, 0.005, 0.01, 0.02, 0.025])
    PARAM3 = np.array([1, 1.5, 2, 2.5, 3])
    C_ = np.array([[1/4/22.4, 3/4/22.4, 1e-5, 0, 0, 0, c.TW(), 3],
                   [1/3/22.4, 2/3/22.4, 1e-5, 0, 0, 0, c.TW(), 3],
                   [1/2/22.4, 1/2/22.4, 1e-5, 0, 0, 0, c.TW(), 3],
                   [2/3/22.4, 1/3/22.4, 1e-5, 0, 0, 0, c.TW(), 3],
                   [3/4/22.4, 1/4/22.4, 1e-5, 0, 0, 0, c.TW(), 3]])
    graph_3D = False
    step = 1e-4
    arr_size = 2911
    # step = 1e-5
    # arr_size = 29011

    print('Ode mode 0:', end=' ')
    sol = solve_ivp(lambda x, y: ode(x, y, 0), x_int, C0, rtol=0.5e-6)
    print('completed.')

    plt.figure(1)
    ax = plt.subplot(1, 1, 1)
    plt.plot(sol.t, sol.y[0], label=': CH4', linewidth=1)
    plt.plot(sol.t, sol.y[2], label=': H2', linewidth=1)
    plt.plot(sol.t, sol.y[3], label=': CO', linewidth=1)
    plt.plot(sol.t, sol.y[4], label=': CO2', linewidth=1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1.1), frameon=False)
    plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])

    plt.figure(2)
    ax = plt.subplot(1, 1, 1)
    plt.plot(sol.t, sol.y[6], label='T', linewidth=1)
    plt.xlabel('z (m)')
    plt.ylabel('Temperature (K)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1.1), frameon=False)

    plt.show()
    print(sol.y[0][-1])
    print(sol.y[2][-1])
    print(sol.y[3][-1])
    print(sol.y[4][-1])
    print(sol.y[6][-1])

    print('Ode mode 1:', end=' ')
    sol = solve_ivp(lambda x, y: ode(x, y, 1), x_int, C0, rtol=0.5e-6)
    print('completed.')

    plt.figure(3)
    ax = plt.subplot(1, 1, 1)
    plt.plot(sol.t, sol.y[0], label='CH4', linewidth=1)
    plt.plot(sol.t, sol.y[2], label='H2', linewidth=1)
    plt.plot(sol.t, sol.y[3], label='CO', linewidth=1)
    plt.plot(sol.t, sol.y[4], label='CO2', linewidth=1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1.1), frameon=False)
    plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])

    plt.figure(4)
    ax = plt.subplot(1, 1, 1)
    plt.plot(sol.t, sol.y[6], label='T', linewidth=1)
    plt.xlabel('z (m)')
    plt.ylabel('Temperature (K)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1.1), frameon=False)

    plt.show()
    print(sol.y[0][-1])
    print(sol.y[2][-1])
    print(sol.y[3][-1])
    print(sol.y[4][-1])
    print(sol.y[6][-1])

    for i in PARAM2:
        print('Ode mode 2, param ' + str(i) + ':', end=' ')
        sol = solve_ivp(lambda x, y: ode(x, y, 2, i), x_int, C0, rtol=0.5e-6)
        print('completed.')

        legend = 'us: ' + str(round_(i, 0.5))
        plt.figure(5)
        plt.plot(sol.t, sol.y[0], label=legend, linewidth=1)
        plt.figure(7)
        plt.plot(sol.t, sol.y[2], label=legend, linewidth=1)
        plt.figure(8)
        plt.plot(sol.t, sol.y[3], label=legend, linewidth=1)
        plt.figure(9)
        plt.plot(sol.t, sol.y[4], label=legend, linewidth=1)
        plt.figure(10)
        plt.plot(sol.t, sol.y[6], label=legend, linewidth=1)

    plt.figure(5)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CH4 (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1.1), frameon=False)
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(7)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: H2 (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='lower right', bbox_to_anchor=(1, 0), frameon=False)
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(8)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CO (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='lower right', bbox_to_anchor=(1, 0), frameon=False)
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(9)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CO2 (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='lower right', bbox_to_anchor=(1, 0), frameon=False)
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(10)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Temperature (K)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1.1), frameon=False)

    plt.show()

    for i in PARAM3:
        print('Ode mode 3, param ' + str(i) + ':', end=' ')
        sol = solve_ivp(lambda x, y: ode(x, y, 3, i), x_int, C0, rtol=0.5e-6)
        print('completed.')

        legend = 'ug: ' + str(round_(i, 0.5))
        plt.figure(11)
        plt.plot(sol.t, sol.y[0], label=legend, linewidth=1)
        plt.figure(13)
        plt.plot(sol.t, sol.y[2], label=legend, linewidth=1)
        plt.figure(14)
        plt.plot(sol.t, sol.y[3], label=legend, linewidth=1)
        plt.figure(15)
        plt.plot(sol.t, sol.y[4], label=legend, linewidth=1)
        plt.figure(16)
        plt.plot(sol.t, sol.y[6], label=legend, linewidth=1)

    plt.figure(11)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CH4 (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1.1), frameon=False)
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(13)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: H2 (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='lower right', bbox_to_anchor=(1, 0), frameon=False)
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(14)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CO (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='lower right', bbox_to_anchor=(1, 0), frameon=False)
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(15)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CO2 (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='lower right', bbox_to_anchor=(1, 0), frameon=False)
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(16)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Temperature (K)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1.1), frameon=False)

    plt.show()

    for C0_ in C_:
        print('Ode with H2O/CH4 = ' + str(round((C0_[1]/C0_[0])*10)/10)
              + ':', end=' ')
        sol = solve_ivp(lambda x, y: ode(x, y, 0), x_int, C0_, rtol=0.5e-6)
        print('completed.')

        legend = 'H20/CH4: ' + str(round((C0_[1]/C0_[0])*10)/10)
        plt.figure(17)
        plt.plot(sol.t, sol.y[0], label=legend, linewidth=1)
        plt.figure(19)
        plt.plot(sol.t, sol.y[2], label=legend, linewidth=1)
        plt.figure(20)
        plt.plot(sol.t, sol.y[3], label=legend, linewidth=1)
        plt.figure(21)
        plt.plot(sol.t, sol.y[4], label=legend, linewidth=1)
        plt.figure(22)
        plt.plot(sol.t, sol.y[6], label=legend, linewidth=1)

    plt.figure(17)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CH4 (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1.15), frameon=False)
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(19)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: H2 (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='lower right', bbox_to_anchor=(1, 0), frameon=False)
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(20)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CO (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='lower right', bbox_to_anchor=(1, 0), frameon=False)
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(21)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Concentrations: CO2 (mol/L)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='lower right', bbox_to_anchor=(1, -0.04), frameon=False)
    # plt.axis([0, round_(c.dim('l'), 0.5), 0, round_(max(C0[:5]), 0.5)])
    plt.figure(22)
    ax = plt.subplot(1, 1, 1)
    plt.xlabel('z (m)')
    plt.ylabel('Temperature (K)')
    ax.spines[['right', 'top']].set_visible(False)
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1.1), frameon=False)

    plt.show()

    if graph_3D:
        X = np.zeros((PARAM2.size, arr_size))
        Y0 = np.zeros((PARAM2.size, arr_size))
        Y1 = np.zeros((PARAM2.size, arr_size))
        Y2 = np.zeros((PARAM2.size, arr_size))
        Y3 = np.zeros((PARAM2.size, arr_size))
        Y4 = np.zeros((PARAM2.size, arr_size))
        Y6 = np.zeros((PARAM2.size, arr_size))
        Z = np.zeros((PARAM2.size, arr_size))
        for i in range(PARAM2.size):
            print('3D | Ode mode 2, param ' + str(PARAM2[i]) + ':', end=' ')
            sol = solve_ivp(lambda x, y: ode(x, y, 2, PARAM2[i]), x_int, C0,
                            max_step=step, min_step=step)
            print('completed.')

            arr = np.full(arr_size, sol.t[-1])
            arr[:sol.t.size] = sol.t
            X[i] = arr
            arr = np.full(arr_size, sol.y[0][-1])
            arr[:sol.y[0].size] = sol.y[0]
            Y0[i] = arr
            arr = np.full(arr_size, sol.y[1][-1])
            arr[:sol.y[1].size] = sol.y[1]
            Y1[i] = arr
            arr = np.full(arr_size, sol.y[2][-1])
            arr[:sol.y[2].size] = sol.y[2]
            Y2[i] = arr
            arr = np.full(arr_size, sol.y[3][-1])
            arr[:sol.y[3].size] = sol.y[3]
            Y3[i] = arr
            arr = np.full(arr_size, sol.y[4][-1])
            arr[:sol.y[4].size] = sol.y[4]
            Y4[i] = arr
            arr = np.full(arr_size, sol.y[6][-1])
            arr[:sol.y[6].size] = sol.y[6]
            Y6[i] = arr
            Z[i] = np.full(arr_size, PARAM2[i])

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
        fig = plt.figure(24)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(X, Z, Y1)
        ax.set_xticks(xticks, empty_labels_x)
        ax.set_yticks(zticks, empty_labels_z)
        ax.set_zticks(y1ticks, empty_labels_y1)
        fig = plt.figure(25)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(Z, Y2, X)
        ax.set_xticks(zticks, empty_labels_z)
        ax.set_yticks(y2ticks, empty_labels_y2)
        ax.set_zticks(xticks, empty_labels_x)
        fig = plt.figure(26)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(Z, -X, -Y3)
        ax.set_xticks(zticks, empty_labels_z)
        ax.set_yticks(-xticks, empty_labels_x)
        ax.set_zticks(-y3ticks, empty_labels_y3)
        fig = plt.figure(27)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(Z, Y4, X)
        ax.set_xticks(zticks, empty_labels_z)
        ax.set_yticks(y4ticks, empty_labels_y4)
        ax.set_zticks(xticks, empty_labels_x)
        fig = plt.figure(28)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(X, Z, Y6)
        ax.set_xticks(xticks, empty_labels_x)
        ax.set_yticks(zticks, empty_labels_z)
        ax.set_zticks(y6ticks, empty_labels_y6)

        plt.show()

        X = np.zeros((PARAM3.size, arr_size))
        Y0 = np.zeros((PARAM3.size, arr_size))
        Y1 = np.zeros((PARAM3.size, arr_size))
        Y2 = np.zeros((PARAM3.size, arr_size))
        Y3 = np.zeros((PARAM3.size, arr_size))
        Y4 = np.zeros((PARAM3.size, arr_size))
        Y6 = np.zeros((PARAM3.size, arr_size))
        Z = np.zeros((PARAM3.size, arr_size))
        for i in range(PARAM3.size):
            print('3D | Ode mode 3, param ' + str(PARAM3[i]) + ':', end=' ')
            sol = solve_ivp(lambda x, y: ode(x, y, 3, PARAM3[i]), x_int, C0,
                            max_step=step, min_step=step)
            print('completed.')

            arr = np.full(arr_size, sol.t[-1])
            arr[:sol.t.size] = sol.t
            X[i] = arr
            arr = np.full(arr_size, sol.y[0][-1])
            arr[:sol.y[0].size] = sol.y[0]
            Y0[i] = arr
            arr = np.full(arr_size, sol.y[1][-1])
            arr[:sol.y[1].size] = sol.y[1]
            Y1[i] = arr
            arr = np.full(arr_size, sol.y[2][-1])
            arr[:sol.y[2].size] = sol.y[2]
            Y2[i] = arr
            arr = np.full(arr_size, sol.y[3][-1])
            arr[:sol.y[3].size] = sol.y[3]
            Y3[i] = arr
            arr = np.full(arr_size, sol.y[4][-1])
            arr[:sol.y[4].size] = sol.y[4]
            Y4[i] = arr
            arr = np.full(arr_size, sol.y[6][-1])
            arr[:sol.y[6].size] = sol.y[6]
            Y6[i] = arr
            Z[i] = np.full(arr_size, PARAM3[i])

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

        fig = plt.figure(29)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(X, Z, Y0)
        ax.set_xticks(xticks, empty_labels_x)
        ax.set_yticks(zticks, empty_labels_z)
        ax.set_zticks(y0ticks, empty_labels_y0)
        fig = plt.figure(30)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(X, Z, Y1)
        ax.set_xticks(xticks, empty_labels_x)
        ax.set_yticks(zticks, empty_labels_z)
        ax.set_zticks(y1ticks, empty_labels_y1)
        fig = plt.figure(31)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(Z, Y2, X)
        ax.set_xticks(zticks, empty_labels_z)
        ax.set_yticks(y2ticks, empty_labels_y2)
        ax.set_zticks(xticks, empty_labels_x)
        fig = plt.figure(32)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(Z, -X, -Y3)
        ax.set_xticks(zticks, empty_labels_z)
        ax.set_yticks(-xticks, empty_labels_x)
        ax.set_zticks(-y3ticks, empty_labels_y3)
        fig = plt.figure(33)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(Z, Y4, X)
        ax.set_xticks(zticks, empty_labels_z)
        ax.set_yticks(y4ticks, empty_labels_y4)
        ax.set_zticks(xticks, empty_labels_x)
        fig = plt.figure(34)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(X, Z, Y6)
        ax.set_xticks(xticks, empty_labels_x)
        ax.set_yticks(zticks, empty_labels_z)
        ax.set_zticks(y6ticks, empty_labels_y6)

        plt.show()

        X = np.zeros((C_.size, arr_size))
        Y0 = np.zeros((C_.size, arr_size))
        Y1 = np.zeros((C_.size, arr_size))
        Y2 = np.zeros((C_.size, arr_size))
        Y3 = np.zeros((C_.size, arr_size))
        Y4 = np.zeros((C_.size, arr_size))
        Y6 = np.zeros((C_.size, arr_size))
        Z = np.zeros((C_.size, arr_size))
        for i in range(C_.shape[0]):
            print('3D | Ode with H2O/CH4 = '
                  + str(round((C_[i][1]/C_[i][0])*10)/10) + ':', end=' ')
            sol = solve_ivp(lambda x, y: ode(x, y, 0), x_int, C_[i],
                            max_step=step, min_step=step)
            print('completed.')

            arr = np.full(arr_size, sol.t[-1])
            arr[:sol.t.size] = sol.t
            X[i] = arr
            arr = np.full(arr_size, sol.y[0][-1])
            arr[:sol.y[0].size] = sol.y[0]
            Y0[i] = arr
            arr = np.full(arr_size, sol.y[1][-1])
            arr[:sol.y[1].size] = sol.y[1]
            Y1[i] = arr
            arr = np.full(arr_size, sol.y[2][-1])
            arr[:sol.y[2].size] = sol.y[2]
            Y2[i] = arr
            arr = np.full(arr_size, sol.y[3][-1])
            arr[:sol.y[3].size] = sol.y[3]
            Y3[i] = arr
            arr = np.full(arr_size, sol.y[4][-1])
            arr[:sol.y[4].size] = sol.y[4]
            Y4[i] = arr
            arr = np.full(arr_size, sol.y[6][-1])
            arr[:sol.y[6].size] = sol.y[6]
            Y6[i] = arr
            Z[i] = np.full(arr_size, C_[i][1]/C_[i][0])

        xticks = np.arange(0, np.max(X)+0.05, 0.05)
        y0ticks = np.arange(0, np.max(Y0)+0.007, 0.007)
        y1ticks = np.arange(0, np.max(Y1)+0.007, 0.007)
        y2ticks = np.arange(0, np.max(Y2)+0.005, 0.005)
        y3ticks = np.arange(0, np.max(Y3)+0.0009, 0.0009)
        y4ticks = np.arange(0, np.max(Y4)+0.0008, 0.0008)
        y6ticks = np.arange(840, np.max(Y6)+28, 28)
        zticks = np.arange(0, np.max(Z)+0.005, 0.005)
        empty_labels_x = ["" for i in range(len(xticks))]
        empty_labels_y0 = ["" for i in range(len(y0ticks))]
        empty_labels_y1 = ["" for i in range(len(y1ticks))]
        empty_labels_y2 = ["" for i in range(len(y2ticks))]
        empty_labels_y3 = ["" for i in range(len(y3ticks))]
        empty_labels_y4 = ["" for i in range(len(y4ticks))]
        empty_labels_y6 = ["" for i in range(len(y6ticks))]
        empty_labels_z = ["" for i in range(len(zticks))]

        fig = plt.figure(35)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(X, Z, Y0)
        ax.set_xticks(xticks, empty_labels_x)
        ax.set_yticks(zticks, empty_labels_z)
        ax.set_zticks(y0ticks, empty_labels_y0)
        fig = plt.figure(36)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(X, Z, Y1)
        ax.set_xticks(xticks, empty_labels_x)
        ax.set_yticks(zticks, empty_labels_z)
        ax.set_zticks(y1ticks, empty_labels_y1)
        fig = plt.figure(37)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(Z, Y2, X)
        ax.set_xticks(zticks, empty_labels_z)
        ax.set_yticks(y2ticks, empty_labels_y2)
        ax.set_zticks(xticks, empty_labels_x)
        fig = plt.figure(38)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(Z, -X, -Y3)
        ax.set_xticks(zticks, empty_labels_z)
        ax.set_yticks(-xticks, empty_labels_x)
        ax.set_zticks(-y3ticks, empty_labels_y3)
        fig = plt.figure(39)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(Z, Y4, X)
        ax.set_xticks(zticks, empty_labels_z)
        ax.set_yticks(y4ticks, empty_labels_y4)
        ax.set_zticks(xticks, empty_labels_x)
        fig = plt.figure(40)
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(X, Z, Y6)
        ax.set_xticks(xticks, empty_labels_x)
        ax.set_yticks(zticks, empty_labels_z)
        ax.set_zticks(y6ticks, empty_labels_y6)

        plt.show()
