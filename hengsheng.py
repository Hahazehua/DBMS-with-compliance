import yfinance as yf
import pandas as pd

# 设置恒生指数的代码
ticker = "^HSI"

# 获取恒生指数的历史数据
hsi_data = yf.download(ticker, start="2019-09-25", end="2024-09-25")

# 保存数据到CSV文件
file_name = "hsi_history.csv"
hsi_data.to_csv(file_name)

# 显示前几行数据
print(hsi_data.head())
