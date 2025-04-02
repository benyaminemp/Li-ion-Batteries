# Battery Thermal Model

This repository contains a Python implementation of a 1D radial-spiral thermal model for a lithium-ion battery, inspired by the work of Gomadam et al. (2003) on **Modeling Heat Conduction in Spiral Geometries**. The model simplifies the 2D energy balance equation to a 1D radial-spiral model using a coordinate transformation technique.

## Features
- Implements a 1D radial-spiral model for heat conduction in spirally-wound batteries.
- Incorporates radial and spiral heat conduction components via effective thermal conductivity calculation.
- Computationally efficient compared to traditional 2D models.
- Can accurately predict temperature distribution for spirally-wound battery designs.
- Supports customised input parameters for different battery geometries and thermal properties.
- Modular code structure with separate modules for parameter handling, FVM calculations, plotting, and solver routines.

## Model Purpose
The 1D Radial-Spiral Model is designed to reduce computation time while maintaining sufficient accuracy for predicting temperature distributions in spirally-wound battery cells. This model can serve as a simplified yet accurate tool for battery thermal management analysis.

## Files
- `Solver.py`: Main solver function handling the iterative solution process.
- `FVM.py`: Finite Volume Method calculations and matrix initialisation.
- `Functions.py`: Helper functions for current calculation and heat generation.
- `Param.py`: Contains all user-defined parameters.
- `ParamF.py`: Computes derived parameters based on user-defined inputs.
- `Plot.py`: Handles the plotting of temperature distribution results.
- `README.md`: Documentation of the repository.

## Requirements
- Python 3.x
- Numpy
- Matplotlib

To install the required packages, use:
```bash
pip install numpy matplotlib
```

## Usage
Run the script using:
```bash
python battery_thermal_model.py
```

The script will output a plot showing the temperature distribution across the battery.

## Author
Benyamin Ebrahimpour

## License
MIT License
