#iris_build_svm_model.py
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

data_file = "iris/iris.data"
iris_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = read_csv(data_file, names=iris_names)

X = df.drop('class', axis =1)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y,
				test_size=0.20, random_state=1, shuffle=True)

# Make predictions
model = SVC(gamma='auto')
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print(accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))

