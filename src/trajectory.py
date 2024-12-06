class Trajectory:
    def __init__(self, direction, distance):
        """
        Initialize a trajectory.
        :param direction: Direction in degrees (0-360).
        :param distance: Distance of the trajectory in the exposure map.
        """
        self.direction = direction
        self.distance = distance
        self.viability = False

    def compute_viability(self, exposure_map, threshold=0.8):
        """
        Compute the viability of the trajectory.
        :param exposure_map: ExposureMap instance.
        :param threshold: Threshold for trajectory viability (e.g., 80%).
        """
        total_length = 0
        high_exposure_length = 0

        for r in range(1, self.distance + 1):
            exposure = exposure_map.get_exposure(r, self.direction)
            if exposure >= 0.6:  # High-exposure threshold
                high_exposure_length += 1
            total_length += 1

        self.viability = (high_exposure_length / total_length) >= threshold
