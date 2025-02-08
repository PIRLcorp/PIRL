# pirl/ai_tools.py

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class IngredientDiscovery:
    def __init__(self):
        # Initialize the model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def discover_bioactives(self, dataset_path):
        """
        Discover bioactive compounds based on the dataset.
        :param dataset_path: Path to the CSV file containing the dataset
        :return: Accuracy of the model and predicted values
        """
        data = pd.read_csv(dataset_path)
        X = data.drop(columns='target')
        y = data['target']
        
        # Split dataset into training and test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train the model
        self.model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = self.model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        return accuracy, y_pred 
 
