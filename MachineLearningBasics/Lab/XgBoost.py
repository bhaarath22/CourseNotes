import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creating a XGBoost DMatrix (optimized for XGBoost)
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

#  parameters
params = {
    'objective': 'multi:softmax',  # Multi-class classification
    'num_class': 3,               # Number of classes
    'eta': 0.3,                   # Learning rate
    'max_depth': 6,               # Maximum depth of trees
    'eval_metric': 'mlogloss'     # Logarithmic loss for multi-class
}

bst = xgb.train(params, dtrain, num_boost_round=100)

y_pred = bst.predict(dtest)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
