# Corrected Single Particle Model (cSPM) for Li-ion Battery – Cathode Half-Cell

## 🔋 Overview
This repository contains a physics-informed simulation of a **corrected Single Particle Model (cSPM)** for a **Li(Ni₀.₄Co₀.₆)O₂ (LNC)** cathode half-cell. The model incorporates **electrolyte dynamics** into the traditional SPM framework and is solved using the **Finite Volume Method (FVM)** for both solid-phase and electrolyte equations.

This implementation provides enhanced accuracy over the classical SPM by including:
- Ionic concentration dynamics in the electrolyte
- Electrolyte potential field
- Improved voltage prediction

## 📁 Project Structure
| File / Folder        | Description |
|----------------------|-------------|
| `cSPM.ipynb`         | Main notebook for running the cSPM simulation, visualization, and validation. |
| `Solver.py`          | Time-stepping algorithm to solve the SPM and corrected cSPM equations. |
| `FVM.py`             | Finite Volume implementations for solid and electrolyte diffusion equations. |
| `Param.py`           | Dimensional parameters for the cathode, electrolyte, and geometry. |
| `NDParam.py`         | Non-dimensional parameters computed from physical constants. |
| `Functions.py`       | Supporting equations: diffusion coefficients, open-circuit potential, overpotentials, etc. |
| `Plot.py`            | Utility functions to visualize solid concentration, electrolyte concentration, potentials, and voltages. |
| `GridSearch.py`      | Grid sensitivity studies over time steps and mesh resolutions. |
| `Data.py`            | Benchmark data for SPM, cSPM, and DFN model comparisons (1C, 4C, 8C, 16C rates). |

## ⚙️ Features
- Solid-phase diffusion using FVM in spherical coordinates
- Electrolyte concentration and potential equations across electrode length
- Coupled reaction kinetics with Butler–Volmer formulation
- Voltage output from both traditional SPM and enhanced cSPM
- Grid search tools for convergence studies

## 📊 Validation
The model results are validated against the **cSPM paper by Richardson et al.**:

> **Richardson, R. R., Ireland, J., & Howey, D. A.**  
> *Battery parameter estimation using a single particle model with electrolyte and thermal dynamics*.  
> Journal of Power Sources, 456, 227997 (2020).  
> [Link to paper](https://www.sciencedirect.com/science/article/pii/S0013468620302541)

Validation includes:
- Interpolation of benchmark data
- Voltage vs. time comparison
- RMSE calculation for accuracy reporting

## 🧪 Example Outputs
- Lithium concentration profiles in the solid and electrolyte phases
- Electrolyte potential and overpotential visualization
- Voltage comparison between SPM, cSPM, and literature data

## 🧰 Requirements
```bash
numpy
matplotlib
scipy
scikit-learn
```

You can install them with:
```bash
pip install numpy matplotlib scipy scikit-learn
```

## 📝 License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
