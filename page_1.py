import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.graph_objects as gos
from plotly.subplots import make_subplots
import re
import plotly.express as px
import dash_bootstrap_components as dbc


##################################### recup données et nettoyage ##################################
data = pd.read_csv("dataCovid.csv") 
data_1 = pd.read_csv("raw_data.csv") 
data[["TC","TD","POP", "GDPCAP", "STI"]] = data_1[["total_cases","total_deaths",
                                                    "population", "gdp_per_capita","stringency_index"]]
data["DATE"] = pd.to_datetime(data['DATE'])
data["DATE_2"] = pd.to_datetime(data['DATE'])

data = data.fillna(0)
data_3 = pd.DataFrame()
for pays in data["COUNTRY"].unique():
    a = data[data["COUNTRY"] == pays].groupby(pd.Grouper(key='DATE', freq='M')).last() ## 
    data_3= pd.concat([data_3, a], axis=0)

######################################################################################################

fig = px.scatter_geo(data_3, locations= 'CODE',
                     hover_name='COUNTRY', size= "TD")

fig1 = px.choropleth(data_3, color="TC", locations="CODE", hover_name='COUNTRY')
fig1.add_trace(fig.data[0])

fig1.update_traces(marker_color="rgba(0,0,0,0)" ,
                    selector=dict(type='scattergeo'))

fig1.update_layout(height=700,
                title_text= "la répartition du nombre de cas totaux (TC) en fonction de leur localisation ",
                showlegend=True)

    
########################################################################################################
page_1_layout = html.Div([
    dbc.Alert(html.H1("Étude de l'impact de la covid-19 sur l'économie pour pays choisi ",
                                    style={"fontSize": "42px", "color": "blue"},),),
    
    dcc.Dropdown(id='page-1-dropdown',
        options=[{'label': i, 'value': i} for i in data["COUNTRY"].unique()],
        value='France'
    ),

    html.Br(),
    dcc.Graph(id='indicator-graphic'),

    html.H1(" Vision globale du numbre de décées (TD) liés à la covid-19 en octobre 2020 ",
                                    style={"fontSize": "25px", "color": "blue"},),
    

    html.Br(),
    dcc.Graph(figure = fig1),

    html.Div(id='page-1-content'),
    html.Br(),
    dbc.Row([
        dbc.Button(dcc.Link('Go to Page 2', href='/page-2'), size="lg", color="primary", 
               style={"vertical-align": "left"}, className="mr-1"),

       dbc.Button(dcc.Link('Go to Page 3', href='/page-3'), size="lg", color="green",
                 style={"vertical-align": "right"}, className="mr-1"),

        dbc.Button(dcc.Link('Go to Page 4', href='/page-4'), size="lg", color="red",
                 style={"vertical-align": "right"}, className="mr-1"),
    ])
])
#table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)
