import numpy as np
from sklearn.cluster import KMeans

from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score


'''
# Topaz Aakal -> 318644549
# Marat Zinger -> 332689405
# Afik Danan -> 208900175
'''



class Kmeans:
    """A class for K-MEANS algorithm in the library sklearn"""

    def __init__(self, x_train, x_test, y_train, y_test):
        self.x_train = x_train
        self.x_test = x_test
        self.y_train = y_train
        self.y_test = y_test

    def model(self, num_clusters):
        """function that builds the model and activates it"""
        model = KMeans(n_clusters=num_clusters,
                       max_iter=400)  # create the knn object with the requested number of clusters
        model.fit(self.x_train, self.y_train)  # fitting the object to the training set

        # get evaluation
        pred = model.predict(self.x_test)  # predict the response for test dataset

        # calculation of evaluation indices on test data
        accuracy = accuracy_score(self.y_test, pred)
        precision = precision_score(self.y_test, pred, average='weighted', zero_division=True)
        recall = recall_score(self.y_test, pred, average='weighted', labels=np.unique(pred), zero_division=True)
        f1Score = f1_score(self.y_test, pred, average='weighted')
        cm = confusion_matrix(self.y_test, pred)

        R = self.y_test.value_counts().argmax()
        maj = (self.y_test.values == R).sum()
        majority = (maj / len(self.y_test)) * 100

        # calculation of evaluation indices on train data
        pred_train = model.predict(self.x_train)
        cm_train = confusion_matrix(self.y_train, pred_train)

        return {'accuracy': accuracy * 100, 'precision': precision * 100, 'recall': recall * 100,
                'f1Score': f1Score * 100,
                'confusion_matrix': cm, 'confusion_matrix_train': cm_train, "model": model, "majority": majority}
