import requests
from bs4 import BeautifulSoup
import os
import yfinance as yf
import pandas as pd

url = 'https://cn.tradingview.com/markets/stocks-usa/sectorandindustry-sector/technology-services/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 查找特定class的元素
elements = soup.find_all('a', class_='apply-common-tooltip tickerNameBox-GrtoTeat tickerName-GrtoTeat')

#numbers = [element.text for element in elements]

numbers = [
    "AMRS",  # Amyris, Inc.
    "CLF",   # Cleveland-Cliffs Inc.
    "SNDL",  # Sundial Growers Inc.
    "ZOM",   # Zomedica Corp.
    "NOK",   # Nokia Corporation
    "PLUG",  # Plug Power Inc.
    "GME"    # GameStop Corp.
]

# Print the list to verify

save_directory = r"F:/HC/Semester 5/DB/data/US/anomaly"
os.makedirs(save_directory, exist_ok=True)
sector_name = os.path.basename(save_directory)

for stock in numbers:
    ticker = yf.Ticker(stock)
    try:
        hist = ticker.history(period="5y")
        if hist.shape[0] <= 1:  # Check if the DataFrame has more than one row
            print(f"Skipping {stock} due to insufficient historical data.")
            continue
        # 添加 'Stock_name' 列并设置为股票名称
        hist['Stock_name'] = stock
        hist['sector'] = sector_name
        
        # 将 'Stock_name' 列移动到第二列
        cols = hist.columns.tolist()
        cols.insert(0, cols.pop(cols.index('Stock_name')))
        hist = hist[cols]
        
        file_name = os.path.join(save_directory, f"{stock}_history.csv")
        hist.to_csv(file_name, index=True)  # 确保索引被保存为一列
        print(f"{stock} 的历史数据已保存为 {file_name}")
    except Exception as e:
        print(f"Skipping {stock} due to error: {e}")

print("所有文件已处理完毕。")
