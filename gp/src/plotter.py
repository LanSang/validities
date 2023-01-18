import pandas as pd
import altair as alt

class Plotter(object):

    def points_plot(self, X, Y, tasks):
        '''plot coregionalization input points'''
    
        source = pd.DataFrame({
            'x': X[:,0].tolist(),
            'y': Y[:,0].tolist(),
            'task': [str(i) for i in tasks[:,0].tolist()]
        })

        points = alt.Chart(source).mark_point(size=30).encode(
            x='x:Q',
            y='y:Q',
            color=alt.Color("task",scale=alt.Scale(scheme="dark2")),
            fill='task',
            shape="task"
        )
        
        return points