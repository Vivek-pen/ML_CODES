from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

# Step 1: Load dataset
data = load_iris()
X = data.data
y = data.target

# Step 2: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Step 3: Create model (k = 3)
knn = KNeighborsClassifier(n_neighbors=3)

# Step 4: Train model
knn.fit(X_train, y_train)

# Step 5: Predict
y_pred = knn.predict(X_test)

# Step 6: Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Step 7: Predict new sample
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = knn.predict(sample)

print("Predicted class:", prediction[0])