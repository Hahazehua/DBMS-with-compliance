import requests
import json

# 定义 API URL
base_url = "https://data.sec.gov/api/xbrl/companyconcept/CIK0000320193/us-gaap/AccountsPayableCurrent.json"

# 定义要保存的文件名
output_file = 'sec_rulemaking_data.json'

# 初始化一个空列表来存储所有页面的数据
all_data = []

for page_num in range(0, 5):  # 假设你想爬取前5页
    url = f"{base_url}?page={page_num}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Accept': 'application/json'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(data)  # 打印完整的 JSON 响应以查看其结构

        # 将当前页面的数据添加到 all_data 列表中
        all_data.append(data)
    else:
        print(f"Failed to retrieve data: {response.status_code}")

# 将所有数据保存到 JSON 文件中
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(all_data, file, ensure_ascii=False, indent=4)

print(f"数据已保存到 {output_file} 文件中。")
