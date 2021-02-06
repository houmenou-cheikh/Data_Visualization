import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import index
import page_1 ,page_2, page_3, page_4
from page_1  import *
from page_2 import *
from page_3  import *
from page_4  import *


print(dcc.__version__) # 0.6.0 or above is required
app = dash.Dash()

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
#########################################################################################
# Page 1 callback
@app.callback(Output('indicator-graphic', 'figure'),
              [Input('page-1-dropdown', 'value')])

def page_1_dropdown(value):
    
    data_pays = page_1.data_3 [page_1.data_3 .COUNTRY == value]

    fig2 = go.Figure()
    # Add traces
    fig2.add_trace(go.Scatter(x=data_pays["DATE_2"] , y=data_pays["TC"],
                        mode='lines+markers',
                        name='TC'))

    fig2.add_trace(go.Scatter(x=data_pays["DATE_2"] , y=data_pays["TD"],
                        mode='lines+markers',
                        name='TD'))

    fig2.add_trace(go.Scatter(x=data_pays["DATE_2"] , y=data_pays["STI"],
                        mode='lines+markers',
                        name='STI'))
    return fig2

 

##################################################################################################
# Page 2
@app.callback(Output('page-2-content', 'children'),
              [Input('page-2-radios', 'value')])

def page_2_radios(value):
    return 'You have selected "{}"'.format(value)

################################################################
#####page_3
@app.callback(Output("graph-4", "figure"), 
            [Input("dropdown-3", "value"),
            Input("checklist-1", "value")]) 
    
def update_graph_5(value,checklist_value): 

    df_plot = data_3[data_3.COUNTRY == f"{value}"]    
    # ############################################## Plot ################################################     
    fig = go.Figure()    
    if "TC" in checklist_value:         
        fig=fig.add_trace(go.Scatter(x=df_plot.DATE_2, y=df_plot.TC, mode='lines+markers', name='Total Cases'))                  
    if "TD" in checklist_value:         
        fig=fig.add_trace(go.Scatter(x=df_plot.DATE_2, y=df_plot.TD, mode='lines+markers', name='Total Deaths'))           

    return fig

############################################################################################################
########### Page-4

@app.callback(
    Output("graph", "figure"), 
    [Input('model-name', "value")])

def train_and_display(name):
    model = models[name]()
    model.fit(X_train, y_train)

    x_range = np.linspace(X.min(), X.max(), 100)
    y_range = model.predict(x_range.reshape(-1, 1))
    
    fig = go.Figure([
        go.Scatter(x=X_train.squeeze(), y=y_train, 
                   name='train', mode='markers'),
        go.Scatter(x=X_test.squeeze(), y=y_test, 
                   name='test', mode='markers'),
        go.Scatter(x=x_range, y=y_range, 
                   name='prediction')
    ])

    return fig
    
#############################################################################################################
# Index Page callback
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return page_1.page_1_layout
    elif pathname == '/page-2':
        return page_2.page_2_layout
    elif pathname == '/page-3':
        return page_3.page_3_layout
    elif pathname == '/page-4':
        return page_4.page_4_layout
    else:
        return '404'

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

if __name__ == '__main__':
    app.run_server(debug=True)