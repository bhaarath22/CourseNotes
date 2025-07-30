import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

Dataset = pd.read_csv('/MachineLearningBasics/Lab/DS/spam_ham_dataset.csv')
# print(Dataset.head())
# feature selection. text as feature & label_num as target variable
x= Dataset['text']
y= Dataset['label_num'] # Ham(0) or Spam(1)
xTrain,xTest,yTrain,yTest= train_test_split(x,y, test_size=0.2,random_state=50)

# converts test data to numerical format using countvectorizer
# method for converting text into a bag-of-words (BoW) representation.
vectorizer = CountVectorizer()
# tokenizes the text and creates a vocabulary of unique words.
XtrainVector = vectorizer.fit_transform(xTrain)
# Learns the vocabulary from X_train ( extracts all unique words)
#transform: Converts X_train into a sparse matrix where each row represents a document
# and each column represents a word count.
XtestVector = vectorizer.transform(xTest)

clf = MultinomialNB()
clf.fit(XtrainVector,yTrain)

Prediction = clf.predict(XtestVector)

accuracy = accuracy_score(yTest,Prediction)
print(f'Accuracy:{accuracy:.2f}')

sampleEmail =['Congratulations! You won a free trip. Click here to claim']
SEvec = vectorizer.transform(sampleEmail)
prediction = clf.predict(SEvec)
print(f'Predicted Class (1 = Spam, 0 = Not Spam): {prediction[0]}')





