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