from dash import Dash, html, dcc, callback, Output, Input
import plotly.graph_objs as go
import yfinance as yf
import pandas as pd

top_sp500 = [
    'SPY', 'QQQ', 'DIA', 'IWM', 'VTI', 'AAPL', 'GOOGL', 'AMZN', 'META', 'MSFT',
    'NVDA', 'AMD', 'INTC', 'WM', 'RSG', 'TSLA', 'SHOP', 'NFLX', 'PG', 'KO', 'MCD'
]

def get_stock_data(symbols):
    data = yf.download(symbols, period='1d', interval='1m')['Adj Close'].iloc[-1]
    return data

app = Dash(__name__, external_stylesheets=['/assets/styles.css'])

app.layout = html.Div([
        html.H1('Live S&P 500 Stock Dashboard', className='header'),
        dcc.Graph(id='live-stock-graph'),
        dcc.Interval(
            id='interval-component',
            interval=60*1000,
            n_intervals=0
        )
])

@app.callback(
    Output('live-stock-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)

def update_graph(_):
    prices = get_stock_data(top_sp500)

    traces = []
    for symbol in top_sp500:
        traces.append(go.Bar(
            x=[symbol],
            y=[prices[symbol]],
            name=symbol,
            marker={'color': '#cba6f7'}
        ))

    figure = go.Figure(
        data=traces,
        layout=go.Layout(
            title='Prices of Top S&P 500 Companies',
            xaxis={'title': 'Company'},
            yaxis={'title': 'Price'},
            height=600,
            plot_bgcolor='#181825',
            paper_bgcolor='#1e1e2e',
            font=dict(
                family='sans-serif',
                color='#b4befe'
            )
        )
    )
    return figure

if __name__ == '__main__':
    app.run_server()
