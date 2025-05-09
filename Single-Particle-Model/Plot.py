import matplotlib.pyplot as plt
import Param, NDParam
import numpy as np

def results(result_bowl):
    """Plots all results from the result bowl."""
    tnew = result_bowl["tnew"]
    #cs Plot
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(Param.params["R0"]*np.linspace(0, 1, Param.params["M"]),Param.params["csmax"]*result_bowl["cs"][0],label=f't = {round(tnew[0], 2)} hours',color='red')
    ax.plot(Param.params["R0"]*np.linspace(0, 1, Param.params["M"]),Param.params["csmax"]*result_bowl["cs"][int(len(tnew)/4)],label=f't = {round(tnew[int(len(tnew)/4)], 2)} hours',color='black')
    ax.plot(Param.params["R0"]*np.linspace(0, 1, Param.params["M"]),Param.params["csmax"]*result_bowl["cs"][int(len(tnew)/2)],label=f't = {round(tnew[int(len(tnew)/2)], 2)} hours',color='black')
    ax.plot(Param.params["R0"]*np.linspace(0, 1, Param.params["M"]),Param.params["csmax"]*result_bowl["cs"][int(len(tnew)*3/4)],label=f't = {round(tnew[int(len(tnew)*3/4)], 2)} hours',color='black')
    ax.plot(Param.params["R0"]*np.linspace(0, 1, Param.params["M"]),Param.params["csmax"]*result_bowl["cs"][-1],label=f't = {round(tnew[-1], 2)} hours', color='blue')
    ax.legend()
    ax.set_xlabel('$r$ [m]')
    ax.set_ylabel('$c_s$ [mol/m$^3$]')
    plt.grid()
    plt.show()

    # Voltage Comparison
    plt.figure(figsize=(4, 3))
    plt.plot(tnew, result_bowl["V_spm"], label="SPM")
    plt.xlabel("time [hrs]")
    plt.ylabel("Voltage [V]")
    plt.legend()
    plt.grid()
    plt.show()
    print(f"SPM Execution time: {result_bowl['spm_time']:.3f} seconds")
