from numpy import ndarray
from GPy.util.multioutput import build_XY
import pandas as pd
import numpy as np
import GPy

class Coregionalized(object):


    def __init__(self):

        self.m = None

    def fit(self, X, Y):

        self._validate_fit(X, Y)

        m = GPy.models.GPCoregionalizedRegression(X_list=X,
                                                  Y_list=Y)

        m.optimize("bfgs", max_iters=100)

        self.m = m

        # note input_dim is always 2 in m.input_dim
        # https://gpy.readthedocs.io/en/deploy/_modules/GPy/models/gp_coregionalized_regression.html
        # which relies on look at X,Y,ix = build_XY(X,Y) 
        # because I find the GPy notion of input_dimension pretty counter intuitive I set 
        # input_dimension to something I defined to refer to the number of observations in X
        self.input_dimension = len(X)

    def predict(self, X:ndarray, output_index:int):
        '''
        Xnew: The points at which to make a prediction (Nnew x self.input_dim)
        '''
        self._validate_predict(X, output_index)

        Y_metadata = {'output_index': np.array([output_index])}
        means, variances = self.m.predict(X,  Y_metadata=Y_metadata)
        assert len(means) == len(X) == len(variances)

        # GPy returns 1-D arrays e.g. means = [[.0323], [.012]]s
        # These lines unpack these arrays
        means = means[:,0]
        variances = variances[:,0]
        
        predictions = []
        ## Note! instances may be multi-dimensional so return the instance_id
        for instance_id, (mean, variance) in enumerate(zip(means, variances)):
            predictions.append({"mean": mean,
                                "variance": variance,
                                "instance_id": instance_id})
        return pd.DataFrame(predictions)

    def _validate_fit(self, X, Y):
        assert len(X) == len(Y), "X and Y must be the same length"


    def _validate_predict(self, X, output_index):
        assert type(output_index) == int
        assert output_index <= self.input_dimension
        assert X.shape[1] == self.input_dimension 



if __name__ == "__main__":

    cr = Coregionalized()

    np.random.seed(43)

    # we observe 10 points in the input domain, this is \phipredict
    X1 = np.random.rand(110, 1) * 10
    # we observe a function Y1 for these 10 points
    Y1 = np.sin(6 * X1) + np.random.randn(*X1.shape) * 0.05

    # select 7 points in the input domain
    X2 = X1[0:7]
    # We observe a correlated function for these 7 points, this is \phiproxy
    Y2 = np.sin((6 * X2) + .7) + np.random.randn(*X2.shape) * 0.5 + 2.0

    # select 3 points in the input domain
    X3 = X1[0:3]
    # We observe a correlated function for these 3 points, this is \phiorg
    Y3 = np.sin((6.2 * X3) + .67) + np.random.randn(*X3.shape) * 0.5 + 2.0

    # the input to coreginoalized model is 3 sets of (X--Y) pairs
    X = [X1, X2, X3]
    Y = [Y1, Y2, Y3]

    cr.fit(X, Y)

    # we have 3D inputs
    # This corresponds to observations for 
    # inputs of X1, X2, X3
    X = np.random.rand(100, 3)

    predictions = cr.predict(X, output_index=0)
