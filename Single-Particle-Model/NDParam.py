import Param
# Compute non-dimensional parameters using primary parameters
params = {
    "dt": 1e-3,
    "B": Param.params["epsilonL"]**1.5,                # Permeability factor of electrolyte
    # Discharge timescale [s]
    "tau": 3*((Param.params["A"] * Param.params["L"] * Param.params["F"]) / abs(Param.params["I0"]))*( Param.params["csmax"] * Param.params["epsilonS"]), 
    # Nondimensional Coefficient of Diffusion Eq (First Particle)
    "Q": Param.params["R0"] ** 2 * abs(Param.params["I0"])/ 
         (Param.params["Ds"] * Param.params["A"] * Param.params["L"] * Param.params["F"] * (Param.params["csmax"] * 3 * Param.params["epsilonS"] / Param.params["R0"] * Param.params["R0"])),
    "I0": abs(Param.params["I0"])/Param.params["I0"],
    "R0": 1,
    "b0": 1,
    "L": 1,
    "csmax": 1,
    "G": abs(Param.params["I0"])/Param.params["I0"]
}