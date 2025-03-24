import numpy as np
params = {
    # Constants
    "crate": 1,         # C rate of the half cell
    "I0": -0.15625,     # Current [A] (Filling the Particle)
    "M": 10,            # Mesh size of the Particle
    "F": 96485.3329,    # Faraday Constant [sA/mol]
    "L": 54e-6,      # Thickness of electrode [m]
    "A": 8.585e-3 ,     # Electrode Cross Section [m^2]
    "epsilonL": 0.296,  # Vol. fraction of Electrolyte
    "T": 298.15,        # Absolute Temperature [K]
    "R": 8.3144,        # Molar Gas constant [J/(K⋅mol)]
    # Particle (LNC)
    "csinit": 0.25,     # [mol/m3] Initial concentration
    "epsilonS": 0.704,  # Vol. fraction of Particle
    "R0": 6.5e-6,       # Radius of the Particle [m]   
    "csmax": 28176.4 ,  # Maximum concentration [mol/m3]
    "Ds": 1e-13,        # Diffusivity Coefficient [m2/s]
    "k": 5.904e-11,     # Reaction rate constant [m2.5 s-1 mol-0.5]
    "U_hat": 1
}
