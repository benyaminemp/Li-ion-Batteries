import numpy as np
import Param, ParamF
import Functions


def initialize_FVM():
    """
    Initializes the Finite Volume Method (FVM) parameters and matrix equations.
    """
    maxit = Param.params['maxit']
    t = np.arange(ParamF.params["dt"], ParamF.params["dt"] * maxit, ParamF.params["dt"])
    r = np.arange(ParamF.params["X"] / 2, ParamF.params["n"] * ParamF.params["X"] + ParamF.params["X"] / 2, ParamF.params["X"])

    RoCp_eff = (Param.params["Ro_a"] * Param.params["Cp_a"] * ParamF.params["A_a"] + Param.params["Ro_c"] * Param.params["Cp_c"] * ParamF.params["A_c"]) / (ParamF.params["A_a"] + ParamF.params["A_c"])
    d = RoCp_eff / ParamF.params["dt"]
    s = np.zeros(Param.params["N"])

    for j in range(Param.params["N"]):
        r1A = ParamF.params["rin"] + 2 * ParamF.params["X"] * j
        r1B = r1A + ParamF.params["X"]
        r2A = r1B
        r2B = r1B + ParamF.params["X"]
        s[j] = 1 / Param.params["lambda_a"] * np.log(r1B / r1A) + 1 / Param.params["lambda_c"] * np.log(r2B / r2A)

    lambda_r = np.log10((ParamF.params["R"] + ParamF.params["rin"]) / ParamF.params["rin"]) / np.sum(s)
    lambda_eff = np.array([lambda_r + Param.params["lambda_a"] / (ParamF.params["a"] ** 2 * r_val ** 2) for r_val in r])
    f = lambda_eff / ParamF.params["dr"] ** 2
    b = (lambda_eff / r - 2 * Param.params["lambda_a"] / (ParamF.params["a"] ** 2 * r ** 3)) / ParamF.params["dr"]

    # Initialization
    T = np.ones(len(r)) * Param.params["T_0"]
    Told = np.copy(T)
    A = np.zeros((ParamF.params["n"], ParamF.params["n"]))
    S = np.zeros(ParamF.params["n"])

    A[0, 0] = 1
    A[0, 1] = -1
    A[-1, -1] = -b[-1] + d + 2 * f[-1]
    A[-1, -2] = b[-1] - f[-1]

    for j in range(1, ParamF.params["n"] - 1):
        A[j, j] = -b[j] + d + 2 * f[j]
        A[j, j + 1] = -d
        A[j, j - 1] = b[j] - f[j]

    for j in range(ParamF.params["n"]):
        S[j] = d * T[j] + Functions.qdot(t[j], r[j])

    S[0] = 0
    S[-1] += ParamF.params["hprim"] * Param.params["T_amb"]

    return A, S, T, Told, r