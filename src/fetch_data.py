import yfinance as yf
import os
from src.stock_names import stocks

bulk_data = yf.download(
    stocks,
    period="5y",
    auto_adjust=False,
    group_by="ticker",
)

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
processed_dir = os.path.join(project_root, "data", "raw")
os.makedirs(processed_dir, exist_ok=True)

for stock in stocks:
    stock_df = bulk_data[stock]
    ohlcv = stock_df[["Open", "High", "Low", "Close", "Volume"]].dropna()
    clean_name = stock.replace(".NS", "")
    ohlcv.to_csv(f"data/raw/{clean_name}_ohlcv.csv")


