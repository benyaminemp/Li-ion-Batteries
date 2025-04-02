import numpy as np
import time
import Param, ParamF
import Functions
import FVM


def solve_thermal():
    """
    Solves the thermal model using the Finite Volume Method (FVM) and returns the results.
    """
    maxit = Param.params['maxit']
    alpha = Param.params['alpha']
    residual_threshold = Param.params['Res_m']

    # Initialize Variables
    result_bowl = {
        "T": [],
        "r": [],
        "thermal_time": 0
    }


    # Initialize the FVM system
    A, S, T, Told, r = FVM.initialize_FVM()
    TT = np.random.uniform(0,1,(ParamF.params["n"],maxit))



    start_time = time.time()

    # Iterative solver
    for k in range(maxit):
        T_new = np.linalg.solve(A, S)

        # Update temperature using relaxation factor
        T = alpha * T_new + (1 - alpha) * Told

        # Residual calculation
        residuals = np.abs(T - Told) / Told
        ee1 = np.max(residuals)

        if ee1 < residual_threshold:
            break

        Told = np.copy(T)
        if k % 20 == 0:
            print(f'Iteration {k+1}: Residual T = {ee1}')
        TT[:,k] = T

    end_time = time.time()
    result_bowl["thermal_time"] = end_time - start_time
    result_bowl["T"] = TT
    result_bowl["r"] = r  
    
    return result_bowl
