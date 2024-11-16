from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url = "https://www.sse.com.cn/regulation/supervision/dynamic/"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

soup = BeautifulSoup(html, 'html.parser')

rows = soup.find_all('div', class_='whats_on_tdy_row')
items = soup.find_all('dd')

# 打开一个CSV文件来保存数据
with open('cnnews.csv', mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Title', 'URL'])  # 写入表头

    for item in items:
        date_span = item.find('span')
        if date_span:
            date = date_span.get_text(strip=True)
        else:
            date = 'N/A'  # 或者其他默认值

        title = item.find('a').get_text(strip=True)
        url = item.find('a')['href']

        writer.writerow([date, title, url])

print("数据已保存到 cnnews.csv 文件中。")
