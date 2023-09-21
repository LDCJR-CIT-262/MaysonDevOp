import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import random

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the game
app.layout = html.Div([
    html.H1("Click Game"),
    html.Button("Click Me!", id="click-button"),
    html.P("Score: ", id="score"),
    dcc.Interval(id='interval-component', interval=1000, n_intervals=0)
])

# Initialize the score
score = 0

# Define the callback function to update the score
@app.callback(
    Output('score', 'children'),
    Input('click-button', 'n_clicks'),
    Input('interval-component', 'n_intervals')
)
def update_score(clicks, n_intervals):
    global score
    if clicks is not None:
        score += 1
    return f"Score: {score}"

if __name__ == '__main__':
    app.run_server(debug=True)
