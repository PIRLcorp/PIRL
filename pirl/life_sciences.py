# pirl/life_sciences.py

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

class LifeSciencesResearch:
    def __init__(self):
        # Initialize with a PCA model for dimensionality reduction
        self.pca = PCA(n_components=2)

    def analyze_gene_expression(self, dataset_path):
        """
        Analyze gene expression data to identify key biological markers.
        :param dataset_path: Path to gene expression data (CSV)
        :return: PCA transformed data
        """
        data = pd.read_csv(dataset_path)
        X = data.drop(columns=['gene', 'sample_id'])  # Drop non-numeric columns

        # Standardize the data
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Apply PCA to reduce dimensionality
        pca_results = self.pca.fit_transform(X_scaled)
        return pca_results
