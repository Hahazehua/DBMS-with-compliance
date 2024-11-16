import pandas as pd
import os

data_frames = []
folder_path = r'F:\HC\Semester 5\DB\data\US\anomaly'
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# 动态选择第一个CSV文件
first_file = os.path.join(folder_path, csv_files[0])
first_df = pd.read_csv(first_file)
columns = first_df.columns  

for file in csv_files:
    file_path = os.path.join(folder_path, file)  # 确保这里传递的是字符串
    df = pd.read_csv(file_path)
    df.columns = columns  # 保持列名一致
    data_frames.append(df)

combined_df = pd.concat(data_frames, ignore_index=True)

# 确保输出文件路径包含文件名
output_file = os.path.join(r'F:\HC\Semester 5\DB\data\US', 'combined_st_stock.csv')
combined_df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"合并后的 DataFrame 已保存到 {output_file}")
