#iris_eval_svc_model
from pandas import read_csv
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, GridSearchCV,RandomizedSearchCV

from sklearn.datasets import load_iris
from sklearn.svm import SVC

data_file = "iris.data"
iris_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = read_csv(data_file, names=iris_names)

X = df.drop('class', axis =1)
y = df['class']
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=1, shuffle=True)

params = {"C":[0.001, 0.01, 1, 5, 10, 100],
              "gamma": [0.001, 0.01, 0.1, 1, 10, 100]}

model1=SVC()
rand_cv=RandomizedSearchCV(model1,params, n_iter = 5, cv=5)
rand_cv.fit(X_train,y_train)
print(f"RandomizedSearch - best parameter: {rand_cv.best_params_}")
print(f"RandomizedSearch - accuracy: {rand_cv.best_score_}")
print(classification_report(y_test,rand_cv.best_estimator_.predict(X_test)))

model2=SVC()
grid_cv=GridSearchCV(model2,params,  cv=5)
grid_cv.fit(X_train,y_train)
print(f"GridSearch- best parameter: {grid_cv.best_params_}")
print(f"GridSearch- accuracy: {grid_cv.best_score_}")
print(classification_report(y_test,grid_cv.best_estimator_.predict(X_test)))


