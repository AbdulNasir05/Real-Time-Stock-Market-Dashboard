# Real-Time Stock Market Dashboard

A Streamlit-based dashboard for tracking and visualizing live stock market data with candlestick charts and financial indicators.

## Stack
- Python (Pandas, Plotly, Requests)
- Streamlit
- Alpha Vantage API (or any stock market API)

## Features
- Live intraday stock data
- Interactive candlestick charts with moving average overlay
- RSI indicator
- Refresh data by clicking button

## Quick Start (Docker)
```bash
cp .env.example .env
# Add your Alpha Vantage API key to .env
docker compose up --build

