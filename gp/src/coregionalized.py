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

        Y_metadata = {'output_index': np.array([Y_index])}
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

    X1 = np.random.rand(110, 1) * 10
    X2 = np.random.rand(110, 1) * 7
    X3 = np.random.rand(110, 1) * 3
    X4 = np.random.rand(110, 1) * 3
    X = [X1, X2, X3, X4]

    Y1 = np.sin(X1) + np.random.randn(*X1.shape) * 0.05
    Y2 = np.sin(X2) + np.random.randn(*X2.shape) * 0.5 + 2.0
    Y3 = np.sin(X3) + np.random.randn(*X3.shape) * 19 + 4.0
    Y4 = np.sin(X3) + np.random.randn(*X3.shape) * 19 + 4.0
    Y = [Y1, Y2, Y3, Y4]

    cr.fit(X, Y)

    Y_index = 0

    Y_metadata1 = {'output_index': np.array([Y_index])}

    X = np.random.rand(100, 4)

    predictions = cr.predict(X, output_index=0)
    
    print(predictions)

    #mean = mean[0][0]
    #variance = variance[0][0]

    #X1[0][0], X2[0][0], X3[0][0], Y1[0][0], Y2[0][0], Y3[0][0], mean, variance
    #print(Y[0][0], Y[0][1], Y[0][2]) 

    #print(mean, variance)