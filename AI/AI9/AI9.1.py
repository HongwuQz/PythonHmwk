import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
iris_tree = tree.DecisionTreeClassifier(criterion='entropy')
iris_tree = iris_tree.fit(iris.data,iris.target)
plt.figure(1)
tree.plot_tree(iris_tree)
plt.show()