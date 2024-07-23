import pandas as pd 

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    # Drop the id column: 
    data = data.drop('id', axis=1)
    
    # Fill missing values in the bmi column: 
    data['bmi'] = data['bmi'].fillna(data['bmi'].mean())

    return data