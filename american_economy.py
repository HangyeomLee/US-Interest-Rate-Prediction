# -*- coding: utf-8 -*-
"""American_Economy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yUMtJVRKzSgq5imGvwLOFL0QMvcWTJux
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np
from sklearn.svm import SVR
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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pca = PCA(n_components=4)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

svr = SVR(kernel='rbf', C=10, epsilon=1)
svr.fit(X_train, y_train)

# params = {'kernel': ['linear', 'rbf'],
#           'C': [0.1, 1, 10],
#           'epsilon': [0.01, 0.1, 1]}

# svr = SVR()
# grid_search = GridSearchCV(svr, params, cv=5, scoring='neg_mean_squared_error')
# grid_search.fit(X_train, y_train)

# best_svr = grid_search.best_estimator_
# best_params = grid_search.best_params_

y_pred = svr.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

#print("최적의 하이퍼파라미터:", best_params)
print("테스트 데이터의 평균 제곱 오차:", mse)

print('Mean Squared Error:', mse)
r_squared = r2_score(y_test, y_pred)
r_squared_percentage = r_squared * 100
print(f"R-squared: {r_squared:.3f}")
print(f"Accuracy: {r_squared_percentage:.2f}%")

Real_GDP = 1.1
Unemployment_Rate = 3.4
Index = 234
Inflation = 0.39

input_data = np.array([Real_GDP, Unemployment_Rate, Index, Inflation]).reshape(1, -1) 
predicted_interest_rate = svr.predict(input_data)

print(f'Predicted interest rate :', predicted_interest_rate[0])