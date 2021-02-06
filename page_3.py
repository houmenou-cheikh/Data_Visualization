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

page_3_layout = html.Div([
    dbc.Row([dbc.Col(html.H1("The Impact of Covid-19 Pandemic on the Global Economy", style={'textAlign':'center'}))]),
    dbc.Row([dbc.Col(html.Div(html.H3("ETUDE DE L'IMPACT DE lA COVID PAR PAYS OU GROUPES DE PAYS")),style={'textAlign':'center',"color": "blue"}),
            dbc.Col(html.Div([html.Hr(),html.Br(),
                            dcc.Dropdown(id='dropdown-3', multi=False, className="four columns",
                                    options=[{'label':name, 'value':name} for name in countries],
                                    value = countries[68]),
                            dcc.Checklist(id="checklist-1",
                                    options=[   {'label': 'Total Cases', 'value': 'TC'},
                                                {'label': 'Total Deaths', 'value': 'TD'},],
                                    value=['TC','TD'],
                                    labelStyle={'display': 'block'}),
                    html.Div([ 
                    html.Div(dcc.Graph(id='graph-4'), className="four columns"),], className="row"),

            ]), width=8),

            dbc.Col(html.Div(id='page-3-content')),
            dbc.Col(html.Div(dcc.Link('Go at home ', href='/'),), style={'textAlign':'right'}, width=3),
            dbc.Col(html.Div(dcc.Link('Go to Page 2 ', href='/page-2'),), style={'textAlign':'left'}, width=3)
        ]), 
        
    ])
