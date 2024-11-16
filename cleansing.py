import os
import pandas as pd

# 指定文件夹路径
folder_path = r'F:\HC\Semester 5\DB\data\HK\try3'
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
data_frames = []
first_file = r'F:\HC\Semester 5\DB\data\HK\try3\0285.HK_history.csv'
first_df = pd.read_csv(first_file)
columns = first_df.columns  
os.makedirs(folder_path, exist_ok=True)



for file in csv_files:
    file_path = os.path.join(folder_path, file)  
    df = pd.read_csv(file_path)
    df.columns = columns  
    data_frames.append(df)
combined_df = pd.concat(data_frames, ignore_index=True)
combined_df['sector'] = 'Tech'

# 保存到新的 CSV 文件
output_file = os.path.join(folder_path, 'combined_with_sector.csv')
combined_df.to_csv(output_file, index=False)

print(f"Data saved to {output_file}")
