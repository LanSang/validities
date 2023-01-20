import pandas as pd
from typing import List
import altair as alt
from numpy import ndarray

class Plotter(object):

    def __init__(self, x_domain=[0, 1.5], y_domain=[-4, 8]):
        self.scale = alt.Scale(scheme="dark2") 
        self.x_scale = alt.Scale(domain=x_domain)
        self.y_scale = alt.Scale(domain=y_domain)


    def _make_df(self, X, Y, tasks, bounds = None):
        source = pd.DataFrame({
            'x': X[:,0].tolist(),
            'y': Y[:,0].tolist(),
            'task': tasks[:,0].tolist() #  [str(int(i)) for i in tasks[:,0].tolist()]
        })
        if bounds is not None:
            source["upper"] = Y[:,0] + bounds.ravel()
            source["lower"] = Y[:,0] - bounds.ravel()
        return source


    def bands_plot(self,
                   X: ndarray, Y:ndarray, tasks: ndarray, 
                   variance: ndarray,
                   color = "grey",
                   legend = True):

        self._validate_points_plot(X, Y)

        if not legend:
            color = alt.Color("task",scale=self.scale, legend=None)
        else:
            color = alt.Color("task",scale=self.scale)

        df = self._make_df(X, Y, tasks, variance)

        return alt.Chart(df).mark_area(
            opacity=0.5, clip=True
        ).encode(
            x=alt.X('x',scale=self.x_scale),
            y=alt.Y('lower', scale=self.y_scale),
            y2='upper',
            color=alt.Color("task",scale=self.scale, legend=None)
        )


    def points_plot(self, X: ndarray, Y: ndarray, tasks: ndarray, legend = True):
        '''plot coregionalization input points'''

        self._validate_points_plot(X, Y)
    
        source = self._make_df(X, Y, tasks)

        if not legend:
            color = alt.Color("task",scale=self.scale, legend=None)
        else:
            color = alt.Color("task",scale=self.scale)

        points = alt.Chart(source).mark_point(size=60, opacity=1, filled=True, clip=True).encode(
            x=alt.X('x',scale=self.x_scale),
            y=alt.Y('y', scale=self.y_scale),
            #shape="task",
            color=color
        )
        
        return points

    def line_plot(self, X: ndarray, Y: ndarray, tasks: ndarray, legend = True):
        self._validate_points_plot(X, Y)
    
        source = self._make_df(X, Y, tasks)

        if not legend:
            color = alt.Color("task",scale=self.scale, legend=None)
        else:
            color = alt.Color("task",scale=self.scale)

        line = alt.Chart(source).mark_line(clip=True).encode(
            x=alt.X('x',scale=self.x_scale),
            y=alt.Y('y', scale=self.y_scale),
            color=color
        )
        
        return line

    def base_plot(self, X: ndarray, Y: ndarray, tasks: ndarray, legend = True):

        source = self._make_df(X, Y, tasks)

        if not legend:
            color = alt.Color("task",scale=self.scale, legend=None)
        else:
            color = alt.Color("task",scale=self.scale)

        return alt.Chart(source).encode(
            x='x:Q',
            y='y:Q',
            color=color,
            shape="task"
        )

    def _validate_points_plot(self, X, Y):
        if len(X) != len(Y):
            raise ValueError(f"X and Y must be the same length but X is len {len(X)} and Y is len {len(Y)} " )