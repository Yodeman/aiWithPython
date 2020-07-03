import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth

input_file = 'sales.csv'
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')

X = []
for count, row in enumerate(file_reader):
    if not count:
        names = row[1:]
        continue
    X.append([float(x) for x in row[1:]])
X = np.array(X)

# Estimate bandwidth of input data
bandwidth = estimate_bandwidth(X, quantile=0.8, n_samples=len(X))

meanshift_model = MeanShift(bandwidth=bandwidth, bin_seeding=True)
meanshift_model.fit(X)

labels = meanshift_model.labels_
cluster_centers = meanshift_model.cluster_centers_
num_clusters = len(np.unique(labels))

print("\nNumber of clusters in input data =", num_clusters)
print("\nCenters of clusters:")
print('\t'.join([names[:3] for name in names]))
for cluster_center in cluster_centers:
    print('\t'.join([str(int(x)) for x in cluster_center]))

cluster_centers_2d = cluster_centers[:, 1:3]
plt.figure()
plt.scatter(cluster_centers_2d[:,0], cluster_centers_2d[:,1], s=120,
            edgecolors='black', facecolors='none')
offset = 0.25
plt.xlim(cluster_centers_2d[:,0].min()-offset *cluster_centers_2d[:,0].ptp(),
        cluster_centers_2d[:,0].max()+offset*cluster_centers_2d[:,0].ptp())
plt.ylim(cluster_centers_2d[:,1].min()-offset*cluster_centers_2d[:,1].ptp(),
        cluster_centers_2d[:,1].max()+offset*cluster_centers_2d[:,1].ptp())
plt.title('Centers of 2D clusters')
plt.show()