import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pandas.io.json import json_normalize
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

above50t = pd.read_pickle("MLdata.pkl")

print("Multinomial Best Parameters")
print("-------------------------------------")
model = Pipeline(steps=[('Tfidf', TfidfVectorizer(min_df=2)), ('MNB', MultinomialNB())])
param_grid = {
    "Tfidf__max_features":[None, 1500, 3000, 5000, 7500],
    "Tfidf__min_df":[1,2,3,4,5],
    "Tfidf__norm":['l1', 'l2', None],
    "Tfidf__ngram_range":[(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)],
    "MNB__alpha":[0.01, 0.25, 0.5, 0.75, 1.00]
}
grid = GridSearchCV(model, param_grid, n_jobs=4, cv=5)
grid.fit(above50t["body"], above50t["subreddit"])
print("Best Parameters :")
print(grid.best_params_)

print("\n")
print("Support Vector Parameters")
print("-------------------------------------")
model = Pipeline(steps=[('Tfidf', TfidfVectorizer(min_df=2)), ('SVC', SVC(C=1E5))])
param_grid = {
    "Tfidf__max_features":[None, 1500, 3000, 5000, 7500],
    "Tfidf__min_df":[1,2,3,4,5],
    "Tfidf__norm":['l1', 'l2', None],
    "Tfidf__ngram_range":[(1,1),(1,2),(1,3),(2,2),(2,3),(3,3)],
    "SVC__kernel":["linear", "poly", "rbf", "sigmoid"],
    "SVC__gamma":['auto','scale']
}
grid = GridSearchCV(model, param_grid, n_jobs=10, cv=5)
grid.fit(above50t["body"], above50t["subreddit"])
print("Best Parameters :")
print(grid.best_params_)