from sklearn.datasets import load_iris
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
#K-Fold Cross-Validation is a model evaluation technique that helps in testing
# how well a machine learning model generalizes to unseen data. Instead of using
# a single train-test split, it divides the dataset into multiple folds and trains
# the model multiple times.

data = load_iris()
X, y = data.data, data.target

model = RandomForestClassifier(random_state=42)

# K-Fold Cross Validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Evaluate model
scores = cross_val_score(model, X, y, cv=kf, scoring='accuracy')
print(f"Cross-Validation Scores: {scores}")
print(f"Mean Accuracy: {scores.mean():.4f}")
print(f"Standard Deviation: {scores.std():.4f}")

