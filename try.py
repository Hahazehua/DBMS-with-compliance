import requests
from bs4 import BeautifulSoup

url = 'https://q.stock.sohu.com/cn/bk_4842.shtml'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 查找所有 class 为 e1 的元素
elements = soup.find_all('td', class_='e1')

# 提取并打印这些元素的文本内容
for element in elements:
    print(element.get_text(strip=True))
