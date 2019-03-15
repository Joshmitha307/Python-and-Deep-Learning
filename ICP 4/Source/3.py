from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets
iris_datasets = datasets.load_iris()
x = iris_datasets.data
y = iris_datasets.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=21)
rbfmodel = SVC(kernel='rbf')
rbfmodel.fit(x_train, y_train)
prediction = rbfmodel.predict(x_test)
print("RBF kernel accuracy score is", accuracy_score(prediction, y_test))