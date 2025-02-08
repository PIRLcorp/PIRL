# pirl/fnb.py

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

class FnbAnalysis:
    def __init__(self):
        # Initialize a regression model for predicting ingredient effects
        self.model = LinearRegression()

    def predict_ingredient_effect(self, dataset_path):
        """
        Predict the impact of ingredient combinations on product outcomes.
        :param dataset_path: Path to the CSV containing F&B data
        :return: The model's predictions and error metrics
        """
        data = pd.read_csv(dataset_path)
        X = data.drop(columns='outcome')
        y = data['outcome']
        
        # Split data into training and testing
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Fit the model
        self.model.fit(X_train, y_train) 
        
        # Predict and evaluate
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        return mse, y_pred
