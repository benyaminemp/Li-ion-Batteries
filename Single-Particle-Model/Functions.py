import numpy as np
import Param, NDParam

def Ds_cs(cs):
    """ Solid-phase diffusion coefficient for cathode material with Arrhenius temperature dependence. """
    x = cs / NDParam.params["csmax"]
    x = np.clip(x, 0, 1)  # Ensure x is in [0,1] range
    Ds_cs_296 = 3.7e-13 - 3.4e-13 * np.exp(-12 * (x - 0.62) ** 2)
    return Ds_cs_296 * np.exp(-80600 / (Param.params["R"] * Param.params["T"])) * np.exp(80600 / (Param.params["R"] * 296)) / Param.params["Ds"]

def Ueq_cathode(cs):
    """ Equilibrium potential for cathode material. """
    x = cs / NDParam.params["csmax"]
    a = -2.35211; c = 0.0747061; d = 31.886; e = 0.0219921
    g = 0.640243; h = 5.48623; i = 0.439245; j = 3.82383
    k = 4.12167; m = 0.176187; n = 0.0542123; o = 18.2919
    p = 0.762272; q = 4.23285; r = -6.34984; s = 2.66395
    t = 0.174352

    return a*x - c*np.tanh(d*(x-e)) - r*np.tanh(s*(x-t)) - g*np.tanh(h*(x-i)) - j*np.tanh(k*(x-m)) - n*np.tanh(o*(x-p)) + q
