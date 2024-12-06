class VDWRCalculator:
    def __init__(self, exposure_map, weighting_function):
        """
        Initialize the VDWR calculator.
        :param exposure_map: ExposureMap instance.
        :param weighting_function: WeightingFunction instance.
        """
        self.exposure_map = exposure_map
        self.weighting_function = weighting_function
        self.trajectories = []

    def add_trajectory(self, trajectory):
        """
        Add a trajectory to the calculator.
        :param trajectory: Trajectory instance.
        """
        self.trajectories.append(trajectory)

    def compute_vdwr(self):
        """
        Compute the Viable Directional Wildfire Risk (VDWR).
        :return: Computed VDWR value.
        """
        vdwr = 0
        for trajectory in self.trajectories:
            trajectory.compute_viability(self.exposure_map)
            if trajectory.viability:
                for r in range(1, trajectory.distance + 1):
                    exposure = self.exposure_map.get_exposure(r, trajectory.direction)
                    weight = self.weighting_function.get_weight(r, trajectory.direction)
                    vdwr += exposure * weight
        return vdwr
