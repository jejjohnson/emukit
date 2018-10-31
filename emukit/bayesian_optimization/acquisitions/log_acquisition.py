from typing import Tuple

import numpy as np

from emukit.core.acquisition import Acquisition


class LogAcquisition(Acquisition):
    """
    Takes the log of an acquisition function
    """
    def __init__(self, acquisition):
        """
        :param acquisition: Base acquisition function
        """
        self.acquisition = acquisition

    def evaluate(self, x: np.ndarray) -> np.ndarray:
        """
        :param x: Input location
        :return: log of original acquisition function at input location(s)
        """
        return np.log(self.acquisition.evaluate(x))

    def evaluate_with_gradients(self, x: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Return log of original acquisition with gradient

        :param x: Input location
        :return: Tuple of (log value, gradient of log value)
        """
        value, gradient = self.acquisition.evaluate_with_gradients(x)
        value = np.maximum(value, 1e-10)
        log_gradient = 1/value * gradient
        return np.log(value), log_gradient

    @property
    def has_gradients(self):
        return self.acquisition.has_gradients
