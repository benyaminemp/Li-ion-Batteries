import matplotlib.pyplot as plt
import numpy as np
import Functions, Param, ParamF

def results(result_bowl):
    """
    Plots temperature distribution results.
    """
    r = result_bowl["r"]
    T = result_bowl["T"]
    maxit = Param.params["maxit"]
    t = np.arange(ParamF.params["dt"], ParamF.params["dt"] * maxit, ParamF.params["dt"])

    plt.figure(figsize=(4, 3))
    plt.plot(r*1000, T[:,0], label=f't = {round(t[0]/3600,2)} hours', color='red')
    plt.plot(r*1000, T[:,int(maxit/5)], label=f't = {round(t[int(maxit/5)]/3600,2)} hours',color='black')
    plt.plot(r*1000, T[:,int(maxit/3)], label=f't = {round(t[int(maxit/3)]/3600,2)} hours',color='black')
    plt.plot(r*1000, T[:,int(maxit/2)], label=f't = {round(t[int(maxit/2)]/3600,2)} hours',color='black')
    plt.plot(r*1000, T[:,int(maxit*3/4)], label=f't = {round(t[int(maxit*3/4)]/3600,2)} hours',color='black')
    plt.plot(r*1000, T[:,int(maxit*4/5)], label=f't = {round(t[int(maxit*4/5)]/3600,2)} hours', color='blue')
    plt.xlabel('Radial Position (mm)')
    plt.ylabel('Temperature (K)')
    plt.title('Temperature Distribution in Battery')
    plt.grid(True)
    plt.legend()
    plt.show()
    # Current 

    I = np.array([Functions.i_current(time) for time in t])
    plt.figure(figsize=(4, 3))
    plt.plot(t, I)
    plt.xlabel("time [seconds]")
    plt.ylabel("Current [A/m2]")
    plt.grid()
    plt.show()
    print(f"Execution time: {result_bowl['thermal_time']:.3f} seconds")

