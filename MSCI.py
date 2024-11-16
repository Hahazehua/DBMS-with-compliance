import yfinance as yf
import pandas as pd
import os

save_directory = r"F:/HC/Semester 5/DB/data/HK"
os.makedirs(save_directory, exist_ok=True)
sector_name = os.path.basename(save_directory)

ticker = "URTH"

msci_data = yf.download(ticker, start="2019-09-25", end="2024-09-25")


file_name = "msci_world_history.csv"
msci_data.to_csv(file_name)


print(msci_data.head())