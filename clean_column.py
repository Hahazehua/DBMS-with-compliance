import os
import pandas as pd

folder_path = r'F:\HC\Semester 5\DB\data\HK\miscellaneous'
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    if 'Capital Gains' in df.columns:
        df.drop(columns=['Capital Gains'], inplace=True)
        df.to_csv(file_path, index=False)
        print(f"Column 'Capital Gains' has been deleted from {file} and the file has been saved.")
    else:
        print(f"Column 'Capital Gains' not found in {file}.")
