import requests
from bs4 import BeautifulSoup
import os
import yfinance as yf


url = 'https://cn.tradingview.com/markets/stocks-usa/sectorandindustry-sector/technology-services/'


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 查找特定class的元素
elements = soup.find_all('a', class_='apply-common-tooltip tickerNameBox-GrtoTeat tickerName-GrtoTeat')

numbers = [element.text for element in elements]

save_directory = "F:/HC/Semester 5/DB/data/HK/miscellaneous"
os.makedirs(save_directory, exist_ok=True)
for stock in numbers:
    ticker = yf.Ticker(stock)
    hist = ticker.history(period="5y")
    file_name = f"{stock}_history.csv"
    hist.to_csv(file_name)
    print(f"{stock} 的历史数据已保存为 {file_name}")



