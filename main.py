import numpy as np
from src.exposure_map import ExposureMap
from src.trajectory import Trajectory
from src.weighting import WeightingFunction
from src.vdwr_calculator import VDWRCalculator
from src.visualization import Visualization


# Simulated data (replace with real data)
exposure_data = np.random.rand(15, 360)  # 15 rows (distance), 360 columns (angles)
weights = np.random.rand(15, 360)

# Initialize components
exposure_map = ExposureMap(exposure_data)
weighting_function = WeightingFunction(weights)
vdwr_calculator = VDWRCalculator(exposure_map, weighting_function)
visualization = Visualization(exposure_map, vdwr_calculator.trajectories, vdwr_calculator)

# Add trajectories
for theta in range(0, 360):
    trajectory = Trajectory(direction=theta, distance=15)
    vdwr_calculator.add_trajectory(trajectory)

# Compute VDWR
vdwr = vdwr_calculator.compute_vdwr()
print(f"Computed VDWR: {vdwr}")

visualization.plot_exposure_map()

visualization.plot_trajectories()

visualization.plot_vdwr()

