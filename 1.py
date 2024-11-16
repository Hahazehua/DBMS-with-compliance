import os
import pandas as pd

folder_path = r'F:\HC\Semester 5\DB\data\HK\miscellaneous'
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    num_columns = len(df.columns)
    print(f"{file} has {num_columns} columns.")
