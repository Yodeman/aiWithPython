# Predicting traffic using Extremely Random Forest regressor.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, mean_absolute_error
from sklearn import model_selection, preprocessing
from sklearn.ensemble import ExtraTreesRegressor

input_file = "traffic_data.txt"
data = []
with open(input_file) as f:
    for line in f.readlines():
        items = line[:-1].split(',')
        data.append(items)
data = np.array(data)
print(data[:3])

# Convert string data to numerical data
label_encoder = []
X_encoded = np.empty(data.shape)
for i,item in enumerate(data[0]):
    if item.isdigit():
        X_encoded[:, i] = data[:, i]
    else:
        label_encoder.append(preprocessing.LabelEncoder())
        X_encoded[:, i] = label_encoder[-1].fit_transform(data[:, i])
print(X_encoded[:3])
X = X_encoded[:, :-1].astype(int)
y = X_encoded[:, -1].astype(int)

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, 
                                    test_size=0.25, random_state=5)

# Extremely Random Forests regressor
params = {'n_estimators':100, 'max_depth':4, 'random_state':0}
regressor = ExtraTreesRegressor(**params)
regressor.fit(X_train, y_train)

# Compute the regressor performane on test data
y_pred = regressor.predict(X_test)
print("Mean absolute error:", round(mean_absolute_error(y_test, y_pred), 2))

