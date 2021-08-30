import matplotlib.pyplot as plt
from matplotlib import style
plt.xkcd()

import numpy as np

X  = np.array([[1,2],
			  [1.5, 1.8],
			  [5, 8],
			  [1, 0.6],
			  [9, 11],
			  [8, 2],
			  [10, 2],
			  [9, 3],])

colors = 10*['g', 'r', 'c', 'b', 'k']

class Mean_Shift:
	"""docstring for Mean_Shift"""
	def __init__(self,  radius=4):
		super(Mean_Shift, self).__init__()
		self.radius = radius

	def fit(self, data):
		centeroids = {}

		for i in range(len(data)):
			centeroids[i] = data[i]

		while True:
			new_centroids = []
			for i in centeroids:
				in_bandwidth = []
				centeroid = centeroids[i]
				for featureset in data:
					if np.linalg.norm(featureset-centeroid) < self.radius:
						in_bandwidth.append(featureset)

				new_centroid = np.average(in_bandwidth, axis=0)
				new_centroids.append(tuple(new_centroid))

			uniques = sorted(list(set(new_centroids)))

			prev_centroids = dict(centeroids)

			centeroids = {}

			for i in range(len(uniques)):
				centeroids[i] = np.array(uniques[i])

			optimized = True

			for i in centeroids:
				if not np.array_equal(centeroids[i], prev_centroids[i]):
					optimized = False

				if not optimized:
					break
			if  optimized:
				break
		self.centeroids = centeroids

	def predict(self, data):
		pass

clf = Mean_Shift()
clf.fit(X)

centeroids = clf.centeroids

plt.scatter(X[: ,0], X[:, 1], s=150)

for c in centeroids:
	plt.scatter(centeroids[c][0], centeroids[c][1], color='k', marker='*', s=150)
plt.show()





		