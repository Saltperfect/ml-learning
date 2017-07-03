from sklearn import tree
features = [[150,0], [140,0], [120,1], [130,1]]
labels = [1, 1, 0, 0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[160,0]]))	
