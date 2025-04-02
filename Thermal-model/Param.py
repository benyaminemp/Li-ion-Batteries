import numpy as np

params = {
    # Constants
    "crate": 1.0,      # C rate of the half cell
    "I_0": -12,         # Current [A/m2]
    "N": 20,           # Wings Number 
    "T_amb": 298,      # Ambient Temperature [K]
    "T_0": 300,        # Initial Temperature [K]
    "h_amb": 10,       # Ambient Convection Coefficient [W/m2.K] 
    "D": 18e-3,        # Diameter [m]
    "D_m": 2e-3,       # Mendral Diameter [m]
    "Res_m": 1e-6,     # Minimum Residual
    "maxit": 100,      # Maximum iterations
    "alpha": 0.001,    # Relaxation factor

    # Anode   LixC6MCMB
    "lambda_a": 1.04,  # Thermal conductivity [W/m.K] 
    "Cp_a": 1437.4,    # Specific heat capacity [J/kg.K] 
    "Ro_a": 1347.33,   # Density [kg/m3]
    "sigma_a": 100,    # Electrical Conductivity in solid [S/m]

    # Cathode  LiyMn2O4 
    "lambda_c": 1.58,  # Thermal conductivity  [W/m.K] 
    "Cp_c": 1269.21,   # Specific heat capacity [J/kg.K] 
    "Ro_c": 2328.5,    # Density [kg/m3]
    "sigma_c": 3.8,    # Electrical Conductivity in solid [S/m]    
}
