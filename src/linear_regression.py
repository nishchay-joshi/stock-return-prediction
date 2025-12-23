import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(project_root, "data", "combined", "combined_data_stocks.csv")

df = pd.read_csv(file_path)

x = df[["ret_1", "ret_5", "ret_10", "vol_5", "vol_20", "vol_ratio", "vol_change"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)

lm = LinearRegression()
lm.fit(X_train, y_train)
predictions = lm.predict(X_test)

mae = metrics.mean_absolute_error(y_test, predictions)
mse = metrics.mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)



