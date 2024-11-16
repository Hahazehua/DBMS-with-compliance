import os
import pandas as pd
import mysql.connector


db_config = {
    'user': 'Athena',
    'password': '302311Forever',  
    'host': '127.0.0.1',
    'database': 'Athenadb'
}


conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()


folder_path = '/home/p2211029@ipm.edu.mo/output'


csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]


def import_csv_to_db(file_path):
    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        
        sql = "INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)"
        cursor.execute(sql, tuple(row))
    conn.commit()


for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    import_csv_to_db(file_path)


cursor.close()
conn.close()

print("所有 CSV 文件已成功导入数据库")
