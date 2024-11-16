import akshare as ak
import pandas as pd

# 获取上证指数的历史数据
index_zh_a_hist_df = ak.stock_zh_index_daily(symbol="sh000001")

# 过滤出最近五年的数据
index_zh_a_hist_df['date'] = pd.to_datetime(index_zh_a_hist_df['date'])
five_years_ago = pd.Timestamp.now() - pd.DateOffset(years=5)
recent_five_years_data = index_zh_a_hist_df[index_zh_a_hist_df['date'] >= five_years_ago]

# 保存数据到 CSV 文件
recent_five_years_data.to_csv("shanghai_composite_5years.csv", index=False)

print("数据已保存到 shanghai_composite_5years.csv")
