from sklearn import tree
features = [[150,1],[140,1],[120,0],[130,0]]
lables = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,lables)
print (clf.predict([[160,1]]))