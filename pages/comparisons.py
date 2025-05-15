import dash
from dash import dcc, html, callback, Input, Output
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/comparisons")

df = pd.read_csv("data/google_play_data.csv")

layout = html.Div(
    [
        html.H2("App Comparisons", className="display-5"),
        
        # Dropdown filter
        html.Label("Select Category:"),
        dcc.Dropdown(
            id="category-filter",
            options=[{"label": cat, "value": cat} for cat in df["Category"].unique()],
            value=None,
            clearable=True,
            placeholder="Select a category...",
        ),

        # Graph
        dcc.Graph(id="scatter-plot"),
    ],
    style={"padding": "40px"},
)


# Callback for interactivity
@callback(
    Output("scatter-plot", "figure"),
    [Input("category-filter", "value")]
)
def update_scatter_plot(selected_category):
    filtered_df = df if not selected_category else df[df["Category"] == selected_category]

    fig = px.scatter(
        filtered_df,
        x="Rating Count",
        y="Maximum Installs",
        color="Category",
        size="Rating",
        log_y=True,
        title="App Popularity: Installs vs Ratings",
    )
    return fig
