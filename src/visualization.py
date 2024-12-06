import matplotlib.pyplot as plt
import numpy as np

class Visualization:
    def __init__(self, exposure_map, trajectories=None, vdwr_calculator=None):
        """
        Initialize the visualization class.
        :param exposure_map: ExposureMap instance.
        :param trajectories: List of Trajectory instances.
        :param vdwr_calculator: VDWRCalculator instance.
        """
        self.exposure_map = exposure_map
        self.trajectories = trajectories if trajectories else []
        self.vdwr_calculator = vdwr_calculator

    def plot_exposure_map(self):
        """
        Visualize the exposure map as a heatmap.
        """
        plt.imshow(self.exposure_map.data, cmap='hot', origin='lower')
        plt.colorbar(label='Exposure Level')
        plt.title('Exposure Map')
        plt.xlabel('Direction (Theta)')
        plt.ylabel('Distance (Radius)')
        plt.show()

    def plot_trajectories(self):
        """
        Overlay trajectories on the exposure map.
        """
        plt.imshow(self.exposure_map.data, cmap='hot', origin='lower')
        for trajectory in self.trajectories:
            if trajectory.viability:
                color = 'green'
                label = 'Viable' if 'Viable' not in plt.gca().get_legend_handles_labels()[1] else None
            else:
                color = 'red'
                label = 'Non-Viable' if 'Non-Viable' not in plt.gca().get_legend_handles_labels()[1] else None
            plt.plot([trajectory.direction] * trajectory.distance, range(1, trajectory.distance + 1), color=color, label=label)
        plt.colorbar(label='Exposure Level')
        plt.legend()
        plt.title('Trajectories on Exposure Map')
        plt.xlabel('Direction (Theta)')
        plt.ylabel('Distance (Radius)')
        plt.show()

    def plot_vdwr(self):
        """
        Visualize the computed VDWR as a polar plot.
        """
        if not self.vdwr_calculator:
            print("VDWR Calculator is not initialized.")
            return

        # Create a polar plot for VDWR
        angles = np.deg2rad(range(360))
        vdwr_values = []

        for trajectory in self.vdwr_calculator.trajectories:
            vdwr_value = sum(
                self.exposure_map.get_exposure(r, trajectory.direction) *
                self.vdwr_calculator.weighting_function.get_weight(r, trajectory.direction)
                for r in range(1, trajectory.distance + 1)
            )
            vdwr_values.append(vdwr_value)

        plt.polar(angles, vdwr_values, label='VDWR')
        plt.title('Directional Wildfire Risk (VDWR)')
        plt.legend()
        plt.show()
