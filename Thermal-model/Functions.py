import numpy as np
import Param, ParamF

def i_current(t):
    return abs(Param.params["I_0"]) if t <= 2880 else Param.params["I_0"]

def qdot(t, r):
    sig_eff = (Param.params["sigma_a"] * ParamF.params["X"] + Param.params["sigma_c"] * ParamF.params["X"]) / (ParamF.params["X"] + ParamF.params["X"])
    A2 = Param.params["N"] * np.pi * ParamF.params["X"] * (3 * ParamF.params["X"] + ParamF.params["R"])
    I = i_current(t)
    qd = (1 / sig_eff) * I ** 2 * A2 * r ** 2 / 2
    return qd