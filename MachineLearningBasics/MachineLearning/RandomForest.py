# import numpy as np # linear algebra
# import pandas as pd # data processing
#
# #data visualization
# import seaborn as sns
# from matplotlib import pyplot as plt
# from matplotlib import style
# # Importing algorithms from sklearn
# from sklearn import linear_model
# from sklearn.linear_model import LogisticRegression
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import Perceptron
# from sklearn.linear_model import SGDClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.svm import SVC, LinearSVC
# from sklearn.naive_bayes import GaussianNB
#
# Importing necessary libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Loading the Iris dataset
data = load_iris()
X = data.data  # Features
y = data.target  # Target labels

# Spliting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialization  the Random Forest Classifier
# n_estimators: Number of decision trees
# max_depth: Maximum depth of each tree (None for unlimited depth)
rf_clf = RandomForestClassifier(n_estimators=100, max_depth=None, random_state=42)

# Train the model on the training data
rf_clf.fit(X_train, y_train)

#  predictions on the test data
y_pred = rf_clf.predict(X_test)

# Evaluation the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
