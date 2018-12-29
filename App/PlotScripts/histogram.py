import sys
sys.path.append("..")
from DataScripts.data import grouped_df,lat,lon,well_names,df
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from enum import Enum     # for enum34, or the stdlib version
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot
from colour import Color


def gradient_generator(length,start,stop):
    start = Color(start)
    stop = Color(stop)
    colors = list(start.range_to(Color(stop),length))
    colors = [item.hex for item in colors]
    return colors

#plot(fig)
def hist(wellname):
    df_filtered = df.loc[df["WellName"]==wellname]["PercentHighAdditive"].to_frame().sort_values(by=["PercentHighAdditive"]).reset_index().drop(['index'],axis=1).reset_index().rename(index=str, columns={"index": "X"})
    trace=go.Bar(x=df_filtered["X"],y=df_filtered["PercentHighAdditive"],marker=dict(
        color=gradient_generator(len(df_filtered["X"]),"#66ffea","#f442f4")
    ),opacity=0.75)
    data=[trace]
    

    
    
    layout=dict(title="Well {}".format(wellname),
       paper_bgcolor='black',
        plot_bgcolor='black',
        font=dict(family='Work Sans', size=15, color='white'),
        xaxis=dict(
            title="Value"
        ),
        yaxis=dict(
            title="PercentHighAdditive"
        )
               
                )

    hist=go.Figure(data=data,layout=layout)
    return hist