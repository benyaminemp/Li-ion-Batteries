import numpy as np
import Param
params = {
    "dt": 57.6,   # time step [s]
    "X":  (Param.params["D"] - Param.params["D_m"]) / (2 * (2 * Param.params["N"] + 1)),
    "dr":  (Param.params["D"] - Param.params["D_m"]) / (2 * (2 * Param.params["N"] + 1)),
    "R":  2 * Param.params["N"] * (Param.params["D"] - Param.params["D_m"]) / (2 * (2 * Param.params["N"] + 1)),
    "a": np.pi / ((Param.params["D"] - Param.params["D_m"]) / (2 * (2 * Param.params["N"] + 1))),
    "hprim": Param.params["h_amb"] * (2 * Param.params["N"] + 1) / (2 * Param.params["N"] + 2),
    "n": 2 * (Param.params["N"] + 1),
    "rin": 2 * (Param.params["D"] - Param.params["D_m"]) / (2 * (2 * Param.params["N"] + 1)),
    "A_a":  Param.params["N"] * np.pi * (Param.params["D"] - Param.params["D_m"]) / (2 * (2 * Param.params["N"] + 1)) * ((Param.params["D"] - Param.params["D_m"]) / (2 * (2 * Param.params["N"] + 1)) + 2 * Param.params["N"] * (Param.params["D"] - Param.params["D_m"]) / (2 * (2 * Param.params["N"] + 1))),
    "A_c":  Param.params["N"] * np.pi * (Param.params["D"] - Param.params["D_m"]) / (2 * (2 * Param.params["N"] + 1)) * (3 * (Param.params["D"] - Param.params["D_m"]) / (2 * (2 * Param.params["N"] + 1)) + 2 * Param.params["N"] * (Param.params["D"] - Param.params["D_m"]) / (2 * (2 * Param.params["N"] + 1)))
}