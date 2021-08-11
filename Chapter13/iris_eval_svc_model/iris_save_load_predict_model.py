#iris_save_load_predict_model.py
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle

data_file = "iris.data"
iris_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = read_csv(data_file, names=iris_names)

X = df.drop('class', axis =1)
y = df['class']
x_train, x_test, y_train, y_test \
	= train_test_split(X, y, test_size=0.20,
					   random_state=1, shuffle=True)

model = SVC(gamma='auto')
model.fit(x_train, y_train)

with open("model.pkl", 'wb') as file:
	pickle.dump(model, file)

with open("model.pkl", 'rb') as file:
	loaded_model = pickle.load(file)
	x_new = [[5.6, 2.5, 3.9, 1.1]]
	y_new = loaded_model.predict(x_new)
	print("X=%s, Predicted=%s" % (x_new[0], y_new[0]))
