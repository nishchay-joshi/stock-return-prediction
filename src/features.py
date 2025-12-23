import os
import pandas as pd

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
processed_dir = os.path.join(project_root, "data", "processed")
os.makedirs(processed_dir, exist_ok=True)

def processedData(stock):
    df = pd.read_csv(f"../data/raw/{stock}_ohlcv.csv")

    df["ret_1"] = df["Close"].pct_change(1)
    df["ret_5"] = df["Close"].pct_change(5)
    df["ret_10"] = df["Close"].pct_change(10)

    df["vol_5"] = df["ret_1"].rolling(window=5).std()
    df["vol_20"] = df["ret_1"].rolling(window=20).std()

    df["vol_ratio"] = df["Volume"] / df["Volume"].rolling(window=5).mean()
    df["vol_change"] = df["Volume"].pct_change(1)

    df["target"] = df["ret_1"].shift(-1)

    feature_cols = [
        "ret_1", "ret_5", "ret_10",
        "vol_5", "vol_20",
        "vol_ratio", "vol_change"
    ]

    final_df = df[feature_cols + ["target"]].dropna()

    final_df.to_csv(f"../data/processed/{stock}_features.csv", index= False)






