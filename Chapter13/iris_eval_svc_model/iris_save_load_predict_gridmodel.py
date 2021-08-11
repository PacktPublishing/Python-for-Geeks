#iris_save_load_predict_gridmodel.py

import joblib
from pandas import read_csv
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split, GridSearchCV,RandomizedSearchCV

from sklearn.datasets import load_iris
from sklearn.svm import SVC

data_file = "iris.data"
iris_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = read_csv(data_file, names=iris_names)

X = df.drop('class', axis =1)
y = df['class']
x_train, x_test, y_train, y_test \
	= train_test_split(X, y, test_size=0.20,
					   random_state=1, shuffle=True)

params = {"C":[0.001, 0.01, 1, 5, 10, 100],
              "gamma": [0.001, 0.01, 0.1, 1, 10, 100]}
model=SVC()
grid_cv=GridSearchCV(model,params,  cv=5)
grid_cv.fit(x_train,y_train)

joblib.dump(grid_cv.best_estimator_, "model.joblib")
loaded_model = joblib.load("model.joblib")
x_new = [[5.6, 2.5, 3.9, 1.1]]
y_new = loaded_model.predict(x_new)
print("X=%s, Predicted=%s" % (x_new[0], y_new[0]))