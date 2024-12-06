import numpy as np

class ExposureMap:
    def __init__(self, data, resolution=1):
        """
        Initialize the exposure map.
        :param data: 2D numpy array representing the exposure map.
        :param resolution: Resolution of the map (e.g., meters per cell).
        """
        self.data = data
        self.resolution = resolution

    def get_exposure(self, r, theta):
        """
        Get the exposure value at a given (r, theta) in polar coordinates.
        :param r: Radius (distance from center).
        :param theta: Angle in degrees.
        :return: Exposure value at (r, theta).
        """
        rows, cols = self.data.shape
        index_r = int(r / self.resolution)
        index_theta = int(theta % cols)  # Wrap around for circular data
        return self.data[min(index_r, rows - 1), index_theta]
