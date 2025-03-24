# Single Particle Model for Li-ion Battery (Cathode Half-Cell)

## 🔋 Overview
This repository contains a physics-based simulation of a **Single Particle Model (SPM)** applied to a **Li(Ni₀.₄Co₀.₆)O₂ (LNC)** cathode half-cell. The model is implemented using the **Finite Volume Method (FVM)** to numerically solve the solid-phase diffusion PDE, and is validated against experimental-style data extracted from the SPM model by *Richardson et al.* ([paper link](https://www.sciencedirect.com/science/article/pii/S0013468620302541)).

## 📁 Project Structure
| File / Folder        | Description |
|----------------------|-------------|
| `SPM.ipynb`          | Main notebook for running the SPM simulation, visualization, and validation. |
| `Solver.py`          | Time-stepping algorithm to solve the SPM and return voltage/concentration profiles. |
| `FVM.py`             | Core Finite Volume Method implementation for solving solid-phase diffusion. |
| `Param.py`           | Physical parameters for the cathode, particle properties, and constants. |
| `NDParam.py`         | Non-dimensionalized versions of the physical parameters. |
| `Functions.py`       | Material-specific functions: diffusion coefficient and equilibrium potential. |
| `Data.py`            | Validation dataset from Richardson et al. (SPM data for 1C, 4C, 8C, 16C). |
| `Plot.py`            | Utility functions to visualize simulation results and voltage curves. |
| `GridSearch.py`      | Grid sensitivity analysis over `dt` and spatial mesh size `M`. |

## ⚙️ Features
- Finite volume discretization of spherical diffusion equation
- Butler–Volmer-based voltage computation
- Time-dependent lithium concentration and terminal voltage tracking
- Built-in benchmark data for result validation
- Grid/time step sensitivity tools

## 📊 Validation
The model results are validated against the corrected Single Particle Model (cSPM) from the following paper:

> **Richardson, R. R., Ireland, J., & Howey, D. A.**  
> *Battery parameter estimation using a single particle model with electrolyte and thermal dynamics*.  
> Journal of Power Sources, 456, 227997 (2020).  
> [Link to paper](https://www.sciencedirect.com/science/article/pii/S0013468620302541)

Comparison is performed by interpolating the reference voltage data and computing RMSE.

## 🧪 Example Output
- Time-evolving lithium concentration profiles
- Voltage vs. time plots
- RMSE between simulated and benchmark data

## 🧰 Requirements
```bash
numpy
matplotlib
scipy
scikit-learn
```

You can install them using:
```bash
pip install numpy matplotlib scipy scikit-learn
```

## 📝 License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
