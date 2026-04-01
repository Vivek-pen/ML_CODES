import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Input data
hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
marks = np.array([2, 4, 5, 4, 5])

# Step 2: Create & train model
model = LinearRegression()
model.fit(hours, marks)

# Step 3: Get slope & intercept
print("Slope (b):", model.coef_[0])
print("Intercept (a):", model.intercept_)

# Step 4: Predict using SAME X (important)
y_pred = model.predict(hours)

# Step 5: Plot graph
plt.scatter(hours, marks)   # actual points
plt.plot(hours, y_pred)     # straight regression line

plt.title("Simple Linear Regression")
plt.xlabel("Hours")
plt.ylabel("Marks")

plt.show()

# Step 6: Predict new value
x_new = np.array([[6]])
y_new = model.predict(x_new)

print("Predicted marks for 6 hours:", y_new[0])