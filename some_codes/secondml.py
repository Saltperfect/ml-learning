from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

iris = load_iris()
test_idx = [0]

train_target = np.delete(iris.target , test_idx)
train_data = np.delete(iris.data , test_idx)
#train_data = train_data[:, None]

test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data , train_target)

print (clf.pridict(test_target))
print (test_data)