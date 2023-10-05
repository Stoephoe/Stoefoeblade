import math as m
import numpy as np
import pandas as pd
import sys

U_free = 8
Eff_v = 1
Eff_t = 0.8
Eff_p = 0.8
TSR = 4
D_t = 2
D_r = 1.8
D_h = 0.15
N_seg = 10
Blades = 3
Max_c = 0.15
Min_c = 0.05
Res_c = 100
Rotorfoil = 'Eppler e422'
Max_itt_BEM = 100
nu = 1.51 * 10**-5
rho = 1.25

res = []

def reset_inputs():
    global aa, at, itter1
    aa = 0
    at = 0
    itter1 = 0

def calc(itter, aa, at):
    global res, itter1
    # Perform calculations using the provided inputs
    # ...

    # Store the results in the 'res' list
    res.append([seg, aa, c, Twist, c_opt])

    if itter1 == Max_itt_BEM:
        itter1 = 0
    else:
        itter1 += 1

def blade(seg):
    global res, aa, at, itter1

    def segment(c):
        global res, aa, at, itter1
        # Perform segment-related calculations
        # ...

        itter = np.full((1, Max_itt_BEM), c)
        calc_vec = np.vectorize(calc, excluded=['itter1'])
        calc_vec(itter, aa, at)

    reset_inputs()
    a1 = np.linspace(Min_c, Max_c, Res_c)
    segment_vec = np.vectorize(segment)
    segment_vec(a1)

reset_inputs()
a1 = np.linspace(1, N_seg, N_seg)
blade_vec = np.vectorize(blade)
blade_vec(a1)

res = np.array(res)

df = pd.DataFrame(res, columns=['Segment', 'aa', 'c', 'Twist', 'c_opt'])
print(df)
