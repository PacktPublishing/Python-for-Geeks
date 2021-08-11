#iris_data_analysis.py
from pandas import read_csv
from matplotlib import pyplot
from pandas.plotting import scatter_matrix

data_file = "iris/iris.data"
iris_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
df = read_csv(data_file, names=iris_names)

print(df.shape)
print(df.head(20))
print(df.describe())
print(df.groupby('class').size())

# box and whisker plots
df.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

# check the histograms
df.hist()
pyplot.show()

# scatter plot matrix
scatter_matrix(df)
pyplot.show()