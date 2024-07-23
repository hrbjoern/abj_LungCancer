import pandas as pd

def train_model(data: pd.DataFrame) -> None:
    # Split the data into features and target: 
    X = data.drop('stroke', axis=1)
    y = data['stroke']
    
    # Split the data into training and testing sets: 
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a logistic regression model: 
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    return model