from numpy import ndarray
from GPy.util.multioutput import build_XY
import pandas as pd
import numpy as np
import GPy

from dataclasses import dataclass
from src.coregionalization_input import CoregionalizationInput
from src.plotter import Plotter
from src.generator import OneDimensionalGenerator
from src.data_packer import DataPacker
from src.generator import function_predict
from src.generator import function_proxy
from src.generator import function_field
from src.observations import Observations
import pandas as pd
import altair as alt
import GPy
import numpy as np


class Coregionalized(object):


    def __init__(self, num_tasks: int, num_feats: int):
        '''
        num_tasks is the total number of categories of Y observations
        num_feats is the total number of features per X
        '''
        self.num_feats = num_feats
        self.num_tasks=num_tasks
        ## ** denotes kronneker product here
        self.kernel = GPy.kern.RBF(input_dim=num_feats) ** GPy.kern.Coregionalize(input_dim=1, output_dim=num_tasks, rank=1)

    def fit(self, X, Y, task_indexes):
        '''
        X is array of input observations, of shape (n_obs, n_feats)
        Y is array of output observations, of shape (n_obs,)
        tasks is array of tasks indexes, of shape (n_obs,)
        '''

        # X has a a special input format where the last column is the task
        _X = self._prepare_X(X, task_indexes)

        self._validate_fit(X, Y, task_indexes)

        m = GPy.models.GPRegression(_X, Y, self.kernel)
        m.optimize()
        self.m = m

    def predict(self, X: ndarray, tasks: ndarray):
        _X = self._prepare_X(X, tasks)
        self._validate_predict(tasks)
        means, variances = self.m.predict(_X)

        # means and variances come out [[1][3][4]], i.e. (n_obs x 1)
        return (means, variances, tasks)

    def _prepare_X(self, X,  tasks):
        # X has a a special input format where the last column is the task
        # This method gets the data into that format
        return np.hstack([X, tasks])

    def _validate_fit(self, X, Y, tasks):
        assert len(X) == len(Y), 'must have n_obs (X--Y) pairs so len(X) should equal len(Y)'
        assert np.unique(tasks).size == self.num_tasks, "tasks must be "

    def _validate_predict(self, tasks):
        pass 
        # this assertion is not valid. some cases will have 0 tasks
        # assert np.unique(tasks).size == self.num_tasks, f"expecting {self.num_tasks} tasks"



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
    X2 = np.random.rand(n_obs_predict, n_feats) * spread
    proxy_observations = g2.generate(X2)

    g3 = OneDimensionalGenerator(f=function_field, task_index=2)
    X3 = np.random.rand(n_obs_predict, n_feats) * spread
    field_observations = g3.generate(X3)

    packer = DataPacker()
    cr_input: CoregionalizationInput = packer.pack([predict_observations, proxy_observations, field_observations])

    coregionalized = Coregionalized(num_tasks=3, num_feats=n_feats)
    coregionalized.fit(cr_input.X, cr_input.Y, cr_input.task_indexes)
    coregionalized.predict(cr_input.X, task_indexes)