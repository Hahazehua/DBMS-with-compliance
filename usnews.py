import yfinance as yf
from newsapi import NewsApiClient
import csv
import requests
from bs4 import BeautifulSoup
import os

# 初始化 NewsApiClient
newsapi = NewsApiClient(api_key='922a4323e84c446687e629134463b7dc')

# 爬取页面获取股票名称
url = 'https://cn.tradingview.com/markets/stocks-usa/market-movers-all-stocks/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 查找特定class的元素
elements = soup.find_all('a', class_='apply-common-tooltip tickerNameBox-GrtoTeat tickerName-GrtoTeat')
stock_names = [element.text for element in elements]

# 创建保存目录
save_directory = r"F:/HC/Semester 5/DB/data/US"
os.makedirs(save_directory, exist_ok=True)

# 保存日期、标题和URL到CSV文件
with open(os.path.join(save_directory, 'us_news.csv'), mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Stock', 'Date', 'Title', 'URL'])
    
    for stock in stock_names:
        # 获取相关新闻
        news = newsapi.get_everything(q=stock, language='en', sort_by='relevancy')
        
        for article in news['articles']:
            date = article['publishedAt']
            title = article['title']
            url = article['url']
            company = stock
            writer.writerow([stock, date, title, url])

print("News data has been saved to us_news.csv file.")
