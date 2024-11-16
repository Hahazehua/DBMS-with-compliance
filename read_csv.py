import pandas as pd

# 指定CSV文件路径
file_path = r'F:\HC\Semester 5\DB\data\HK\hsi_history.csv'

# 读取CSV文件
df = pd.read_csv(file_path)

# 打印数据框内容
print(df)
