import pickle
from sklearn.datasets import load_iris
#from sklearn.linear_model import LogisticRegression
from sklearn import tree

# 1. Load Data (Iris Flower Dataset)
X, y = load_iris(return_X_y=True)

# 2. Train Model
print("Training model...")
#clf = LogisticRegression(max_iter=200)
clf = tree.DecisionTreeClassifier()
clf.fit(X, y)

# 3. Save Model (The "Artifact")
with open("model2.pkl", "wb") as f:
    pickle.dump(clf, f)

print("Success! Model trained and saved to model.pkl")