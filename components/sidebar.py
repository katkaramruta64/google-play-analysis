from dash import html, dcc
import dash_bootstrap_components as dbc

sidebar = html.Div([
    html.H2("Google Play Dashboard", className="display-6"),
    html.Hr(),
    dbc.Nav([
        dbc.NavLink("Home", href="/", active="exact"),
        dbc.NavLink("Trends", href="/trends", active="exact"),
        dbc.NavLink("Price Analysis", href="/price-analysis", active="exact"),
        dbc.NavLink("Comparisons", href="/comparisons", active="exact"),
    ], vertical=True, pills=True),
], className="sidebar")
