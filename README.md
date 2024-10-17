# Stock-Dashboard

A live-updating stock dashboard that tracks the top S&P 500 companies using Yahoo Finance data. This dashboard is built using [Dash](https://dash.plotly.com/), with live updates every minute, showing the most recent stock prices for multiple companies.

## Features

- **Live updates** every minute.
- Tracks stock prices of top S&P 500 companies.
- Responsive layout with Bootstrap styling.

## Tech Stack

- **Python**
- **Dash** for building the web application.
- **Plotly** for interactive graphs.
- **Yahoo Finance** (`yfinance`) to retrieve stock data.
- **Bootstrap** (via `dash-bootstrap-components`) for styling.

## Installation

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Setup Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/live-stock-dashboard.git
   cd live-stock-dashboard
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source .venv/bin/activate
   ```

3. Install the required dependacies:

   ```bash
   pip3 install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python3 app.py
   ```

5. Open your browser and go to `http://127.0.0.1:8050/` to view the dashboard.

## Requirements

The `requirements.txt` includes:

```bash
dash
dash-bootstrap-components
plotly
yfinance
pandas
```

To install these, run:

```bash
pip install -r requirements.txt
```

## How It Works

- The app fetches live stock data for the top S&P 500 companies selected every minute using the `yfinance` library.

- It plots the data using Plotly graphs, where each stock is represented as a line plot.

- The dashboard automatically updates via the `dcc.Interval` component.

## Customization

- You can modify the list of tracked stocks by editing the `top_sp500` list in `app.py`.

- Change the update frequency by adjusting the interval in the `dcc.Interval` component.
