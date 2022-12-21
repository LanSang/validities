from GPy.models import GPRegression
import numpy as np
from src.kl import KL
import pytest

def test_gp_regression_loads():
    
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

def test_gp_regression_wrong_input_dim_checkrows():

    X = np.asarray([[.5, .5], [.5, .5], [.5, .5]])
    Y = np.asarray([[.2], [.3], [.4]])

    # I think input_dim here specifies the number of 
    # components in X. This test verifies that 
    # there is no error if there are 3 test points of dim 2
    kernel=KL(input_dim=2)
    GPRegression(kernel=kernel, X=X, Y=Y)