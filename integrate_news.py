import pandas as pd
import os

data_frames = []
folder_path = r'F:/HC/Semester 5/DB/data/news'
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# 读取文件us_news作为column的参考
reference_file = 'F:/HC/Semester 5/DB/data/news/1.csv'
reference_df = pd.read_csv(reference_file)
columns = reference_df.columns  

for file in csv_files:
    file_path = os.path.join(folder_path, file)  # 确保这里传递的是字符串
    df = pd.read_csv(file_path)
    
    # 检查是否有 'stock' 列，如果没有则添加并填充 'government'
    if 'Stock' not in df.columns:
        df['Stock'] = 'market'
    
    df = df.reindex(columns=columns)  # 保持列名一致
    data_frames.append(df)

combined_df = pd.concat(data_frames, ignore_index=True)

# 确保输出文件路径包含文件名
output_file = os.path.join(r'F:/HC/Semester 5/DB/data/news', 'combined_news.csv')
combined_df.to_csv(output_file, index=False, encoding='utf-8-sig')

print(f"合并后的 DataFrame 已保存到 {output_file}")
