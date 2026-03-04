import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

class StockPredictor:
    def __init__(self, stock_data):
        self.data = stock_data
        self.model = None

    def prepare_data(self, time_steps=1):
        # Prepare the data for LSTM
        X, y = [], []
        for i in range(len(self.data) - time_steps):
            X.append(self.data[i:(i + time_steps), 0])
            y.append(self.data[i + time_steps, 0])
        return np.array(X), np.array(y)

    def train_lstm(self, time_steps=1):
        X, y = self.prepare_data(time_steps)
        X = X.reshape((X.shape[0], X.shape[1], 1))
        self.model = Sequential()
        self.model.add(LSTM(50, return_sequences=True, input_shape=(X.shape[1], 1)))
        self.model.add(Dropout(0.2))
        self.model.add(LSTM(50, return_sequences=False))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(1))
        self.model.compile(optimizer='adam', loss='mean_squared_error')
        self.model.fit(X, y, epochs=100, batch_size=32)

    def train_random_forest(self):
        # Prepare data for Random Forest
        X = self.data.drop(columns=['target'])  # Adjust this as necessary
        y = self.data['target']  # Adjust this as necessary
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
        self.model = RandomForestRegressor()
        self.model.fit(X_train, y_train)

    def predict_lstm(self, input_data):
        input_data = input_data.reshape((input_data.shape[0], input_data.shape[1], 1))
        return self.model.predict(input_data)

    def predict_random_forest(self, input_data):
        return self.model.predict(input_data)