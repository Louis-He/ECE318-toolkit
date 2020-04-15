import numpy as np
from color import *

def rad_2_deg(theta):
    return theta / np.pi * 180


def deg_2_rad(theta):
    return theta / 180 * np.pi


def get_refractive(ni, nt, theta_i):
    sin_t = ni * np.sin(theta_i) / nt
    if sin_t > 1:
        return -1

    return np.arcsin(sin_t)


##
#   get_fresnal_coef: find fresnal coefficient
#   Input: ni, nt, theta_i(in radius)
#   Return: string, list
#   Comment: string = 'T' or 'N'(whether total internal reflection)
#               if 'T', return list: [phi_te, phi_tm]
#               if 'N', return list: [r_te, t_te, r_tm, t_tm]
#
def get_fresnal_coef(ni, nt, theta_i):
    theta_t = get_refractive(ni, nt, theta_i)

    # Total internal reflection
    if theta_t == -1:
        phi_te = -2 * np.arctan((nt * np.sqrt(np.power(ni * np.sin(theta_i) / nt, 2) - 1)) / (ni * np.cos(theta_i)))
        phi_tm = -2 * np.arctan((ni * np.sqrt(np.power(ni * np.sin(theta_i) / nt, 2) - 1)) / (nt * np.cos(theta_i))) + np.pi

        return ('T', [round(phi_te, 4), round(phi_tm, 4)])
    else:
        r_te = (ni * np.cos(theta_i) - nt * np.cos(theta_t)) / (ni * np.cos(theta_i) + nt * np.cos(theta_t))
        r_tm = (2 * ni * np.cos(theta_i)) / (ni * np.cos(theta_i) + nt * np.cos(theta_t))
        t_te = (-nt * np.cos(theta_i) + ni * np.cos(theta_t)) / (nt * np.cos(theta_i) + ni * np.cos(theta_t))
        t_tm = (2 * ni * np.cos(theta_i)) / (nt * np.cos(theta_i) + ni * np.cos(theta_t))

        return ('N', [round(r_te, 4), round(r_tm, 4), round(t_te, 4), round(t_tm, 4), theta_t])

def cmd_fresnal(cmd):
    # check args length
    if len(cmd) != 4:
        print_args_error(cmd[0])
        return

    # check args type
    ni, nt, theta_i = cmd[1:]
    try:
        ni = float(ni)
        nt = float(nt)

        # support both radius and degree
        if len(theta_i) > 3 and theta_i[-3:] == 'deg':
            theta_i = float(theta_i[:-3])
            theta_i = deg_2_rad(theta_i)
        else:
            theta_i = float(theta_i)

    except:
        print_type_error("fr")
        return -1

    # command start here
    res = get_fresnal_coef(ni, nt, theta_i)
    if (res[0] == 'T'):
        print_to_terminal("WARNING", "Total Internal Reflection")
        print('phi_te: ', res[1][0], '=', round(rad_2_deg(res[1][0]), 3), 'deg\t\tphi_tm: ', res[1][1], '=', round(rad_2_deg(res[1][1]), 3), 'deg')
    else:
        print('theta_t: ', round(res[1][4], 4), '=', round(rad_2_deg(res[1][4]), 3),  'deg')
        print('r_te: ', res[1][0], '\t\tt_te: ', res[1][1])
        print('r_tm: ', res[1][2], '\t\tt_tm: ', res[1][3])

def cmd_finesse(cmd):
    if len(cmd) != 2:
        print_args_error(cmd[0])
        return
    R = cmd[1]
    try:
        if R[-1:] == '%':
            R = float(R[:-1]) / 100.0
        elif float(R) > 1.0:
            finesse_help()
            return -1
        elif float(R) < 0:
            finesse_help()
            return -1
        else:
            R = float(R)
    except:
        print_type_error("fin")
        return -1


    F = (4 * R) / ((1 - R) *(1 - R))
    fin = (np.pi * np.sqrt(F)) / 2
    print('Finesse: ', fin)


if __name__ == '__main__':
    print_to_terminal("OKGREEN", "ECE318 toolkit version " + version)
    print("source code avaliable @ https://github.com/Louis-He/ECE318-toolkit\n")
    print_to_terminal("WARNING",
                      "Degree supported by adding deg to the end, eg. 30deg.\nOtherwise, the toolkit will regard all your inputs as in radius.\n"
                      "percentage(%) expression supported (e.g. 95% == 0.95)")
    print("Type \"help\" to know more about supported commands.\n")

    while (True):
        cmd = input("ECE318_toolkit >> ")
        cmd = cmd.split()

        if len(cmd) <= 0:
            continue

        if cmd[0] == "quit" or cmd[0] == "q":
            exit(0)

        if cmd[0] not in cmdList:
            print_to_terminal("FAIL", "command not found: " + cmd[0])
            continue

        if cmd[0] == "help":
            printhelp(cmd)
        elif cmd[0] == "fr":
            cmd_fresnal(cmd)
        elif cmd[0] == "fin":
            cmd_finesse(cmd)