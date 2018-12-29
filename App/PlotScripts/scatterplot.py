import sys
sys.path.append("..")
from DataScripts.data import grouped_df,lat,lon,well_names,df
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot

import plotly.plotly as py
import plotly.graph_objs as go


def scatterplot(wellname):

    df_scatter = df.loc[df["WellName"]==wellname]
    if len(df_scatter.groupby(by=["IngredientName"]).count()) == 0:
        print("Its been said and done")
        return None
    else:
        df_scatter = df_scatter.groupby(by=["IngredientName"]).mean()["PercentHFJob"].to_frame().reset_index()

    trace = dict(
    x=df_scatter["IngredientName"],
    y=df_scatter["PercentHFJob"],
    marker = dict(color="#FFD7E9",size=12),
    mode="markers",
    text = df["IngredientName"],
    type = "scatter",
    hoverinfo="text",
    hoveron="points",
    orientation="v")

    data = [trace]
    layout = dict(
        #height=650,
    #width=700,
     title="Ingred",
     paper_bgcolor='#111111',
    plot_bgcolor='#111111',
    font=dict(family='Work Sans', size=15, color='white'),
    
        yaxis=dict(
            title="Occurences"
        ))

    fig = go.Figure(data=data, layout=layout)
    return fig