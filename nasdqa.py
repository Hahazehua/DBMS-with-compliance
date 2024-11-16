import yfinance as yf
save_directory = r"F:/HC/Semester 5/DB/data/US/billy"
# 下载纳斯达克综合指数的历史数据
nasdaq = yf.Ticker("^IXIC")
hist = nasdaq.history(period="1y")  # 获取过去一年的数据

hist.to_csv("nasdaq_history.csv")

print("数据已保存到 nasdaq_history.csv")