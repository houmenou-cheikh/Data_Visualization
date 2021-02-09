import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors
from page_1 import data , data_1 , data_3
from page_2 import data_2
import dash_bootstrap_components as dbc


print(" ")
df = data_3
X = df.TC.values[:, None]
X_train, X_test, y_train, y_test = train_test_split(
    X, df.TD , random_state=42)

models = {'Regression': linear_model.LinearRegression,
          'Decision Tree': tree.DecisionTreeRegressor,
          'k-NN': neighbors.KNeighborsRegressor}

###########################################################################################################

page_4_layout = html.Div([
    dbc.Row([dbc.Col(html.H1("Étude de l'impact de la covid-19 sur l'économie: PRÉDICTION DE DÉCÉS ", 
                                    style={"fontSize": "36px", "color": "blue",'textAlign':'center'},)),]),
    html.Br(),html.Br(),
    dbc.Row([dbc.Col(html.Div(html.H4("NIVEAU MONDIAL : Prédiction du nombre de déces (TD) sur focntion du nombre de cas (TC)")),
                    style={"fontSize": "32px", 'textAlign':'center',"color": "orange"}),]),
                               
    dcc.Dropdown(
        id='model-name',style={'color':"blue"},
        options=[{'label': x, 'value': x} 
                 for x in models],
        value='Regression',
        clearable=False
    ),

    dcc.Graph(id="graph"),
    html.Br(),html.Br(),
    dbc.Row([dbc.Col(html.Div(html.H4("NIVEAU NATIONAL: Prédiction du nombre de déces sur fonction du nombre de cas")),
                    style={"fontSize": "34px",'textAlign':'center',"color": "orange"}),]),

    html.Br(),
    dcc.Dropdown(id='page-4-dropdown',style={'color':"blue"},
        options=[{'label': i, 'value': i} for i in data_3["COUNTRY"].unique()],
        value='France'),
    html.Br(),
    dcc.RadioItems(id="radiobutton",
                                options=[   {'label': 'Regression', 'value': 'Regression'},
                                        {'label': 'Decision Tree', 'value': 'Decision Tree'},
                                        {'label': 'k-NN', 'value': 'k-NN'},],
                                value='Regression',
                                labelStyle={'display': 'block'}),
    dcc.Graph(id="graph_2"),

    html.Div(id='page-1-content'),

    dbc.Row([
        dbc.Button(dcc.Link('Go to Page 2', href='/page-2'),outline=True, color="warning", 
               style={"vertical-align": "left"}, className="mr-1"),

       dbc.Button(dcc.Link('Go to Page 3', href='/page-3'),outline=True, color="secondary",
                 style={"vertical-align": "right"}, className="mr-1"),

        dbc.Button(dcc.Link('Go at home', href='/'),outline=True, color="danger",
                 style={"vertical-align": "right"}, className="mr-1"),
    ])
])

