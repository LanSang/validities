from dataclasses import dataclass
from numpy import ndarray

@dataclass
class Observations:
    """Observations of a particular function"""
    X: ndarray
    Y: ndarray
    task_indexes: ndarray