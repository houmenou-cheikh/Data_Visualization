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
from dash.dependencies import Input, Output


################################### nettoyage et redimentionnement des data #########################################
data = pd.read_csv("dataCovid.csv") 
data_1 = pd.read_csv("raw_data.csv") 
data[["TC","TD","POP", "GDPCAP", "STI"]] = data_1[["total_cases","total_deaths","population", "gdp_per_capita","stringency_index"]]
data["DATE"] = pd.to_datetime(data['DATE'])
data = data.fillna(0)
data_2 = data.groupby("CODE").last()
data["DATE_2"] = pd.to_datetime(data['DATE'])

data_3= pd.DataFrame()
for pays in data["COUNTRY"].unique():
    a = data[data["COUNTRY"] == pays].groupby(pd.Grouper(key='DATE', freq='M')).last() ## 
    data_3= pd.concat([data_3, a], axis=0)


data_FR_USA = data_3[(data_3["COUNTRY"] == 'France') | (data_3["COUNTRY"] == 'United States')]
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
############################################################################

fig0 = px.bar(data_FR_USA, x=data_FR_USA["DATE_2"], y=data_FR_USA["TC"],color=data_FR_USA["COUNTRY"], barmode="group")

fig0.update_layout(
    plot_bgcolor='#111111',
    paper_bgcolor='#111111',
    font_color='white'
)

#############################################################################
fig1 = make_subplots(
    rows=3, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.03,
    specs=[[{"type": "table"}],
           [{"type": "scatter"}],
           [{"type": "scatter"}]]
)

fig1.add_trace(
    go.Scatter(
        x=data["DATE"].unique(),
        y=data["TC"],
        mode="lines+markers",
        name="Total des cas positifs"
    ),
    row=3, col=1)

fig1.add_trace(go.Scatter(
        x=data["DATE"].unique(),
        y=data["TD"],
        mode="lines+markers",
        name="Total décés"
    ),
    row=3, col=1
)

fig1.add_trace(
    go.Scatter(
        x=data["DATE"].unique(),
        y=data["STI"],
        mode="lines",
        name="Strategie"
    ),
    row=2, col=1)

fig1.add_trace(go.Scatter(
        x=data["DATE"].unique(),
        y=data["HDI"],
        mode="lines",
        name="IDH"
    ),
    row=2, col=1
)

fig1.add_trace(
    go.Table(
        header=dict(
            values=["CODE" , "COUNTRY" , "DATE","HDI", "TC", "TD", "STI", "POP","GDPCAP"],

            font=dict(size=10),
            align="left"
        ),
        cells=dict(
            values=[data_3[k].tolist() for k in data_3.columns[:]],
            align = "left")
    ),
    row=1, col=1
),
fig1.update_layout(
    height=700,
    showlegend=True,
    title_text="Graphe1: Recessement des données (tableau) de tous les pays en 2020 \n Graphe2 et Graphe3: étude du nombre de cas positifs et du nombre de décées au cours de la pandémie ",
)
##############################################################################################################

markdown_text = """La pandémie de Covid-19 Écouter est une pandémie d'une maladie infectieuse émergente, 
appelée la maladie à coronavirus 2019 ou Covid-19, provoquée par le coronavirus SARS-CoV-2,\n 
apparue à Wuhan le 16 novembre 2019, dans la province de Hubei (en Chine centrale), 
avant de se propager dans le monde.\nL'Organisation mondiale de la santé (OMS) alerte \n
dans un premier temps la République populaire de Chine et ses autres États membres, puis 
prononce l'état d'urgence de santé publique de portée internationale le 30 janvier 2020.\n\n
                        
            """
########################################################################################################
page_2_layout  = html.Div(
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

        html.H6(children="""Compraison du Nombre de cas totaux entre la France et les Etats-Unis """,
                style={"fontSize": "48px", "color": "green"},),
        html.Br(),
        dcc.Graph(figure = fig0),
#################
        dcc.Graph(figure = fig1),

#################

    html.Div(id='page-2-content'),
    html.Br(),
    dcc.Link('Go to Page 3', href='/page-3'),
    html.Br(),
    dcc.Link('Go back to home', href='/')
])