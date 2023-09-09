# Importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# Load the dataset
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:, [3, 4]].values

# Determine the optimal number of clusters using the elbow method
wcss = []  # Within-cluster sum of squares
for num_clusters in range(1, 11):
    kmeans = KMeans(n_clusters=num_clusters, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot the elbow method results
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS (Within-cluster sum of squares)')
plt.show()

# Train the K-Means model with the optimal number of clusters
optimal_num_clusters = 5
kmeans = KMeans(n_clusters=optimal_num_clusters, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Visualize the clusters
colors = ['red', 'blue', 'green', 'cyan', 'magenta']
cluster_labels = [f'Cluster {i + 1}' for i in range(optimal_num_clusters)]

for cluster_num in range(optimal_num_clusters):
    plt.scatter(X[y_kmeans == cluster_num, 0], X[y_kmeans == cluster_num, 1], s=100, c=colors[cluster_num], label=cluster_labels[cluster_num])

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
