import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# Initialize Dash app
app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Sidebar layout with more padding
sidebar = html.Div(
    [
        html.H3("Google Play Analysis Dashboard", className="text-white text-center mb-4"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Trends", href="/trends", active="exact"),
                dbc.NavLink("Price Analysis", href="/price-analysis", active="exact"),
                dbc.NavLink("Comparisons", href="/comparisons", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="sidebar-col",
    style={
        "background-color": "#002B5B",  # Dark blue
        "padding": "20px 15px",  # Increased left & right padding
        "color": "white",
        "width": "260px",  # Slightly wider for better spacing
        "min-height": "100vh",
    },
)

# Navbar with improved button size
navbar = html.Div(
    [
        html.Button("☰ Menu", id="menu-toggle", className="btn btn-light", style={"font-size": "18px", "padding": "8px 12px"}),
    ],
    className="d-flex justify-content-start p-3 bg-dark text-white",
)

# Main layout
app.layout = html.Div(
    [
        navbar,
        html.Div(
            [
                sidebar,
                html.Div(dash.page_container, className="main-content", style={"flex-grow": "1", "padding": "30px", "max-width": "80%"}),  # Reduce empty space
            ],
            className="d-flex",
        ),
    ]
)

# Sidebar toggle callback
@app.callback(
    Output("sidebar-col", "style"),
    [Input("menu-toggle", "n_clicks")],
    [State("sidebar-col", "style")],
)
def toggle_sidebar(n, current_style):
    if n and current_style.get("display", "block") == "block":
        return {**current_style, "display": "none"}  # Hide sidebar
    return {**current_style, "display": "block"}  # Show sidebar

if __name__ == "__main__":
    app.run(debug=True)
