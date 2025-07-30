import pandas as pd
import string
import nltk
import re
#  regular expressions. This module provides powerful tools
# for searching, matching, and manipulating strings using regular expressions.

from nltk.corpus import stopwords
#A corpus is a large collection of text used for language analysis,
# machine learning, and natural language processing (NLP)

from nltk.stem import WordNetLemmatizer

# lemmatization, which reduces words to their base or root form
# while ensuring they remain valid words.

from sklearn.feature_extraction.text import TfidfVectorizer
# is used to convert text data into numerical features using TF-IDF (Term Frequency-Inverse Document Frequency).

from sklearn.model_selection import GridSearchCV
# a powerful tool for hyperparameter tuning in machine learning models.
# It helps find the best combination of hyperparameters by performing
# exhaustive search over a predefined parameter grid using cross-validation.

from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
#used to convert categorical labels  into numerical values.

from sklearn.metrics import accuracy_score ,classification_report,confusion_matrix,ConfusionMatrixDisplay
#classification_report – Provides precision, recall, F1-score, and support for each class.

# nltk.download('stopwords')
# nltk.download('wordnet')#WordNet is a large lexical database of the English language
stopwords = set(stopwords.words('english'))
lemmatizer =  WordNetLemmatizer()

trainP='/Users/bharathgoud/PycharmProjects/machineLearing/MachineLearningBasics/DS/SA/train.csv'
testP='/Users/bharathgoud/PycharmProjects/machineLearing/MachineLearningBasics/DS/SA/test.csv'


DSTrain = pd.read_csv(trainP,encoding='latin1')
DSTest = pd.read_csv(testP,encoding='latin1')

# print(DSTrain.head())
# print(DSTrain.info())
# print(DSTest.head())
# print(DSTest.info())

# Data preprocessing
def cleantext(text):
    text = text.lower()
    text= re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE) # removes urls
    text = re.sub(r'\@\w+|\#', '', text)  # Removes mentions and hashtags
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    # Applies the translation table to remove punctuation from the text.
    text = ''.join([i for i in text if not i.isdigit()])  # Removes numbers
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split() if word not in stopwords])
    return text

#applying text cleaning to the DS
DSTrain['text'] = DSTrain['text'].astype(str)  # Convert all values to string
DSTest['text'] = DSTest['text'].astype(str)

DSTrain['text']=DSTrain['text'].apply(cleantext)
DSTest['text']=DSTest['text'].apply(cleantext)

le = LabelEncoder()

DSTrain['sentiment']=le.fit_transform(DSTrain['sentiment'])
DSTest['sentiment']=le.fit_transform(DSTest['sentiment'])
#used to convert categorical labels  into numerical values.

vectorizer = TfidfVectorizer(max_features=4000)# Measures how frequently a term appears in a document.
Xtrain=vectorizer.fit_transform(DSTrain['text'])
Xtest = vectorizer.fit_transform(DSTest['text'])
Ytrain = DSTrain['sentiment']
Ytest = DSTest['sentiment']

paramGrid = {
    'C': [0.1, 1, 10],  # Regularization parameter
    'kernel': ['linear', 'rbf'],
    'gamma': [0.001, 0.01, 0.1, 1]
}
# gridsearch = GridSearchCV(SVC(), paramGrid, cv=5, scoring='accuracy', verbose=1)
# gridsearch.fit(Xtrain,Ytrain)
#Grid Search is a hyperparameter tuning technique used in machine learning to find the best combination
# of parameters for a given model.Trains multiple SVM models with different hyperparameter combinations.
# finds best combination based on accuracy

# Best Model
# svm_classifier = gridsearch.best_estimator_
# svm_classifier.fit(Xtrain,Ytrain)
svm_classifier = SVC(C=1, kernel='linear')  # Use a simple model first
svm_classifier.fit(Xtrain, Ytrain)

prediction = svm_classifier.predict(Xtest)
print(f'Accuracy: {accuracy_score(Ytest, prediction):.2f}')
print(classification_report(Ytest, prediction, target_names=le.classes_))

# Confusion Matrix
cm = confusion_matrix(Ytest, prediction)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=le.classes_)
disp.plot()





