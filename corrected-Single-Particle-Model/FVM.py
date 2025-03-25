import numpy as np
import Param, NDParam
import Functions

r = np.linspace(0, 1, Param.params["M"]) # Grid # r Direction
dr = 1 / (Param.params["M"] - 1)
x = np.linspace(0, 1, Param.params["O"]) # X Direction
dx = 1 / (Param.params["O"] - 1)

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


# Define the function for solving the ODE system for c

def root2(unew, uold, t, dt):
    # Electrolyte
    cnew = unew[:Param.params["O"]]
    cold = uold[:Param.params["O"]]
    phi  = unew[Param.params["O"]:Param.params["O"]*2]

    cnewm = np.array([np.nan] + list(cnew) + [np.nan])
    cnewl = np.array([np.nan, np.nan] + list(cnew))
    cnewr = np.array(list(cnew) + [np.nan, np.nan])
    coldm = np.array([np.nan] + list(cold) + [np.nan])

    phim = np.array([np.nan] + list(phi) + [np.nan])
    phil = np.array([np.nan, np.nan] + list(phi))
    phir = np.array(list(phi) + [np.nan, np.nan])

    thing1 = cnewm - coldm - NDParam.params["dt"] / (dx * Param.params["epsilonL"] * NDParam.params["Na"]) * \
        (NDParam.params["B"] * Functions.D_c((cnewm + cnewr) / 2) * (cnewr - cnewm) / dx - NDParam.params["Gamma"] * (1 - Param.params["tplus"]) * \
        NDParam.params["P"] * Functions.kappa((cnewm + cnewr) / 2) * NDParam.params["B"] * ((phir - phim) / dx - 4 * (1 - Param.params["tplus"]) / (cnewr + cnewm) * \
        (cnewr - cnewm) / dx) - (NDParam.params["B"] * Functions.D_c((cnewm + cnewl) / 2) * (cnewm - cnewl) / dx - NDParam.params["Gamma"] * (1 - Param.params["tplus"]) * \
        NDParam.params["P"] * Functions.kappa((cnewl + cnewm) / 2) * NDParam.params["B"] * ((phim - phil) / dx - 4 * (1 - Param.params["tplus"]) / (cnewm + cnewl) * \
        (cnewm - cnewl) / dx)))

    thing2 = -NDParam.params["P"] * Functions.kappa((cnewr + cnewm) / 2) * NDParam.params["B"] * ((phir - phim) / dx - 4 * (1 - Param.params["tplus"]) / (cnewr + cnewm) * (cnewr - cnewm) / dx) \
        - (-NDParam.params["P"] * Functions.kappa((cnewm + cnewl) / 2) * NDParam.params["B"] * ((phim - phil) / dx - 4 * (1 - Param.params["tplus"]) / (cnewm + cnewl) * (cnewm - cnewl) / dx)) - NDParam.params["G"] * NDParam.params["b0"] * dx 

    F = np.zeros(2 * Param.params["O"])

    # Internal points
    F[1:Param.params["O"] - 1] = thing1[2:-2]
    F[Param.params["O"]+1:Param.params["O"] + Param.params["O"] - 1] = thing2[2:-2]

    # Left BCs
    F[0] = cnew[0] - cold[0] - NDParam.params["dt"] / (dx * Param.params["epsilonL"] * NDParam.params["Na"]) * (NDParam.params["B"] * Functions.D_c((cnew[1] + cnew[0]) / 2) * (cnew[1] - cnew[0]) / dx - NDParam.params["Gamma"] * (1 - Param.params["tplus"]) * NDParam.params["P"] * Functions.kappa((cnew[0] + cnew[1]) / 2) * NDParam.params["B"] * ((phi[1] - phi[0]) / dx - 4 * (1 - Param.params["tplus"]) / (cnew[1] + cnew[0]) * (cnew[1] - cnew[0]) / dx))
    F[Param.params["O"]] = phi[0]

    # Right BCs
    F[Param.params["O"] - 1] = -(NDParam.params["B"] * Functions.D_c((cnew[-1] + cnew[-2]) / 2) * (cnew[-1] - cnew[-2]) / dx - NDParam.params["Gamma"] * (1 - Param.params["tplus"]) * NDParam.params["P"] * Functions.kappa((cnew[-2] + cnew[-1]) / 2) * NDParam.params["B"] * ((phi[-1] - phi[-2]) / dx - 4 * (1 - Param.params["tplus"]) / (cnew[-1] + cnew[-2]) * (cnew[-1] - cnew[-2]) / dx))
    F[Param.params["O"] + Param.params["O"] - 1] = 0 - (-NDParam.params["P"] * Functions.kappa((cnew[-2] + cnew[-1]) / 2) * NDParam.params["B"] * ((phi[-1] - phi[-2]) / dx - 4 * (1 - Param.params["tplus"]) / (cnew[-1] + cnew[-2]) * (cnew[-1] - cnew[-2]) / dx)) - NDParam.params["G"] * NDParam.params["b0"] * dx

    return F

