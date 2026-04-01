import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 1: Input data
X = np.array([
    [1, 2],
    [1.5, 1.8],
    [5, 8],
    [8, 8],
    [1, 0.6],
    [9, 11]
])

# Step 2: Create model (k = 2 clusters)
kmeans = KMeans(n_clusters=2, random_state=42)

# Step 3: Train model
kmeans.fit(X)

# Step 4: Get cluster labels
labels = kmeans.labels_

# Step 5: Get centroids
centroids = kmeans.cluster_centers_

print("Cluster Labels:", labels)
print("Centroids:\n", centroids)

# Step 6: Plot clusters
plt.scatter(X[:,0], X[:,1], c=labels)   # data points
plt.scatter(centroids[:,0], centroids[:,1], marker='X')  # centroids

plt.title("K-Means Clustering")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()