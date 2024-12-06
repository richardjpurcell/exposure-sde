# Wildfire Directional Vulnerability Risk (SDE Project)

## Project Overview

This project models and computes **Viable Directional Wildfire Risk (VDWR)** using Python. The goal is to quantify and analyze the directional vulnerability of communities to wildfires, considering hazardous fuel exposure, trajectory viability, and dynamic weighting factors like wind and critical infrastructure proximity.

The project is designed for modularity, scalability, and future adaptability, enabling integration with real-world geospatial data and advanced simulation techniques.

---

## Reference

The project is based on:
Beverly, J. L., & Forbes, A. M. (2023). Assessing directional vulnerability to wildfire. *Natural Hazards, 117*(2), 831–849. https://doi.org/10.1007/s11069-023-05885-3

---

## Problem Definition Equation (PDE)

The Viable Directional Wildfire Risk (**VDWR**) for a community or location is defined as:

![VDWR Formula](https://latex.codecogs.com/svg.latex?VDWR%20=%20\sum_{\theta=1}^{360}\int_{r=0}^{R}\mathcal{E}(r,%20\theta)\cdot{T}(r,%20\theta)\,dr)

### Variables:
- ![Theta Variable](https://latex.codecogs.com/svg.latex?\theta): Directional angle (degrees) from the community centroid (![Theta Range](https://latex.codecogs.com/svg.latex?0^\circ%20\text{to}%20360^\circ)).
- ![r Variable](https://latex.codecogs.com/svg.latex?r): Radial distance from the community centroid, ranging from ![r Range](https://latex.codecogs.com/svg.latex?0) to ![R Variable](https://latex.codecogs.com/svg.latex?R) (e.g., 15 km).
- ![E Variable](https://latex.codecogs.com/svg.latex?\mathcal{E}(r,%20\theta)): Hazardous fuel exposure at a given distance ![r](https://latex.codecogs.com/svg.latex?r) and angle ![theta](https://latex.codecogs.com/svg.latex?\theta).
  - Binary metric: ![Binary 1](https://latex.codecogs.com/svg.latex?1) for high exposure (![Greater Than 60](https://latex.codecogs.com/svg.latex?\geq%2060\%)), ![Binary 0](https://latex.codecogs.com/svg.latex?0) for low exposure.
- ![T Variable](https://latex.codecogs.com/svg.latex?T(r,%20\theta)): Trajectory viability (binary).
  - ![Binary Viability](https://latex.codecogs.com/svg.latex?1) if ![Greater Than 80](https://latex.codecogs.com/svg.latex?80\%) of the trajectory intersects high-exposure areas; ![Binary Viability](https://latex.codecogs.com/svg.latex?0) otherwise.
- ![R Variable](https://latex.codecogs.com/svg.latex?R): Maximum distance (e.g., 15 km).

---

## Solution Domain Equation (SDE)

To provide actionable insights, the SDE refines the PDE by integrating additional factors such as wind direction, proximity to critical infrastructure, and suppression resource availability:

![SDE Formula](https://latex.codecogs.com/svg.latex?\hat{VDWR}%20=%20\sum_{\theta=1}^{360}\int_{r=0}^{R}\mathcal{E}(r,%20\theta)\cdot{T}(r,%20\theta)\cdot\mathcal{W}(r,%20\theta)\,dr)

### Additional Variable:
- ![W Variable](https://latex.codecogs.com/svg.latex?\mathcal{W}(r,%20\theta)): Weighting function or adjustment factor.
  - Example factors: wind directionality, suppression priority, proximity to infrastructure.

---

## Project Structure

The project is organized as follows:

- **`wildfire-sde/`**  
  Main project directory containing all source code and resources.

  - **`data/`**  
    Directory for input data files, such as exposure maps and weights.

  - **`src/`**  
    Source code for the project.
    - **`exposure_map.py`**: Handles exposure map logic.
    - **`trajectory.py`**: Computes trajectory viability.
    - **`weighting.py`**: Applies dynamic weighting factors.
    - **`vdwr_calculator.py`**: Integrates components to compute VDWR.
    - **`visualization.py`**: Visualizes VDWR results in different plots.
    - **`utils.py`**: Contains helper functions.

  - **`tests/`**  
    Unit tests for validating individual components of the project.

  - **`notebooks/`**  
    Jupyter notebooks for experiments, visualizations, and exploratory analysis.

  - **`main.py`**  
    Main script to execute the workflow for computing directional wildfire risk.

  - **`requirements.txt`**  
    File listing Python dependencies required for the project.

  - **`README.md`**  
    Project description and documentation (this file).


