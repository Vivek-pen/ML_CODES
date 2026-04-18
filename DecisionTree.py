import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# FIXED DATA (same length)
data = {
    'age':    [23, 46, 64, 64, 21, 34, 45],
    'income': [32000, 65000, 40000, 57000, 70000, 50000, 45000],
    'buys':   [0, 1, 1, 1, 0, 0, 0]
}

df = pd.DataFrame(data)

X = df[["age","income"]]
y = df["buys"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Model
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

# Prediction
y_pred = dt.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))


plot_tree(dt, filled=True,
          class_names=["No","Yes"],
          feature_names=["Age", "Income"])

plt.title("Decision Tree")
plt.show()
