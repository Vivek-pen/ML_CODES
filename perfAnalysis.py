import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Required models
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

# Dataset (same as your table)
data = {
    'Age': [45, 54, 60, 48, 52, 46],
    'Sex': [1, 0, 1, 0, 1, 0],
    'ChestPain': [3, 2, 1, 2, 3, 1],
    'BP': [130, 140, 120, 135, 150, 128],
    'Cholesterol': [230, 250, 240, 220, 260, 210],
    'MaxHR': [150, 140, 130, 160, 120, 170],
    'Target': [1, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

# Split
X = df.drop('Target', axis=1)
y = df['Target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 1. Decision Tree
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
pred_dt = dt.predict(X_test)

# 2. SVM
svm = SVC()
svm.fit(X_train, y_train)
pred_svm = svm.predict(X_test)

# 3. Random Forest
rf = RandomForestClassifier()
rf.fit(X_train, y_train)
pred_rf = rf.predict(X_test)

# Accuracy
print("Decision Tree Accuracy:", accuracy_score(y_test, pred_dt))
print("SVM Accuracy:", accuracy_score(y_test, pred_svm))
print("Random Forest Accuracy:", accuracy_score(y_test, pred_rf))