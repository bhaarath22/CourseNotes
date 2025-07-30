import numpy as np
import pandas as pd
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv("/Users/bharathgoud/PycharmProjects/machineLearing/MachineLearningBasics/DS/diabetes.csv")

X = df.drop(columns=['Outcome'])  # Features
y = df['Outcome']  # Target (Binary Classification)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

scaler = StandardScaler()
# Normalizing  features for better convergence
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Training a Single-Layer Perceptron
slp = Perceptron(max_iter=1000, eta0=0.01, random_state=1)
slp.fit(X_train, y_train)

y_pred = slp.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
