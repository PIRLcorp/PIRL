
# pirl/nutraceuticals.py

import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

class NutraceuticalsDevelopment:
    def __init__(self):
        # Initialize GradientBoostingRegressor
        self.model = GradientBoostingRegressor(n_estimators=100, random_state=42)

    def develop_nutraceuticals(self, dataset_path):
        """
        Develop new nutraceutical ingredients based on dataset analysis.
        :param dataset_path: Path to nutraceuticals dataset
        :return: R-squared score and predictions
        """
        data = pd.read_csv(dataset_path)
        X = data.drop(columns='efficacy')
        y = data['efficacy']
        
        # Split into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Fit the model
        self.model.fit(X_train, y_train)
        
        # Predict and evaluate
        y_pred = self.model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        return r2, y_pred
