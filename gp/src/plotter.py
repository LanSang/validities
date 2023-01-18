import pandas as pd
import altair as alt
from numpy import ndarray

class Plotter(object):

    def points_plot(self, X: ndarray, Y: ndarray, tasks: ndarray):
        '''plot coregionalization input points'''

        self._validate_points_plot(X, Y)
    
        source = pd.DataFrame({
            'x': X[:,0].tolist(),
            'y': Y[:,0].tolist(),
            'task': [str(i) for i in tasks[:,0].tolist()]
        })

        scale = alt.Scale(scheme="dark2")

        points = alt.Chart(source).mark_point(size=30).encode(
            x='x:Q',
            y='y:Q',
            color=alt.Color("task",scale=scale),
            fill=alt.Color("task",scale=scale),
            shape=alt.Color("task",scale=scale)
        )
        
        return points

    def _validate_points_plot(self, X, Y):
        if len(X) != len(Y):
            raise ValueError(f"X and Y must be the same length but X is len {len(X)} and Y is len {len(Y)} " )