import pandas as pd
from sklearn.metrics import accuracy_score

def test_model(trained_model, data: pd.DataFrame) -> None:
    # Split the data into features and target: 
    X = data.drop('stroke', axis=1)
    y = data['stroke']
    
    # Make predictions: 
    y_pred = trained_model.predict(X)
    
    # Evaluate the model: 
    accuracy = accuracy_score(y, y_pred)
    print(f'Accuracy: {accuracy}')
    
    return