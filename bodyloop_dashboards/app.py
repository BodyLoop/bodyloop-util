import argparse

from dash import Dash, html, dcc

from bodyloop_dashboards.pages import sync_excel, scan_compare, login

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H2("BodyLoop Dashboards"),
        login.layout,
        dcc.Tabs(
            id="main-tabs",
            value="sync-excel",
            children=[
                sync_excel.layout,
                scan_compare.layout,
            ],
        ),
        *sync_excel.stores,
    ],
    style={"padding": "2rem"},
)


def _parse_args():
    parser = argparse.ArgumentParser(description="Run BodyLoop Dashboards")
    parser.add_argument("--host", default="127.0.0.1", help="Host interface to bind")
    parser.add_argument("--port", type=int, default=8050, help="Port to listen on")
    return parser.parse_args()


def main():
    args = _parse_args()
    app.run(debug=True, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
