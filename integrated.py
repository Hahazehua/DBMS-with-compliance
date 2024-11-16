import pandas as pd
import os

data_frames = []
main_folder_path = r'F:\HC\Semester 5\DB\data\US\AM_data'

# 遍历主文件夹中的所有子文件夹
for sub_folder in os.listdir(main_folder_path):
    sub_folder_path = os.path.join(main_folder_path, sub_folder)
    if os.path.isdir(sub_folder_path):
        csv_files = [f for f in os.listdir(sub_folder_path) if f.endswith('.csv')]
        for file in csv_files:
            file_path = os.path.join(sub_folder_path, file)  # 确保这里传递的是子文件夹中的文件路径
            print(f"正在读取文件: {file_path}")  # 打印文件路径
            try:
                df = pd.read_csv(file_path)
                data_frames.append(df)
            except pd.errors.EmptyDataError:
                print(f"文件 {file_path} 是空的，已跳过。")
            except Exception as e:
                print(f"读取文件 {file_path} 时出错: {e}")

# 合并所有 DataFrame
if data_frames:
    combined_df = pd.concat(data_frames, ignore_index=True)
    output_file = os.path.join(r'F:\HC\Semester 5\DB\data\US', 'combined.csv')
    combined_df.to_csv(output_file, index=False)
    print(f"合并后的 DataFrame 已保存到 {output_file}")
else:
    print("没有可合并的 DataFrame。")
