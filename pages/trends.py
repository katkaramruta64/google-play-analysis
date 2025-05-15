import dash
from dash import dcc, html, callback, Input, Output
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/trends")

# Load dataset
df = pd.read_csv("data/google_play_data.csv")

# Convert Last Updated to Year format
df["Year"] = pd.to_datetime(df["Last Updated"], errors="coerce").dt.year

# Layout
layout = html.Div(
    [
        html.H2("App Install Trends", className="display-5"),
        
        # Dropdown for category selection
        html.Label("Select App Category:"),
        dcc.Dropdown(
            id="category-dropdown",
            options=[{"label": cat, "value": cat} for cat in df["Category"].unique()],
            value=None,
            clearable=True,
            placeholder="Select a category...",
        ),

        # Slider for rating filter
        html.Label("Minimum App Rating:"),
        dcc.Slider(
            id="rating-slider",
            min=df["Rating"].min(),
            max=df["Rating"].max(),
            step=0.1,
            marks={i: str(i) for i in range(int(df["Rating"].min()), int(df["Rating"].max()) + 1)},
            value=df["Rating"].min(),
        ),

        # Graph
        dcc.Graph(id="install-trend-graph"),
    ],
    style={"padding": "40px"},
)


# Callback for interactivity
@callback(
    Output("install-trend-graph", "figure"),
    [Input("category-dropdown", "value"),
     Input("rating-slider", "value")]
)
def update_trend_graph(selected_category, min_rating):
    filtered_df = df[df["Rating"] >= min_rating]
    
    if selected_category:
        filtered_df = filtered_df[filtered_df["Category"] == selected_category]

    installs_over_time = filtered_df.groupby("Year")["Maximum Installs"].sum().reset_index()

    fig = px.line(
        installs_over_time,
        x="Year",
        y="Maximum Installs",
        title="Total Installs Over Time",
        markers=True,
    )

    return fig
