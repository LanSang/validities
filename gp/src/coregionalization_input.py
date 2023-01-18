from dataclasses import dataclass
from numpy import ndarray
import numpy as np

@dataclass
class CoregionalizationInput:
	'''

	let n_obs be the number of total observations == len(X) == len(Y)

	Input
	X: ndarray(n_obs x n_feats) for T different tasks
	Y: ndarray(n_obs, 1) variable for the input X
	task_indexes: ndarray(n_obs, 1), an array of task indexes for each row in X
	'''

	X: ndarray
	Y: ndarray
	task_indexes: ndarray


	def __post_init__(self):
		assert len(self.X) == len(self.Y) == len(self.task_indexes), "X, Y and n_obs need to be the same length"
		assert np.unique(self.task_indexes).size > 0, "Need to have at least 2 tasks"