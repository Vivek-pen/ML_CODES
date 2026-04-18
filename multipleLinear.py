import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = np.array([
    [1000, 2],
    [1200, 2],
    [1500, 3],
    [1800, 3],
    [2000, 4]
])

y = np.array([200000, 250000, 300000, 350000, 400000])

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

plt.scatter(y, y_pred)   # actual vs predicted
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Multiple Linear Regression")

plt.plot(y, y)
plt.show()

new_house = np.array([[1600, 3]])
price = model.predict(new_house)

print("Predicted Price:", price[0])
