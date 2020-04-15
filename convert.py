import numpy as np
from color import *

envir_n = 1
const_c = 2.9979246E8
types = [0, 0, 0, 0, 0, 0]

def k2w(k):
    global envir_n, const_c
    return const_c*k/envir_n
def w2k(w):
    global envir_n, const_c
    return envir_n*w/const_c
def k2f(k):
    return 0.5*k/np.pi
def f2lam(f):
    return 1/f
def lam2k(lam):
    return 2*np.pi/lam
def w2V(w):
    return 0.5*w/np.pi
def V2T(V):
    return 1/V
def T2w(T):
    return 2*np.pi/T

def cmd_convert(cmd):
    global envir_n, const_c
    if len(cmd) < 3:
        print_args_error(cmd[0])
        return -1
    try:    
        if cmd[1] == "k":
            types[0] = float(cmd[2])
        elif cmd[1] == "f":
            types[1] = float(cmd[2])
        elif cmd[1] == "lam":
            types[2] = float(cmd[2])
        elif cmd[1] == "w":
            types[3] = float(cmd[2])
        elif cmd[1] == "V":
            types[4] = float(cmd[2])
        elif cmd[1] == "T":
            types[5] = float(cmd[2])
        elif cmd[1] == "n":
            envir_n = float(cmd[2])
            print("set up new index of refraction = ", cmd[2])
            return
        else:
            property_help(cmd[1])
            return -1
    except:
        print_type_error("prop")
        return -1        
            
    while (not(types[0] and types[1] and types[2] and types[3] and types[4] and types[5])):
            
        if(types[0] and (not types[3])):
            types[3] = k2w(types[0])
        if(types[3] and (not types[0])):
            types[0] = w2k(types[3])  
                
        if(types[0] and (not types[1])):
            types[1] = k2f(types[0])
        if(types[1] and (not types[2])):
            types[2] = f2lam(types[1])
        if(types[2] and (not types[0])):
            types[0] = lam2k(types[2])
            
        if(types[3] and (not types[4])):
            types[4] = w2V(types[3])
        if(types[4] and (not types[5])):
            types[5] = V2T(types[4])
        if(types[5] and (not types[3])):
            types[3] = T2w(types[5])    
        
    for i in range(len(types)):
        types[i] = "{0:.4g}".format(types[i])
    print("index of refraction = ", envir_n)
    print("k = ", types[0], "rad/m, ", "f = ", types[1], "m-1, ", "lam = ", types[2], "m; ")
    print("w = ", types[3], "rad/s, ", "V = ", types[4], "Hz, ",  "T = ", types[5], "s; ")
    for i in range(len(types)):
        types[i] = 0        
                    