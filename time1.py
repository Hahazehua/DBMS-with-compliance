from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import csv

# 设置ChromeDriver路径
driver_path = 'path/to/chromedriver'

# 初始化Chrome选项
options = webdriver.ChromeOptions()

# 初始化WebDriver
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# 打开目标网页
url = "https://www.hkex.com.hk/News/News-Release?sc_lang=en&DateFrom=2019-09-01&DateTo=2024-09-01&Category=&Category2=undefined"
driver.get(url)

# 模拟滚动页面以加载新内容
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # 向下滚动页面
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    # 等待页面加载
    time.sleep(SCROLL_PAUSE_TIME)
    
    # 计算新的滚动高度并与上一次的滚动高度进行比较
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# 获取页面内容
html = driver.page_source

# 关闭WebDriver
driver.quit()

# 使用BeautifulSoup解析页面内容
soup = BeautifulSoup(html, 'html.parser')

rows = soup.find_all('div', class_='whats_on_tdy_row')

with open('hkex_news.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Title', 'URL'])  
    
    for row in rows:
        date_div = row.find('div', class_='whats_on_tdy_ball_number')
        date_number = date_div.get_text() if date_div else 'N/A'
        
        date_month_year_div = row.find('div', class_='whats_on_tdy_ball')
        date_month_year = date_month_year_div.find_all('div')[2].get_text() if date_month_year_div else 'N/A'
        
        title_div = row.find('div', class_='whats_on_tdy_text_2')
        title = title_div.get_text() if title_div else 'N/A'
        
        link_tag = title_div.find('a') if title_div else None
        link = link_tag['href'] if link_tag else 'N/A'
        
        full_date = f"{date_number} {date_month_year}"
        
        writer.writerow([full_date, title, link])

print("Data has been saved to hkex_news.csv")
