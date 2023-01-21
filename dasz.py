from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

data = pd.read_csv("winequelity.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.Table(
        # Table header
        [html.Tr([html.Th(col) for col in data.columns])] +
        # Table rows
        [html.Tr([
            html.Td(data.iloc[i][col]) for col in data.columns
        ]) for i in range(10)]
    ),

    dcc.RadioItems(
        ['Regression', 'Classification'],
        'Linear',
        id='model-type',
        labelStyle={'display': 'inline-block', 'marginTop': '5px'}
    ),

    dcc.Dropdown(
        id='model-variable',
        options=[{'label': col, 'value': col} for col in data.columns if col != 'target'],
        value='pH'
    ),
    dcc.Graph(id='model-plot')
])

@app.callback(
    Output('model-plot', 'figure'),
    [Input('model-type', 'value'),
     Input('model-variable', 'value')])
def update_plot(model_type, model_variable):
    if model_type == 'Regression':
        fig= px.scatter(data_frame=data, x=model_variable, y='pH', color=model_variable, title=f'{model_variable} vs Target')
        return fig
    else:
        fig = px.box(data_frame=data, x=model_variable, y='target', color='target', boxmode='group',title=f'{model_variable} vs Target')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)