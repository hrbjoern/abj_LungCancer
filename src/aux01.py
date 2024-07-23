import pandas as pd

def print_data_head(file_path):
    data = pd.read_csv(file_path)
    print(data.head())
    return 