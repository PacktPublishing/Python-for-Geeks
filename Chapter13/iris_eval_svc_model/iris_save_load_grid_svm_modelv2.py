import pickle

from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split, GridSearchCV,RandomizedSearchCV

from sklearn.datasets import load_iris
from sklearn.svm import SVC

iris= load_iris()

X = iris.data
y = iris.target
x_train, x_test, y_train, y_test=train_test_split(X,y,test_size=0.2)

#the numpy. logspace() function returns number spaces evenly w.r.t interval on a log scale
params = {"C":[0.001, 0.01, 1, 5, 10, 100],
              "gamma": [0.001, 0.01, 0.1, 1, 10, 100]}
model=SVC()
grid_cv=GridSearchCV(model,params,  cv=5)
grid_cv.fit(x_train,y_train)

with open("svm_grid.pkl", 'wb') as file:
	pickle.dump(grid_cv, file)

with open("svm_grid.pkl", 'rb') as file:
	loaded_grid_cv = pickle.load(file)

print(f"GridSearch- best parameter: {loaded_grid_cv.best_params_}")
print(f"GridSearch- accuracy: {loaded_grid_cv.best_score_}")


with open("svm_grid_best.pkl", 'wb') as file:
	pickle.dump(grid_cv.best_estimator_, file)

with open("svm_grid_best.pkl", 'rb') as file:
		loaded_model = pickle.load(file)
		predictions = loaded_model.predict(x_test)

		# Evaluate predictions
		print(accuracy_score(y_test, predictions))
		print(classification_report(y_test, predictions))