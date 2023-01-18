import numpy as np

class DataGenerator(object):
    '''
    Generate random data to go into a coregionalization model

    The key method is generate
    '''
        
    def function_predict(self, x):
        return np.sin(6 * x) + np.random.rand() * .5

    def function_proxy(self, x):
        return np.sin((4.5 * x) + .2) + np.random.rand()* .5

    def function_field(self, x):
        return np.sin((4.7 * x) + .3) + np.random.rand()* .5

    def generate(self, num_obs=100, n_feats=1, spread=2):
        '''
        Returns:
        X: a numpy array of shape (num_obs x n_feats)
        Y: a numpy array of shape (num_obs,)
        task_indexes: a numpy array of shape (num_obs,)

        X is the input data
        Y is the observed value, for each point X; i.e. len(X) = len(Y) = num_obs
        task_indexes is a vector of task indexes, specifying the task for each X--Y pair
        '''

        # TODO: n_feats is currently set to 1

        X = np.random.rand(num_obs, n_feats) * spread

        Y = np.random.rand(num_obs, 1)

        task_indexes = np.zeros((num_obs, 1))

        for i in range(num_obs):
            draw = np.random.rand()
            if draw <= .5:
                task_indexes[i] = 0
                Y[i] = self.function_predict(X[i])
            if draw >.5 <= .8:
                task_indexes[i] = 1
                Y[i] = self.function_proxy(X[i])
            if draw >.8:
                task_indexes[i] = 2
                Y[i] = self.function_proxy(X[i])    
                
        return X, Y, task_indexes