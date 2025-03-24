import numpy as np
import importlib
import matplotlib.pyplot as plt
import Param, NDParam
import FVM, Functions
import Data
import Solver
import time
from sklearn.metrics import mean_squared_error

def dt_Search(dt_values):
    fig, ax = plt.subplots(figsize=(8, 6))
    for dt in dt_values:
        # Set new dt value in parameters
        NDParam.params["dt"] = dt
        # Reload dependent modules
        importlib.reload(NDParam)
        importlib.reload(Functions)
        importlib.reload(FVM)
        importlib.reload(Solver)
        importlib.reload(Data)

        # Solve Model
        start_time = time.time()
        solution = Solver.SPM()
        end_time = time.time()

        # Extract V_cspmb and time grid
        V_spm = np.array(solution["V_spm"])  
        time_grid = np.array(solution["tnew"])

        # Compute execution time
        computation_time = end_time - start_time

        # Plot results
        ax.plot(time_grid, V_spm, label=f'dt = {dt:.1e} sec | Time = {computation_time:.3f} sec')

    # Final plot settings
    ax.legend()
    ax.set_xlabel('Time [hours]')
    ax.set_ylabel('Voltage [V]')
    plt.grid()
    plt.show()

def dr_Search(M_values):
    # Initialize figure
    fig, ax = plt.subplots(figsize=(8, 6))
    for dM in M_values:
        # Set new dt value in parameters
        Param.params["M"] = dM


        # Reload dependent modules
        importlib.reload(NDParam)
        importlib.reload(Functions)
        importlib.reload(FVM)
        importlib.reload(Data)
        importlib.reload(Solver)

        # Solve Model
        start_time = time.time()
        solution = Solver.SPM()
        end_time = time.time()

        # Extract V_cspmb and time grid
        V_spm = np.array(solution["V_spm"])  
        time_grid = np.array(solution["tnew"])

        # Compute execution time
        computation_time = end_time - start_time

        # Plot results
        ax.plot(time_grid, V_spm, label=f'R mesh size = {dM} | Time = {computation_time:.3f} sec')

    # Final plot settings
    ax.legend()
    ax.set_xlabel('Time [hours]')
    ax.set_ylabel('Voltage [V]')
    plt.grid()
    plt.show()
