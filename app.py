import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
from data_fetcher import get_stock_data
from indicators import moving_average, rsi
from config import settings

st.set_page_config(page_title="Stock Dashboard", layout="wide")

st.title("📈 Real-Time Stock Market Dashboard")

symbol = st.sidebar.text_input("Stock Symbol", value="AAPL")
interval = st.sidebar.selectbox("Interval", ["1min", "5min", "15min", "30min", "60min"], index=1)

if st.sidebar.button("Fetch Data"):
    try:
        df = get_stock_data(symbol, interval)
        st.success(f"Showing {symbol} data as of {datetime.now().strftime('%H:%M:%S')}")

        fig = go.Figure(data=[go.Candlestick(
            x=df.index,
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"],
            name="Candlesticks"
        )])

        ma20 = moving_average(df, 20)
        fig.add_trace(go.Scatter(x=df.index, y=ma20, mode="lines", name="MA20"))

        st.plotly_chart(fig, use_container_width=True)

        rsi_series = rsi(df)
        st.subheader("RSI Indicator")
        st.line_chart(rsi_series)

        st.subheader("Latest Data")
        st.dataframe(df.tail(10))

    except Exception as e:
        st.error(f"Error: {e}")
