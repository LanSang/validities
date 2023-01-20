import numpy as np
from typing import List
from numpy import ndarray

from src.observations import Observations
from src.data_packer import DataPacker

from src.coregionalization_input import CoregionalizationInput
    

class OneDimensionalGenerator(object):

    def __init__(self, f, task_index: int):
        self._f = f
        self.task_index = task_index

    def generate(self, X: ndarray) -> ndarray:
        num_obs = len(X)
        Y = np.zeros((num_obs, 1))
        for i in range(num_obs):
            Y[i] = self._f(X[i][0])

        task_indexes = np.zeros_like(Y)
        task_indexes += self.task_index

        return Observations(X, Y, task_indexes)


def function_predict(x):
    return np.sin(6 * x) + np.random.rand() * .5

def function_proxy(x):
    return 2 + np.sin((4.5 * x) + .2) + np.random.rand()* .5

def function_field(x):
    return 4 + np.sin((4.7 * x) + .3) + np.random.rand()* .5


if __name__ == "__main__":

    n_feats = 1
    n_obs_field = 2
    n_obs_proxy = 5
    n_obs_predict = 10
    spread = 9

    g1 = OneDimensionalGenerator(f=function_predict, task_index=0)
    X1 = np.random.rand(n_obs_predict, n_feats) * spread
    predict_observations = g1.generate(X1)

    g2 = OneDimensionalGenerator(f=function_proxy, task_index=1)
    X2 = np.random.rand(n_obs_proxy, n_feats) * spread
    proxy_observations = g2.generate(X2)

    g3 = OneDimensionalGenerator(f=function_field, task_index=2)
    X3 = np.random.rand(n_obs_field, n_feats) * spread
    field_observations = g3.generate(X3)

    packer = DataPacker()
    input_: CoregionalizationInput = packer.pack([predict_observations, proxy_observations, field_observations])
