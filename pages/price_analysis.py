import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

dash.register_page(__name__, path="/price-analysis")

# Load dataset
df = pd.read_csv("data/google_play_data.csv")  # Update with actual file path

# Extract unique categories
categories = df["Category"].unique()

# Layout
layout = dbc.Container([
    html.H3("Category-wise Free vs Paid Apps", className="text-center text-black"),

    # Dropdown to select category
    dcc.Dropdown(
        id="category-dropdown",
        options=[{"label": cat, "value": cat} for cat in categories],
        value=categories[0],  # Default selection
        placeholder="Select a Category",
        clearable=False,
        style={"width": "50%"}
    ),

    # Graph to display free vs paid distribution
    dcc.Graph(id="price-category-chart")
], fluid=True)

# Callback to update graph based on selection
@dash.callback(
    Output("price-category-chart", "figure"),
    [Input("category-dropdown", "value")]
)
def update_price_chart(selected_category):
    # Filter data
    filtered_df = df[df["Category"] == selected_category]

    # Count Free vs Paid Apps
    price_counts = filtered_df["Type"].value_counts().reset_index()
    price_counts.columns = ["App Type", "Count"]

    # Create Pie Chart
    fig = px.pie(price_counts, names="App Type", values="Count",
                 title=f"Free vs Paid Apps in {selected_category}",
                 color="App Type",
                 color_discrete_map={"Free": "green", "Paid": "blue"})

    return fig
