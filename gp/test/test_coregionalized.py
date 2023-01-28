from GPy.models import GPRegression
import numpy as np
from src.kernels.kl import KL
import pytest
import random
from dataclasses import dataclass
from src.coregionalization_input import CoregionalizationInput
from src.plotter import Plotter
from src.data_packer import DataPacker
from src.coregionalized import Coregionalized
from src.generator import OneDimensionalGenerator
from src.generator import function_predict
from src.generator import function_proxy
from src.generator import function_field
from GPy.kern import RBF


def test_coregionalized():
    random.seed(3)
    for i in range(100):

        '''fit and predict run with random feats and obs'''
        n_obs_predict = random.randint(20, 50)
        n_obs_proxy = random.randint(20, 50)
        n_obs_field = random.randint(20, 50)
        n_feats = 1
        spread = random.randint(1, 20)

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

        cr_input: CoregionalizationInput = packer.pack([predict_observations,
                                                        proxy_observations,
                                                        field_observations])

        kernel = RBF(input_dim=n_feats,
                     variance=1., 
                     lengthscale=1.)

        coregionalized = Coregionalized(input_kernel=kernel, num_tasks=3, num_feats=n_feats)
        coregionalized.fit(cr_input.X, cr_input.Y, cr_input.task_indexes)
        coregionalized.predict(cr_input.X, cr_input.task_indexes)

def test_gp_regression_loads_with_KL_kernel():
    
    X = np.asarray([[.5, .5]])
    Y = np.asarray([[.9, .4]])

    kernel=KL(input_dim=2)
    GPRegression(kernel=kernel, X=X, Y=Y)

def test_gp_regression_wrong_input_dim():
    with pytest.raises(Exception) as exc_info:   
        raise Exception('some info')
    
        X = np.asarray([[.5, .5]])
        Y = np.asarray([[.9, .4]])

        # I think input_dim here specifies the number of 
        # components in X. In the above example X has 2
        # dim but the kernel below is defined for 6 dim so it 
        # will fail
        kernel=KL(input_dim=6)
        GPRegression(kernel=kernel, X=X, Y=Y)

def test_kl_input_dim_1():
    with pytest.raises(Exception) as exc_info:   
        raise Exception('some info')
    
        # this should raise an error
        kernel=KL(input_dim=1)

def test_kl_diagonal():

    k = KL(input_dim=2, A=-1, B=0)

    # 10 random bernoulli distros
    X = np.random.rand(10,2)
    X = X/(np.sum(X, axis=1).reshape(10, 1))
    C = k.K(X,X) # covariance matrix

    assert np.unique(np.diag(C)).size == 1
    assert np.unique(np.diag(C))[0] == 1

def test_gp_regression_wrong_input_dim_checkrows():

    X = np.asarray([[.5, .5], [.5, .5], [.5, .5]])
    Y = np.asarray([[.2], [.3], [.4]])

    # I think input_dim here specifies the number of 
    # components in X. This test verifies that 
    # there is no error if there are 3 test points of dim 2
    kernel=KL(input_dim=2)
    GPRegression(kernel=kernel, X=X, Y=Y)