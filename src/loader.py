from datetime import datetime
import pandas as pd
import os

def save_in_csv(df: pd.DataFrame, path: str):
    data_da_coleta = datetime.today().date()
    data_string = data_da_coleta.strftime("%Y-%m-%d")
    
    filename = f"indicadores_{data_string}.csv"
    
    dir_path = os.path.join(path, filename)
    
    df.to_csv(dir_path, index=False)
    return