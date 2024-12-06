class WeightingFunction:
    def __init__(self, weights):
        """
        Initialize the weighting function.
        :param weights: 2D numpy array representing the weights.
        """
        self.weights = weights

    def get_weight(self, r, theta):
        """
        Get the weight at a given (r, theta) in polar coordinates.
        :param r: Radius (distance from center).
        :param theta: Angle in degrees.
        :return: Weight value at (r, theta).
        """
        rows, cols = self.weights.shape
        index_r = int(r)
        index_theta = int(theta % cols)
        return self.weights[min(index_r, rows - 1), index_theta]
