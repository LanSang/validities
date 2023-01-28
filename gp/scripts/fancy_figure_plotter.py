import numpy as np
import GPy
import pandas as pd
import altair as alt
from typing import List
from numpy import ndarray
from src.observations import Observations
from src.data_packer import DataPacker
from src.generator import OneDimensionalGenerator
from src.generator import function_proxy
from src.generator import function_field
from src.generator import function_predict
from src.coregionalized import Coregionalized
from src.coregionalization_input import CoregionalizationInput
from src.plotter import Plotter

plotter = Plotter()

np.random.seed(43)

n_feats = 1
n_obs_field = 2
n_obs_proxy = 4
n_obs_predict = 7
spread = 1

range_predict = [0, 1.5]
range_proxy = [0, 1]
range_field = [.2, .5]

g1 = OneDimensionalGenerator(f=function_predict, task_index=0)
X1 = np.random.uniform(low=range_predict[0], 
                       high=range_predict[1],
                       size=(n_obs_predict, n_feats))
predict_observations = g1.generate(X1)

g2 = OneDimensionalGenerator(f=function_proxy, task_index=1)
X2 = np.random.uniform(low=range_proxy[0], 
                       high=range_proxy[1],
                       size=(n_obs_proxy, n_feats))
proxy_observations = g2.generate(X2)

g3 = OneDimensionalGenerator(f=function_field, task_index=2)
X3 = np.random.uniform(low=range_field[0], 
                       high=range_field[1],
                       size=(n_obs_field, n_feats))
field_observations = g3.generate(X3)

packer = DataPacker()
cr_input: CoregionalizationInput = packer.pack([predict_observations, proxy_observations, field_observations])

coregionalized = Coregionalized(num_tasks=3, num_feats=n_feats, variance=.2, lengthscale=.1)
coregionalized.fit(cr_input.X, cr_input.Y, cr_input.task_indexes)

def to_task(task):
    map_ = {"0": "Prediction", "1": "Proxy", "2": "Target"}
    return map_[task]

def convert_to_str(arr: ndarray):
    arr = np.asarray([to_task(str(int(i[0]))) for i in arr.tolist()])
    return arr.reshape(-1, 1)    


points = plotter.points_plot(cr_input.X, cr_input.Y, 
                             convert_to_str(cr_input.task_indexes),
                             legend=True)

X, m, v, tasks = coregionalized.predict_region(region_start=0, region_end=2)

lines = plotter.line_plot(X, m, convert_to_str(tasks), legend=None)

only_field = np.where(tasks==2)[0]

bands = plotter.bands_plot(X[only_field], 
                           m[only_field], 
                           convert_to_str(tasks[only_field]),
                           v[only_field],
                           legend=None)


df = pd.DataFrame([{"x": .7}])
line = alt.Chart(df).mark_rule().encode(x="x")

# alt.vconcat(points, lines).resolve_legend(color='independent') 
c = alt.layer(points, lines, bands, line).resolve_legend(color='independent')
c.layer[0].encoding.y.title = 'Y'
c.layer[0].encoding.x.title = 'X'
c.properties(
    width=300,
    height=300
)

c