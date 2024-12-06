# Wildfire Directional Vulnerability Risk (SDE Project)

## Project Overview

This project models and computes **Viable Directional Wildfire Risk (VDWR)** using Python. The goal is to quantify and analyze the directional vulnerability of communities to wildfires, considering hazardous fuel exposure, trajectory viability, and dynamic weighting factors like wind and critical infrastructure proximity.

The project is designed for modularity, scalability, and future adaptability, enabling integration with real-world geospatial data and advanced simulation techniques.

## Reference
The project is based on:
Beverly, J. L., & Forbes, A. M. (2023). Assessing directional vulnerability to wildfire. *Natural Hazards, 117*(2), 831–849. https://doi.org/10.1007/s11069-023-05885-3

---

## Problem Definition Equation (PDE)

The Viable Directional Wildfire Risk (**VDWR**) for a community or location is defined as:

\[
VDWR = \sum_{\theta=1}^{360} \int_{r=0}^{R} \mathcal{E}(r, \theta) \cdot T(r, \theta) \, dr
\]

### Variables:
- \( \theta \): Directional angle (degrees) from the community centroid (\(0^\circ\) to \(360^\circ\)).
- \( r \): Radial distance from the community centroid, ranging from \(0\) to \(R\) (e.g., 15 km).
- \( \mathcal{E}(r, \theta) \): Hazardous fuel exposure at a given distance \(r\) and angle \( \theta \).
  - Binary metric: \(1\) for high exposure (\( \geq 60\% \)), \(0\) for low exposure.
- \( T(r, \theta) \): Trajectory viability (binary).
  - \(1\) if \(80\%\) of the trajectory intersects high-exposure areas; \(0\) otherwise.
- \( R \): Maximum distance (e.g., 15 km).

---

## Solution Domain Equation (SDE)

To provide actionable insights, the SDE refines the PDE by integrating additional factors such as wind direction, proximity to critical infrastructure, and suppression resource availability:

\[
\hat{VDWR} = \sum_{\theta=1}^{360} \int_{r=0}^{R} \mathcal{E}(r, \theta) \cdot T(r, \theta) \cdot \mathcal{W}(r, \theta) \, dr
\]

### Additional Variable:
- \( \mathcal{W}(r, \theta) \): Weighting function or adjustment factor.
  - Example factors: wind directionality, suppression priority, proximity to infrastructure.


### Project Structure:
wildfire-sde/
├── data/               # Input data files (e.g., exposure maps, weights)
├── src/                # Source code for the project
│   ├── exposure_map.py # Handles exposure map logic
│   ├── trajectory.py   # Computes trajectory viability
│   ├── weighting.py    # Applies dynamic weighting factors
│   ├── vdwr_calculator.py # Integrates components to compute VDWR
│   ├── utils.py        # Helper functions
├── tests/              # Unit tests
├── notebooks/          # Jupyter notebooks for experiments and visualization
├── main.py             # Main script to run the workflow
├── requirements.txt    # Python dependencies
└── README.md           # Project description (this file)


