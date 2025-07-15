import ta
import pandas as pd

def analyze(df):
    df["sma_fast"] = ta.trend.sma_indicator(df["c"], window=5)
    df["sma_slow"] = ta.trend.sma_indicator(df["c"], window=20)
    if df["sma_fast"].iloc[-2] < df["sma_slow"].iloc[-2] and df["sma_fast"].iloc[-1] > df["sma_slow"].iloc[-1]:
        return "BUY"
    elif df["sma_fast"].iloc[-2] > df["sma_slow"].iloc[-2] and df["sma_fast"].iloc[-1] < df["sma_slow"].iloc[-1]:
        return "SELL"
    return "HOLD"
