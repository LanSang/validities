

# https://www.cs.toronto.edu/~duvenaud/cookbook/

import numpy as np
import GPy, numpy as np
from numpy import ndarray
from GPy.kern import Kern
from GPy.util.linalg import tdot
from GPy.core.parameterization import Param
from paramz.transformations import Logexp
from paramz.caching import Cache_this
from GPy.kern.src.psi_comp import PSICOMP_Linear
from scipy.special import rel_entr as kl_div # the kl_div has some extra terms I am not famliar with; see scipy docs

from scipy.stats import entropy as relative_entropy


class BinarySE(Kern):
    """
    A kernel for binary data.

    It represents similarity as a product of RBF kernels for each binary dimension
    As described here https://www.cs.toronto.edu/~duvenaud/cookbook/

    """

    def __init__(self, input_dim, active_dims=None,
                 name='BinarySE', variance=1., lengthscale=1.):
        super(BinarySE, self).__init__(input_dim, active_dims, name)

        # a 1dimensionsal SE kernel. The input dimension is one. That is first param below
        self.one_D_se = GPy.kern.RBF(1, variance=variance, lengthscale=lengthscale)
        if input_dim < 2:
            raise ValueError("A binary SE requires more then 1 dimension")


    def _bin_se(self, X1, X2):
        assert len(X1) == len(X2)
        assert X1.shape == X2.shape
        for dimension in range(len(X1)):
            self.one_D_se()
        return 1
        # GPy.kern.RBF(1, variance=1., lengthscale=2.)


    
    @Cache_this(limit=3)
    def K(self, X: ndarray, X2: ndarray=None) -> ndarray:
        '''
        Inputs are N X C arrays, for N observed data points with C binary features
        
        Returns an N x N kernel
        '''
        # this line is kind of weird but is in the gpy docs
        # I don't totally get what X2 does at least right now
        if X2 is None: X2 = X

        assert len(X) == len(X2) 
        N = len(X)

        out = np.zeros((N, N))
        for i in range(N):
            for j in range(N): # 1/2 this computation is redundant TODO
                out[i,j] = self._bin_se(X[i], X[j])
        return out

    def Kdiag(self, X):
        out = np.zeros((N, 1))
        N = len(X)
        for i in range(N):
            out[i, 0] = self._bin_se(X[i], X[i])
        return out

    ############# Block #############
    # I do not these are required for our kernel b/c no hyperparams update
    # the paramters A and B are just there for numerical stability

    def update_gradients_full(self, dL_dK, X, X2=None):
        pass

    def update_gradients_diag(self, dL_dKdiag, X):
        pass

    def gradients_X(self, dL_dK, X, X2=None):
        pass

    def gradients_X_diag(self, dL_dKdiag, X):
        pass
    
    def gradients_XX(self, dL_dK, X, X2=None):
        pass

    def gradients_XX_diag(self, dL_dKdiag, X):
        pass
    ############ end block ##############