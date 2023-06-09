# -*- coding: utf-8 -*-
"""American_Economy_Deep.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ixs5vE9gwDrl_aHaG_W3WZQVbtZ6HHy4
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.impute import SimpleImputer
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA

data_inf = pd.read_csv('/content/drive/MyDrive/US_data/cpiai.csv')
data_int = pd.read_csv('/content/drive/MyDrive/US_data/US_interest_rate.csv')
data_inf = pd.DataFrame(data_inf)
data_int = pd.DataFrame(data_int)
data_int = data_int.fillna(method='ffill')
data_inf = data_inf.fillna(method='ffill')

data_inf['Date'] = pd.to_datetime(data_inf['Date'])
data_inf['Year'] = data_inf['Date'].dt.year

filtered_data_int = data_int[(data_int['Year'] >= 1954) & (data_int['Year'] <= 2017)]
filtered_data_inf = data_inf[(data_inf['Year'] >= 1954) & (data_inf['Year'] <= 2017)]
filtered_data_int = pd.merge(filtered_data_int, filtered_data_inf, on='Year')
filtered_data_int['Real GDP (Percent Change)'] = filtered_data_int['Real GDP (Percent Change)'].fillna(method='ffill')

print(filtered_data_int)

X = filtered_data_int[['Real GDP (Percent Change)', 'Unemployment Rate','Index','Inflation', ]]
y = filtered_data_int['Effective Federal Funds Rate']

X_train, X_val_test, y_train, y_val_test = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_val_test, y_val_test, test_size=0.5, random_state=42)



# 모델 디자인
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_dim=X_train.shape[1]),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)
])

# 모델 학습 설정
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mse'])

# 모델 학습
model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=200, batch_size=16)

# 모델 평가
model.evaluate(X_test, y_test)

# 모델을 이용해 예측값을 구합니다.
y_pred = model.predict(X_test)

# 결정계수를 계산합니다.
r2 = r2_score(y_test, y_pred)
print("R-squared:", r2)
print("Accuracy : ", r2*100,"%")