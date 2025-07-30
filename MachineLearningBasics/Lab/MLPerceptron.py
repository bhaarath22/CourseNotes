import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("/Users/bharathgoud/PycharmProjects/machineLearing/MachineLearningBasics/DS/diabetes.csv")  # Ensure correct file path
X = df.drop(columns=['Outcome'])  # Features
y = df['Outcome']  # Target (0 = No Diabetes, 1 = Diabetes)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize feature values (important for neural networks)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialization  and training of the Multi-Layer Perceptron model with 3 hidden layers
mlp = MLPClassifier(hidden_layer_sizes=(128, 64, 32),  # Three hidden layers: 128 → 64 → 32 neurons
                    activation='relu',
                    solver='adam',
                    max_iter=500,
                    random_state=42)

mlp.fit(X_train, y_train)

pred = mlp.predict(X_test)

accuracy = accuracy_score(y_test, pred)
print(f"Model Accuracy: {accuracy:.4f}")
print("\nClassification Report:\n", classification_report(y_test, pred))
