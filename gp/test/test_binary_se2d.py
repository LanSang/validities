from GPy.models import GPRegression
import numpy as np
from src.kernels.kl import KL
from src.kernels.binary_se2d import BinarySE2D
import pytest

def test_loads():    
    se = BinarySE2D(input_dim=2)


def test_run_regression():
    X = np.asarray([[.5, .5]])
    Y = np.asarray([[.9, .4]])

    kernel=BinarySE2D(input_dim=2)
    GPRegression(kernel=kernel, X=X, Y=Y)

def test_binary():
    se = BinarySE2D(input_dim=2)
    X = np.asarray([[1., 0.], [1., 0.]])
    Y = np.asarray([[1.5, 2.5], [1.0, 2.0]])
    sims = GPRegression(kernel=se, X=X, Y=Y)
    assert np.unique(sims).size == 1