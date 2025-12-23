from src.features import processedData
from src.stock_names import stocks

for stock in stocks:
    processedData(stock.replace(".NS", ""))
