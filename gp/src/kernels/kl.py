


import numpy as np
from numpy import ndarray
from GPy.kern import Kern
from GPy.util.linalg import tdot
from GPy.core.parameterization import Param
from paramz.transformations import Logexp
from paramz.caching import Cache_this
from GPy.kern.src.psi_comp import PSICOMP_Linear
from scipy.special import rel_entr as kl_div # the kl_div has some extra terms I am not famliar with; see scipy docs

from scipy.stats import entropy as relative_entropy
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html
# if you include qk the entropy function computes relative_entropy


class KL(Kern):
    """
    Symetric KL kernel
    
    See "A Kullback-Leibler Divergence Based Kernel for SVM Classification in Multimedia Applications"

    :param input_dim: the number of input dimensions
    :type input_dim: int # 
    :param A: the scale parameter from Moreno et al., see paper
    :type A: float
    :param B: the shift parameter from Moreno et al., see paper
    :type B: float
    :rtype: kernel object
    """

    def __init__(self, input_dim, A: float=1.0, B: float=1.0, active_dims=None, name='linear'):
        super(KL, self).__init__(input_dim, active_dims, name)
        self.A = A
        self.B = B
        if input_dim < 2:
            raise ValueError("A KL divergence requires a distribution, so input_dim must be larger than 1")

    
    def _kl(self, p, q):
        '''
        A simple wrapper that renames pk/qk and ensures output is always in base2
        '''

        return relative_entropy(pk=p, qk=q, base=2)
        
    def _exp_kl(self, x1: ndarray, x2: ndarray) -> float:
        '''
        x1 and x2 are distributions with length 1 and C columns
        '''
        assert x1.ndim == x2.ndim == 1, f"expected 1, got {x1.ndim}, {x2.ndim}"


        symetric_kl_divergence = (self._kl(x1, x2) + self._kl(x2, x1))
        return np.exp((-1 * self.A * symetric_kl_divergence) + self.B)
    
    @Cache_this(limit=3)
    def K(self, X: ndarray, X2: ndarray=None) -> ndarray:
        '''
        Inputs are N X C arrays, for N observed data points with C components
        
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
                out[i,j] = self._exp_kl(X[i], X[j])
        return out

    def Kdiag(self, X):
        out = np.zeros((N, 1))
        N = len(X)
        for i in range(N):
            out[i, 0] = self._exp_kl(X[i], X[i])
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