import requests
import pandas as pd
from config import settings

def get_stock_data(symbol: str, interval: str = "1min") -> pd.DataFrame:
    url = f"{settings.API_BASE}"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": interval,
        "apikey": settings.API_KEY,
        "outputsize": "compact"
    }
    r = requests.get(url, params=params)
    r.raise_for_status()
    data = r.json()

    key = f"Time Series ({interval})"
    if key not in data:
        raise ValueError(f"Invalid response: {data}")

    df = pd.DataFrame(data[key]).T
    df.columns = ["open", "high", "low", "close", "volume"]
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    df.sort_index(inplace=True)
    return df
