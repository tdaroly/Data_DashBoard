import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/iris.csv')
df.head()


def well_bore():
    def brownian_motion(T = 1, N = 100, mu = 0.1, sigma = 0.01, S0 = 20):
        dt = float(T)/N
        t = np.linspace(0, T, N)
        W = np.random.standard_normal(size = N)
        W = np.cumsum(W)*np.sqrt(dt) # standard brownian motion
        X = (mu-0.5*sigma**2)*t + sigma*W
        S = S0*np.exp(X) # geometric brownian motion
        return S

    dates = pd.date_range('2012-01-01', '2013-02-22')
    T = (dates.max()-dates.min()).days / 365
    N = dates.size
    start_price = 100
    y = pd.Series(
        brownian_motion(T, N, sigma=10, S0=start_price), index=dates)
    z = pd.Series(
        brownian_motion(T, N, sigma=12, S0=start_price), index=dates)

    trace = go.Scatter3d(
        x=list(dates), y=y, z=z,
        marker=dict(
            size=4,
            color=z,
            colorscale='Viridis',
        ),
        line=dict(
            color='#1f77b4',
            width=1
        )
    )

    data = [trace]

    layout = dict(
        width=450,
        height=470,
        autosize=False,
        title='Well Bore of well ##',
        scene=dict(
            xaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            yaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            zaxis=dict(
                gridcolor='rgb(255, 255, 255)',
                zerolinecolor='rgb(255, 255, 255)',
                showbackground=True,
                backgroundcolor='rgb(230, 230,230)'
            ),
            camera=dict(
                up=dict(
                    x=0,
                    y=0,
                    z=1
                ),
                eye=dict(
                    x=-1.7428,
                    y=1.0707,
                    z=0.7100,
                )
            ),
            aspectratio = dict( x=1, y=1, z=0.7 ),
            aspectmode = 'manual'
        ),
    )

    fig = dict(data=data, layout=layout)
    return fig
    #plot(fig)