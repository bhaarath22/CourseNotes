import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding

# Load the IMDB dataset
max_features = 10000  # Top 10k most frequent words
maxlen = 100          # Each review will be truncated/padded to 100 words
batch_size = 32

# Load data
(input_train, y_train), (input_test, y_test) = imdb.load_data(num_words=max_features)
input_train = sequence.pad_sequences(input_train, maxlen=maxlen)
input_test = sequence.pad_sequences(input_test, maxlen=maxlen)

# Build the LSTM model
model = Sequential()
model.add(Embedding(max_features, 32, input_length=maxlen))  # Embedding turns word indices into dense vectors
model.add(LSTM(32))  # LSTM layer with 32 units
model.add(Dense(1, activation='sigmoid'))  # Output layer for binary classification

model.summary()

#  compileing the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

#  model training
history = model.fit(input_train, y_train, epochs=10, batch_size=batch_size, validation_split=0.2)
model.summary()
#  model Evaluation
test_loss, test_acc = model.evaluate(input_test, y_test)
print(f"Test Accuracy: {test_acc:.4f}")
