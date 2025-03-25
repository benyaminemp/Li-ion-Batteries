import time
import numpy as np
from scipy.optimize import fsolve
import Param, NDParam
import FVM
import Functions

def cSPM():
    """Solves the SPM model and saves results in the result bowl."""
    # Initialize Variables
    result_bowl = {
        "cs": [], 
        "G": [],
        "C": [],
        "Ueq": [],
        "tnew": [], 
        "V_spm": [],
        "maxit": None,
        "c": None, 
        "phi": None,
        "JJ": None, 
        "FF": None,
        "V_cspm": None,
        "spm_time": 0,
        "cspm_time": 0
    }
    
    ## 🔹 **SPM Calculation**
    uold = [Param.params["csinit"]] * Param.params["M"]
    t = 0
    maxit = 0
    ts = [] 
    spm_start_time = time.time()
    while True:
        def fun(unew):
            return FVM.root2d(unew, uold, t, NDParam.params["dt"])
        unew = fsolve(fun, uold)
        result_bowl["cs"].append(unew[:Param.params["M"]])
        result_bowl["C"].append(unew[Param.params["M"]-1])
        maxit += 1
        if np.max(unew[:Param.params["M"]]) > 0.975:
            break
        uold = unew
        ts.append(t)
        t += NDParam.params["dt"]

    # Compute Ueq & V_spm
    for i in range(len(ts)):
        result_bowl["Ueq"].append(Functions.Ueq_cathode(result_bowl["C"][i]))
        result_bowl["tnew"].append(ts[i] * NDParam.params["tau"] / 3600)

    result_bowl["V_spm"] = result_bowl["Ueq"]
    spm_end_time = time.time()
    result_bowl["spm_time"] = spm_end_time - spm_start_time
    ## 🔹 **cSPM Calculation**
    t = 0
    wold = np.zeros(2 * Param.params["O"])
    wold[0:Param.params["O"]] = 1
    wold[Param.params["O"]:Param.params["O"] + Param.params["O"]] = 0
    c = np.zeros((maxit, Param.params["O"]))
    phi = np.zeros((maxit, Param.params["O"]))
    dphidx = np.zeros((maxit, Param.params["O"]-1))
    dcdx = np.zeros((maxit, Param.params["O"]-1))
    JJ = np.zeros((maxit, Param.params["O"]-1))
    FF = np.zeros((maxit, Param.params["O"]-1))
    x = np.linspace(0, 1, Param.params["O"])

    cspm_start_time = time.time()

    for j in range(maxit):
        t += NDParam.params["dt"]
        def fun(wnew):
            return FVM.root2(wnew, wold, t, NDParam.params["dt"])
        wnew = fsolve(fun, wold)
        c[j, :] = wnew[:Param.params["O"]]
        phi[j, :] = wnew[Param.params["O"]:]
        wold = wnew
    
    result_bowl["V_cspm"] = np.zeros(maxit-2)
    # Calculate dphidx and dcdx
    for i in range(maxit):
        dphidx[i, :] = (phi[i, 1:] - phi[i, :-1]) / (x[1] - x[0])
        dcdx[i, :] = (c[i, 1:] - c[i, :-1]) / (x[1] - x[0])
    for i in range(maxit-1):
        JJ[i, :] = -NDParam.params["B"]  * NDParam.params["P"]  * Functions.kappa(c[i,1:]) * (dphidx[i, :] - 2 * (1 - Param.params["tplus"]) * dcdx[i, :] / c[i, 1:])
        FF[i, :] = -NDParam.params["B"]  * Functions.D_c(c[i,1:]) * dcdx[i, :] - NDParam.params["Gamma"] * (1 - Param.params["tplus"]) * JJ[i, :]
    
    # cSPM (Corrected V) calculation
    for i in range(maxit-2):
        int_js = 1 / (2 * NDParam.params["Teta"] * Param.params["sigma"]) + NDParam.params["B"]* Functions.kappa(c[i,Param.params["O"]-1]) / (NDParam.params["Teta"] * Param.params["sigma"]) * np.trapz(phi[i, -1] - phi[i, :],x)
        int_phi = np.trapz(phi[i, :],x)
        int_eta = np.trapz(Functions.eta_val(result_bowl["C"][i], c[i,:]),x)
        v1 = int_phi - int_js + int_eta
        result_bowl["V_cspm"][i] = result_bowl["V_spm"][i] + 1 / NDParam.params["lamda"] * v1 
    result_bowl["c"], result_bowl["phi"], result_bowl["JJ"], result_bowl["FF"] = c, phi, JJ, FF   
    cspm_end_time = time.time()

    result_bowl["cspm_time"] = cspm_end_time - cspm_start_time
    result_bowl["maxit"] = maxit 

    return result_bowl
