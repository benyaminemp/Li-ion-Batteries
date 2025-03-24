import numpy as np
import Param, NDParam
import Functions

r = np.linspace(0, 1, Param.params["M"]) # Grid # r Direction
dr = 1 / (Param.params["M"] - 1)

def root2d(unew, uold, t, dt): # Define the function for solving the ODE system for cs (Electrode - SPM)
    # Extract variables from u and uG
    csnew = unew[:Param.params["M"]]
    csold = uold[:Param.params["M"]]
 
    Rm = np.array([np.nan] + list(r) + [np.nan])
    Rl = np.array([np.nan, np.nan] + list(r))
    Rr = np.array(list(r) + [np.nan, np.nan])

    csnewm = np.array([np.nan] + list(csnew) + [np.nan])
    csnewl = np.array([np.nan, np.nan] + list(csnew))
    csnewr = np.array(list(csnew) + [np.nan, np.nan])
    csoldm = np.array([np.nan] + list(csold) + [np.nan])

    segment = csnewm - csoldm - NDParam.params["dt"] / (Rm**2 * dr + dr**3 / 12) * (1 / (4 * NDParam.params["Q"] * dr)) * (
        Functions.Ds_cs((csnewm + csnewr) / 2) * (Rm + Rr)**2 * (csnewr - csnewm) -
        Functions.Ds_cs((csnewm + csnewl) / 2) * (Rm + Rl)**2 * (csnewm - csnewl)
    )

    F = np.zeros(Param.params["M"])
    # Internal points
    F[1:Param.params["M"]-1] = segment[2:-2]
    # Left BC
    F[0]                = csnew[0] - csold[0] - NDParam.params["dt"] / (dr**3 / 24) * (1 / (4 * NDParam.params["Q"] * dr)) * \
        Functions.Ds_cs((csnew[0] + csnew[1]) / 2) * (r[0] + r[1])**2 * (csnew[1] - csnew[0])
    # Right BC
    F[Param.params["M"]-1]                   = csnew[-1] - csold[-1] - NDParam.params["dt"] / (1 / 3 - 1 / 3 * (1 - dr / 2)**3) * \
        1 / NDParam.params["Q"]  * (-NDParam.params["Q"] * NDParam.params["G"] - 1 / (4 * dr) * Functions.Ds_cs((csnew[-1] + csnew[-2]) / 2) * (r[-1] + r[-2])**2 * (csnew[-1] - csnew[-2]))
    return F


