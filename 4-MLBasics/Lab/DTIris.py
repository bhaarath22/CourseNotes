
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier , export_text , plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
# Notes
# scikit-learn(sklearn) - open source ML libray in python.
# provides simple and efficient tool for data mining and data analysis
# built on top of Numpy , Scipy and matplotlib

'''SL: Classification-> SVM, Random Forest, Decision Trees, k-NN,etc
 Regression->Linear Regression, Ridge, Lasso, SVR ,etc
 UNSL: Clustering: K-Means, DBSCAN, Hierarchical clustering
 Dimensionality Reduction: PCA, t-SNE  '''

# Metrics like accuracy, precision, recall, F1-score
# Cross-validation , GridSearchCV & RandomizedSearchCV (Hyperparameter tuning)

iris = load_iris()
x,y = iris.data , iris.target

xTrain,xTest,yTrain,yTest = train_test_split(x,y,test_size=0.2,random_state=50)
# controls random ness in the dataset
clf = DecisionTreeClassifier(criterion='gini',max_depth=3,random_state=52)
# ( measure the quality of a split) gini impurity or we can use 'entropy'- uses information gain
clf.fit(xTrain,yTrain) # training

prediction = clf.predict(xTest)

accuracy = accuracy_score(yTest,prediction)

print(f'Accuracy:{accuracy:.2f}')

# visualization of the decision tree
plt.figure(figsize=(10,6))  # W,H
plot_tree(clf,filled=True,feature_names=iris.feature_names,class_names=iris.target_names)

# Colors the nodes based on class labels,to distinguish.
# Labels the tree branches with feature names
# tree leaf nodes with class names
plt.show()
print(export_text(clf,feature_name=iris.feature_names))
# decision tree structure into a readable text representation.






