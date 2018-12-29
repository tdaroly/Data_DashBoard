import sys
sys.path.append("..")
from DataScripts.data import grouped_df,lat,lon,well_names
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from enum import Enum     # for enum34, or the stdlib version
from plotly.offline import download_plotlyjs, init_notebook_mode, plot,iplot

plotly.tools.set_credentials_file(username='tdaroly2', api_key='gYvalucu7J5Z8eveMbPR')
mapbox_access_token = 'pk.eyJ1IjoiamFja2x1byIsImEiOiJjajNlcnh3MzEwMHZtMzNueGw3NWw5ZXF5In0.fk8k06T96Ml9CLGgKmk81w'  # noqa: E501

trace = dict(
type="scattermapbox",
visible=True,
lon=lon,
lat=lat,
ids=well_names,
text= well_names,
mode="markers",
hoverinfo="text",
marker=dict(
        color='#8BA870'
    )
,    hoverlabel = dict(
    bgcolor ="magenta",
    bordercolor="black",
        font = dict(
        family="Comic Sans",
        size=25
            
        )
    ),
fillcolor="magenta",


    
)

layout = dict(
  
    paper_bgcolor='#111111',
    plot_bgcolor='#111111',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="dark",
        bearing=0,
        center=dict(
            lat=45,
            lon=-73
        )
    ),
       geo = dict(
            scope='usa',
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 1.5
        )
         
)
data = [trace]
fig=go.Figure(data=data,layout=layout)
#py.iplot(fig)
#plot(fig) #run for testing fam