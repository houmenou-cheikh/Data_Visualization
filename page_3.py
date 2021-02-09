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


################################################ Data prepare ##############################################################
data = pd.read_csv("dataCovid.csv") 
data_1 = pd.read_csv("raw_data.csv") 
data[["TC","TD","POP", "GDPCAP", "STI"]] = data_1[["total_cases","total_deaths","population",
                                                 "gdp_per_capita","stringency_index"]]
data["DATE"] = pd.to_datetime(data['DATE'])
data = data.fillna(0)
countries=data.COUNTRY.unique()

############################################## layout page 3 ######################################################

page_3_layout = html.Div([dbc.Alert(
    "The Impact of Covid-19 Pandemic on the Global Economy",color="light", 
    style={'textAlign':'center',"color": "white","fontSize": "40px"},className="m-5"),

 
        dbc.Col([html.Hr(style={"color": "white"}), html.H3("ETUDE DE L'IMPACT DE lA COVID PAR PAYS", 
        style={'textAlign':'center',"color": "blue"}), html.Hr(style={"color": "white"}), 

                        dcc.Dropdown(id='dropdown-3', multi=False, className="four columns",style={'color':"blue"},
                                    options=[{'label':name, 'value':name} for name in countries],
                                    value = countries[68]),

                        html.Br(), html.Br(),

                        dcc.Checklist(id="checklist-1",
                                options=[   {'label': 'Total Cases', 'value': 'TC'},
                                        {'label': 'Total Deaths', 'value': 'TD'},],
                                value=['TC','TD'],
                                labelStyle={'display': 'block'}),

                    
                html.Div(dcc.Graph(id='graph-4'),)

            ]),
###################################################################################################

        dbc.Row([
        dbc.Button(dcc.Link('Go to Page 2', href='/page-2'),outline=True, color="warning", 
                style={"vertical-align": "left"}, className="mr-1"),

        dbc.Button(dcc.Link('Go to Page 4', href='/page-4'),outline=True, color="success",
                    style={"vertical-align": "right"}, className="mr-1"),

        dbc.Button(dcc.Link('Go at home', href='/'),outline=True, color="danger",
                    style={"vertical-align": "right"}, className="mr-1"),
    ]), 
        
    ])
