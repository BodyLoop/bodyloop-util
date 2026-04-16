from dash import html, dcc

layout = html.Div(
    [
        html.Div(
            [
                html.Label("Base URL", style={"width": "8rem", "marginRight": "0.75rem"}),
                dcc.Input(
                    id="base-url-input",
                    type="text",
                    placeholder="https://bodyloop-control-pc ",
                    persistence=True,
                    persistence_type="local",
                    style={"width": "24rem"},
                ),
            ],
            style={"display": "flex", "alignItems": "center", "marginBottom": "0.5rem"},
        ),
        html.Div(
            [
                html.Label("Username", style={"width": "8rem", "marginRight": "0.75rem"}),
                dcc.Input(
                    id="username-input",
                    type="text",
                    placeholder="your-username",
                    persistence=True,
                    persistence_type="local",
                    style={"width": "24rem"},
                ),
            ],
            style={"display": "flex", "alignItems": "center", "marginBottom": "0.5rem"},
        ),
        html.Div(
            [
                html.Label("Password", style={"width": "8rem", "marginRight": "0.75rem"}),
                dcc.Input(
                    id="password-input",
                    type="password",
                    placeholder="Your password",
                    persistence=True,
                    persistence_type="local",
                    style={"width": "24rem"},
                ),
            ],
            style={"display": "flex", "alignItems": "center"},
        ),
    ],
    style={"marginBottom": "1.5rem"},
)
