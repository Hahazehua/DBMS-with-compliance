import pandas as pd
import os

data_frames = []
folder_path = r'F:\HC\Semester 5\DB\data\HK\sector'
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

first_file = r'F:\HC\Semester 5\DB\data\HK\sector\finance.csv'
first_df = pd.read_csv(first_file)
columns = first_df.columns  

for file in csv_files:
    file_path = os.path.join(folder_path, file)  
    df = pd.read_csv(file_path)
    df.columns = columns  
    data_frames.append(df)
combined_df = pd.concat(data_frames, ignore_index=True)
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