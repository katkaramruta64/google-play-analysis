import dash
from dash import html

dash.register_page(__name__, path="/")  # No `path="/"` needed

layout = html.Div(
    [
        html.H1("Welcome to Google Play Analysis Dashboard", className="display-4"),
        html.P("Explore trends, pricing, and app comparisons."),
    ],
    style={"padding": "40px"},
)
