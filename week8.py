from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

X = np.array([10,20,30,40,50,60,70]).reshape(-1,1)
y = np.array([1,1,1,1,0,0,0])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

sample = [[25]]
prediction = model.predict(sample)

print("Predicted class:", prediction[0])

plt.scatter(X, y)  # original data
plt.plot(X_test, y_pred)  # logistic curve
plt.xlabel("X")
plt.ylabel("Probability")
plt.title("Logistic Regression Curve")
plt.show()