import pandas as pd
import os

data_frames = []
folder_path = r'F:\HC\Semester 5\DB\data\US'

first_file = r'F:\HC\Semester 5\DB\data\US\Us_stockdata.csv'
first_df = pd.read_csv(first_file)
columns = first_df.columns  
combined_df = pd.read_csv(first_file)
sector_column = combined_df['sector']
combined_df['Date'] = pd.to_datetime(combined_df['Date'])
columns_to_weight = ['Open', 'High', 'Low', 'Close']
weighted_avg_df = combined_df.groupby(['sector', 'Date']).apply(
    lambda x: (x[columns_to_weight].multiply(x['Volume'], axis=0)).sum() / x['Volume'].sum()
).reset_index()

# 添加 Volume 列
weighted_avg_df['Volume'] = combined_df.groupby(['sector', 'Date'])['Volume'].sum().values

# 保存到新的 CSV 文件
weighted_avg_df.to_csv('weighted_avg_file.csv', index=False)

# 排除非数值列
numeric_columns = combined_df.select_dtypes(include='number').columns
combined_df = combined_df.groupby(['sector', 'Date'])[numeric_columns].mean().reset_index()
combined_df.to_csv('sertor_datahk.csv', index=False)

print(combined_df)