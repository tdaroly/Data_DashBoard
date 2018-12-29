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

#countyName="Andrews"
def piechart(countyName):
    df_occurences = df.loc[df["CountyName"]==countyName].groupby(by=["OperatorName"]).size().to_frame().reset_index().rename(index=str, columns={0: "Occurences"})
    labels = list(df_occurences["OperatorName"].sort_values())
    values = list(df_occurences["Occurences"].sort_values())
    red = Color("#66ffea")
    colors = list(red.range_to(Color("#f442f4"),len(labels)))
    colors = [item.hex for item in colors]
    colors = gradient_generator(len(labels),"#66ffea","#f442f4")
    trace = go.Pie(labels=labels,hole=0.2, 
                    hoverinfo='label+percent',
                   textinfo='value+label',
                   textfont=dict(size=14,family="Work Sans"),
                   values=values,
                   opacity=1,
                   marker=dict(colors=colors,
                        line=dict(color='#000000', width=2)),
                        
                    insidetextfont=dict(family="Work Sans",color="white"),
                    outsidetextfont=dict(family="Work Sans",
                                        color="white"
                                        )
                   

                    
                    
                    )

    data=[trace]
    layout=dict(title= "Oil Provider's for: <b>{}</b>".format(countyName),
    font=dict(family='Work Sans', size=14, color='white'),
    paper_bgcolor='#111111',
    plot_bgcolor='#111111',
    showlegend=False,
  
    autosize=True,
    legend= dict(
        orientation='h',
                font=dict( 
                     family="Work Sans",
                    size =6,
                    color="black"),
        bgcolor='#E2E2E2',
        bordercolor='#FFFFFF'
                )
            )

    fig=go.Figure(data=data,layout=layout)
    return fig