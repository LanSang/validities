import numpy as np

from src.coregionalization_input import CoregionalizationInput
from src.observations import Observations
from typing import List

class DataPacker(object):
    '''
    Generate random data to go into a coregionalization model

    The key method is generate
    '''
    def pack(self, function_observations = List[Observations]):
        '''
        Returns:
        function_observations is a list of observations from K functions
        Each set of observations has an X, Y pair of len(n_obs_f) where 
        n_obs_f is the number of observations for the function

        Returns data in the format needed for GPY, X, Y task_indexes
        X is the input data
        Y is the observed value, for each point X; i.e. len(X) = len(Y) = num_obs
        task_indexes is a vector of task indexes, specifying the task for each X--Y pair
        '''

        X = np.vstack([o.X for o in function_observations])

        Y = np.vstack([o.Y for o in function_observations])

        task_indexes = np.vstack([o.task_indexes for o in function_observations])
                
        return CoregionalizationInput(X=X, Y=Y, task_indexes=task_indexes)
