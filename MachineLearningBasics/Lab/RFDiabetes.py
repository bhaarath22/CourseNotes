import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

# Column names
colNames = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']

# Load dataset
pima = pd.read_csv("/Users/bharathgoud/PycharmProjects/machineLearing/MachineLearningBasics/DS/diabetes.csv", header=0, names=colNames)

# Feature columns and target variable
featureCol = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
x = pima[featureCol]  # Features
y = pima['label']     # Target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# Initializing and training the Random Forest Classifier with hyperparameter tuning
rfclf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
rfclf.fit(x_train, y_train)

# Predict and evaluate the model
prediction = rfclf.predict(x_test)

# Print Accuracy and Classification Report
print("Accuracy:", metrics.accuracy_score(y_test, prediction))
print("\nClassification Report:\n", classification_report(y_test, prediction))

# Confusion Matrix
cm = confusion_matrix(y_test, prediction)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["No Diabetes", "Diabetes"])
disp.plot()
