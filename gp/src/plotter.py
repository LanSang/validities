import pandas as pd
from typing import List
import altair as alt
from numpy import ndarray

class Plotter(object):

    def __init__(self):
        self.scale = alt.Scale(scheme="dark2")


    def _make_df(self, X, Y, tasks, bounds = None):
        source = pd.DataFrame({
            'x': X[:,0].tolist(),
            'y': Y[:,0].tolist(),
            'task': [str(int(i)) for i in tasks[:,0].tolist()]
        })
        if bounds is not None:
            source["upper"] = Y[:,0] + bounds.ravel()
            source["lower"] = Y[:,0] - bounds.ravel()
        return source


    def bands_plot(self, X: ndarray, Y:ndarray, tasks: ndarray, variance: ndarray, legend = True):

        self._validate_points_plot(X, Y)

        if not legend:
            color = alt.Color("task",scale=self.scale, legend=None)
        else:
            color = alt.Color("task",scale=self.scale)

        df = self._make_df(X, Y, tasks, variance)

        return alt.Chart(df).mark_area(
            opacity=0.5, color='gray'
        ).encode(
            x='x',
            y='lower',
            y2='upper',
            color=color,
            fill='task'
        )


    def points_plot(self, X: ndarray, Y: ndarray, tasks: ndarray, legend = True):
        '''plot coregionalization input points'''

        self._validate_points_plot(X, Y)
    
        source = self._make_df(X, Y, tasks)

        if not legend:
            color = alt.Color("task",scale=self.scale, legend=None)
        else:
            color = alt.Color("task",scale=self.scale)

        points = alt.Chart(source).mark_point(size=30).encode(
            x='x:Q',
            y='y:Q',
            color=color,
            fill="task",
            shape="task"
        )
        
        return points

    def line_plot(self, X: ndarray, Y: ndarray, tasks: ndarray, legend = True):
        self._validate_points_plot(X, Y)
    
        source = self._make_df(X, Y, tasks)

        if not legend:
            color = alt.Color("task",scale=self.scale, legend=None)
        else:
            color = alt.Color("task",scale=self.scale)

        line = alt.Chart(source).mark_line().encode(
            x='x:Q',
            y='y:Q',
            color=color
        )
        
        return line



    def _validate_points_plot(self, X, Y):
        if len(X) != len(Y):
            raise ValueError(f"X and Y must be the same length but X is len {len(X)} and Y is len {len(Y)} " )