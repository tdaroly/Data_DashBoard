# -*- coding: utf-8 -*-
import dash
import json
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output,State
from DataScripts.data import grouped_df,lat,lon,df
from PlotScripts.map import fig
from PlotScripts.histogram import hist
from PlotScripts.wellbore import well_bore
from PlotScripts.piechart import piechart
from PlotScripts.scatterplot import scatterplot
import plotly.graph_objs as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "This is the start of how it ever ends"

options=[] #creating the dropdown list fam
for el in grouped_df["StateName"].unique():
    dic=[]
    dic=dict(label=el,value=el)
    options.append(dic)



#where the fun-stuff happens
app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    'Oil & Gas Dashboard',
                    id="info-top-heading"
                    
                ),
                dcc.Markdown(id="total-wells",children='''Total wells being monitored is 
                **{}** '''.format(len(lat))),
                html.H5(
                    id="state_county",
                    children="none"
                )
            ]),
            html.Div(
                [

                     dcc.Input(
               placeholder='Enter a value...',
                type='text',
                value='Sims 7-8 #1',
                id="input_hide"
                )



                    ,dcc.Dropdown(
    options=options,
    value='Colorado',
    id="dropdown-state"
),                   dcc.Dropdown(
    options={},
    value='Weld',
    id="dropdown-county"
),
                ],className="six columns"
            ),
            html.Div(
                [
                     html.Div(
                    [
                        dcc.Graph(id='geoMap',figure=fig)
                    ],
                    className='eight columns',
                    style={'margin-top': '20'}
                ),
                html.Div(
                    [
                       
                        dcc.Graph(id='wellbore',figure=well_bore())
                    ],
                    className='four columns',
                    style={'margin-top': '20'}
                )
            
            
            
            
            
            ],className="row"
            ),
            html.Div([
                html.Div([
                    dcc.Graph(id="histogram",figure=hist("Sims 7-8 #1"))
                ],className="four columns",style={'margin-top': '10'}),

                html.Div([
                    dcc.Graph(id="pie-chart",figure=piechart("Weld"))
                ],className="four columns",style={'margin-top': '10'}),
                html.Div([
                    
                    dcc.Graph(id="scatter-plot",figure=scatterplot("Sims 7-8 #1"))
                ],className="four columns",style={'margin-top': '10'}),
                
                

            ],
            className="row") 
        



],className="ten columns offset-by-one")
@app.callback(
    Output("dropdown-county","options"),
    [(Input("dropdown-state","value"))]
)
def changeddval(value):
    dff = grouped_df.groupby(by=["StateName","CountyName"]).mean()
    dff = dff.reset_index()
    county_names = dff.loc[dff["StateName"]==value]["CountyName"].unique()
    return [{'label':i,'value':i} for i in county_names]

@app.callback(
    Output("state_county","children"),
    [Input("dropdown-state","value"),
    Input("dropdown-county","value")])
def changeH3(state,county):
    return "You selected state: {} and county {}".format(state,county)

@app.callback(
    Output('histogram','figure'),
    [Input('geoMap','clickData')],
    [State('input_hide','value')]
)
def changer(clickData,input2):
    if clickData is not None:
        wellname=clickData['points'][0]['text']
        return hist(wellname)
    else:
        return hist(input2)


@app.callback(
    Output('scatter-plot','figure'),
    [Input('geoMap','clickData')],
    [State('input_hide','value')]
)
def changer_scatterplot(clickData,value2):
    if clickData is not None:
        wellname=clickData['points'][0]['text']        
    else:
        wellname = value2
    return scatterplot(wellname)

@app.callback(
    Output('pie-chart','figure'),
    [Input('dropdown-county','value')]
)
def pie(value):
    return piechart(value)






       
if __name__ == '__main__':
    app.run_server(debug=True)