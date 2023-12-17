# -*- coding: utf-8 -*-
"""Project4:House Price Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KWTNZHtXNvYLkp7iwKNJBLSyistMHgdV
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

house_dataset=pd.read_csv('/content/boston.csv')

house_dataset

"""Data Preprocessing:"""

house_dataset.shape

#check for missing values
house_dataset.isnull().sum()

house_dataset.describe()

x=house_dataset.drop('MEDV',axis=1)
y=house_dataset['MEDV']

print(x)
print(y)

"""Train-Test split

"""

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=2)



print(x.shape, x_train.shape, x_test.shape)

model=XGBRegressor()

model.fit(x_train,y_train)

"""Evalutaion
prediction on training data
"""

# accuracy for prediction on training data
training_data_prediction = model.predict(x_train)

score_1=metrics.r2_score(y_train,training_data_prediction)
print(score_1)

"""Prediction on test data"""

# accuracy for prediction on training data
training_data_prediction = model.predict(x_test)

score_2=metrics.r2_score(y_test,training_data_prediction)
print(score_2)

"""Predictitive system


"""

#input_data=(0.62976,0.00,8.140,0,0.5380,5.9490,61.80,4.7075,4,307.0,21.00,396.90,8.26)
input_data=(0.75026,0.00,8.140,0,0.5380,5.9240,94.10,4.3996,4,307.0,21.00,394.33,16.30)
input_data_numpy=np.asarray(input_data)
input_data_reshape=input_data_numpy.reshape(1,-1)
prediction=model.predict(input_data_reshape)
print("Predicted Price of House is:",prediction)

