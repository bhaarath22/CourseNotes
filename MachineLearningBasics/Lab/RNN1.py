import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Embedding

# Loading the IMDB dataset
max_features = 10000
maxlen = 100
batch_size = 32

# Load data
(input_train, y_train), (input_test, y_test) = imdb.load_data(num_words=max_features)
input_train = sequence.pad_sequences(input_train, maxlen=maxlen)
input_test = sequence.pad_sequences(input_test, maxlen=maxlen)

#  model Building
model = Sequential()
model.add(Embedding(max_features, 32, input_length=maxlen))
model.add(SimpleRNN(32,input_shape=(100,1), return_sequences=False))
model.add(Dense(1, activation='sigmoid'))

model.summary()

# Compileing the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

#  model training
history = model.fit(input_train, y_train, epochs=10, batch_size=batch_size, validation_split=0.2)
model.summary()
#  model evaluation
test_loss, test_acc = model.evaluate(input_test, y_test)
print(f"Test Accuracy: {test_acc}")
