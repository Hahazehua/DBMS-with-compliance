from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url = "https://www.hkex.com.hk/News/News-Release?sc_lang=en&DateFrom=2024-01-01&DateTo=2024-12-31&Category=&Category2=undefined"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

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
