import pandas as pd

def moving_average(df: pd.DataFrame, window: int = 20) -> pd.Series:
    return df["close"].rolling(window=window).mean()

def rsi(df: pd.DataFrame, window: int = 14) -> pd.Series:
    delta = df["close"].diff()
    gain = delta.clip(lower=0).rolling(window=window).mean()
    loss = -delta.clip(upper=0).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))
