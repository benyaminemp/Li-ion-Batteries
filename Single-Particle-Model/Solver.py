import time
import numpy as np
from scipy.optimize import fsolve
import Param, NDParam
import FVM
import Functions

def SPM():
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
        "spm_time": 0
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
    result_bowl["maxit"] = maxit 
    return result_bowl
