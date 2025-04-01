
# Battery Thermal Model

This repository contains a Python implementation of a 1D radial-spiral thermal model for a lithium-ion battery, inspired by the work of Gomadam et al. (2003) on **Modeling Heat Conduction in Spiral Geometries**. The model simplifies the 2D energy balance equation to a 1D radial-spiral model using a coordinate transformation technique.

## Features
- Implements a 1D radial-spiral model for heat conduction in spirally-wound batteries.
- Incorporates radial and spiral heat conduction components via effective thermal conductivity calculation.
- Computationally efficient compared to traditional 2D models.
- Can accurately predict temperature distribution for spirally-wound battery designs.

## Model Purpose
The 1D Radial-Spiral Model is designed to reduce computation time while maintaining sufficient accuracy for predicting temperature distributions in spirally-wound battery cells. This model can serve as a simplified yet accurate tool for battery thermal management analysis.

## Files
- `battery_thermal_model.py`: Main Python implementation of the thermal model.
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
