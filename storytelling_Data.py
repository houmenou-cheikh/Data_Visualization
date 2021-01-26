import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

data = pd.read_csv("raw_data.csv")
print(data.head())
print(data.info())
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(
    children=[
        html.H1(children="Impact de la pandémie Covid-19 sur l'économie mondiale",
                style={"fontSize": "48px", "color": "blue"},),
        html.P(
            children="Évaluation de l'impact de la pandémie sur économie mondiale",
            
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["date"],
                        "y": data["total_cases"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "nombre de cas positifs de la population "},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["location"],
                        "y": data["population"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "la répartition de la population mondiale en fonctionde leur localisation "},
            },
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
