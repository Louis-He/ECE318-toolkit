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
#   todo: test this function
def get_fresnal_coef(ni, nt, theta_i):
    theta_t = get_refractive(ni, nt, theta_i)

    # Total internal reflection
    if theta_t == -1:
        phi_te = -2 * np.arctan((nt * np.sqrt(np.power(ni * np.sin(theta_i) / nt, 2) - 1)) / (ni * np.cos(theta_i)))
        phi_tm = -2 * np.arctan((ni * np.sqrt(np.power(ni * np.sin(theta_i) / nt, 2) - 1)) / (nt * np.cos(theta_i))) + np.pi

        return ('T', [phi_te, phi_tm])
    else:
        r_te = (ni * np.cos(theta_i) - nt * np.cos(theta_t)) / (ni * np.cos(theta_i) + nt * np.cos(theta_t))
        r_tm = (2 * ni * np.cos(theta_i)) / (ni * np.cos(theta_i) + nt * np.cos(theta_t))
        t_te = (-nt * np.cos(theta_i) + ni * np.cos(theta_t)) / (nt * np.cos(theta_i) + ni * np.cos(theta_t))
        t_tm = (2 * ni * np.cos(theta_i)) / (nt * np.cos(theta_i) + ni * np.cos(theta_t))

        return ('N', [r_te, r_tm, t_te, t_tm])

cmdList = [
    'fresnal'
]
if __name__ == '__main__':
    print_to_terminal("OKGREEN", "ECE318 toolkit version 0.1")
    print("source code avaliable @ https://github.com/Louis-He/ECE318-toolkit\n")
    while (True):
        cmd = input("ECE318_toolkit >> ")
        cmd = cmd.split()

        if len(cmd) <= 0:
            continue

        if cmd[0] not in cmdList:
            print_to_terminal("FAIL", "command not found: " + cmd[0])
            continue