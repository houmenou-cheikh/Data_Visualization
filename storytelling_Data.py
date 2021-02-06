#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.graph_objects as gos
from plotly.subplots import make_subplots
import re
import plotly.express as px
from dash.dependencies import Input, Output



data = pd.read_csv("dataCovid.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
############################################################################

#fig0 = px.bar(data, x="TC", y="DATE", color="COUNTRY", barmode="group")

fig0 = px.bar(data, x=data["DATE"], y=data["TC"],color=data['COUNTRY'], barmode="group")

fig0.update_layout(
    plot_bgcolor='#111111',
    paper_bgcolor='#111111',
    font_color='white'
)

#############################################################################
fig = make_subplots(
    rows=3, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.03,
    specs=[[{"type": "table"}],
           [{"type": "scatter"}],
           [{"type": "scatter"}]]
)

fig.add_trace(
    go.Scatter(
        x=data["DATE"].unique(),
        y=data["TC"],
        mode="lines+markers",
        name="Total des cas positifs"
    ),
    row=3, col=1)

fig.add_trace(go.Scatter(
        x=data["DATE"].unique(),
        y=data["HDI"],
        mode="lines",
        name="IDH"
    ),
    row=3, col=1
)

fig.add_trace(
    go.Scatter(
        x=data["DATE"].unique(),
        y=data["TD"],
        mode="lines",
        name="TOTAl des  DECES"
    ),
    row=2, col=1)

fig.add_trace(go.Scatter(
        x=data["DATE"].unique(),
        y=data["HDI"],
        mode="lines",
        name="IDH"
    ),
    row=2, col=1
)

fig.add_trace(
    go.Table(
        header=dict(
            values=["CODE" , "COUNTRY" , "DATE","HDI", "TC", "TD", "STI", "POP","GDPCAP"],

            font=dict(size=10),
            align="left"
        ),
        cells=dict(
            values=[data[k].tolist() for k in data.columns[:]],
            align = "left")
    ),
    row=1, col=1
),
fig.update_layout(
    height=800,
    showlegend=True,
    title_text="évolution mondiale de la covid19 ",
)
##############################################################################################################


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

markdown_text = """La pandémie de Covid-19 Écouter est une pandémie d'une maladie infectieuse émergente, 
appelée la maladie à coronavirus 2019 ou Covid-19, provoquée par le coronavirus SARS-CoV-2,\n 
apparue à Wuhan le 16 novembre 2019, dans la province de Hubei (en Chine centrale), 
avant de se propager dans le monde.\nL'Organisation mondiale de la santé (OMS) alerte \n
dans un premier temps la République populaire de Chine et ses autres États membres, puis 
prononce l'état d'urgence de santé publique de portée internationale le 30 janvier 2020.\n\n
                        
            """
########################################################################################################
app.layout = html.Div(
    children=[
        html.H1(children="""Impact de la pandémie de Covid-19 sur l'économie mondiale:
                            accent sur la réduction de la pauvreté et la croissance économique""",
                style={"fontSize": "48px", "color": "blue"},),
        
#################
        dcc.Markdown(children=markdown_text),
        dcc.Link('source Wikipedia', href="https://fr.wikipedia.org/wiki/Pand%C3%A9mie_de_Covid-19"),
        html.Br(),
        dcc.Link('Source Projet',href="https://data.mendeley.com/datasets/b2wvnbnpj9/1"),
#################
        html.P(
            children=html.H2("Évaluation de l'impact de la pandémie sur économie mondiale",
             style={ 'textAlign': 'center','color': 'orange'}),  
        ),
#################
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["COUNTRY"].unique(),
                        "y": data["POP"].unique(),
                        "type": "lines",
                    },
                ],
                "layout": {"title": "la répartition de la population mondiale en fonctionde leur localisation "},
            },
        ),
#################
        html.Br(),

        html.H6(children="""Évolution du Nombre de cotaminants en 2020 """,
                style={"fontSize": "48px", "color": "green"},),
        html.Br(),
        dcc.Graph(figure = fig0),
#################
        dcc.Graph(figure = fig),

#################
        dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in data.COUNTRY.unique()],
                value='choisir un pays'
            ),

    
#################
        dcc.Location(id='url', refresh = False),

        html.Br(),
        dcc.Link('page suivante', href='/page-2'),

    

    ]
)
@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'))

def update_graph(xaxis_column_name):

        dff = data[data['COUNTRY'] == value]

        fig1 = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                        y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                        hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

        return fig1

#############################################################################""
if __name__ == "__main__":
    app.run_server(debug=True)
