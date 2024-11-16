import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import yfinance as yf
import akshare as ak

url = 'https://cn.tradingview.com/markets/stocks-china/sectorandindustry-sector/technology-services/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


elements = soup.find_all('a', class_='apply-common-tooltip tickerNameBox-GrtoTeat tickerName-GrtoTeat')
save_directory = r"F:/HC/Semester 5/DB/data/US/billy"
sector_name=os.path.basename(save_directory)
numbers = [element.text for element in elements]


os.makedirs(save_directory, exist_ok=True)
for stock in numbers:
    try:
        stock_data = ak.stock_zh_a_hist(symbol=stock, period="daily", start_date="20190925", end_date="20240925")
        file_name = f"{save_directory}/{stock}.csv"
        stock_data.to_csv(file_name, index=False)
        print(f"{stock} 的历史数据已保存为 {file_name}")

        df = pd.read_csv(file_name)
        
    
        df = df[['日期', '开盘', '最高', '最低', '收盘', '成交量']]
        df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']


        df['Dividends'] = 0
        df['Stock Splits'] = 0


        df.loc[1:1169, ['Dividends', 'Stock Splits']] = 0
        df['Stock_code'] = os.path.splitext(os.path.basename(file_name))[0]
        cols = df.columns.tolist()
        cols.insert(1, cols.pop(cols.index('Stock_code')))
        df = df[cols]
        df['sector'] = sector_name
        
        
        df.to_csv(file_name, index=False)
    except Exception as e:
        print(f"获取 {stock} 的数据时出错: {e}，跳过该股票代码。")

print("所有文件已处理完毕。")
