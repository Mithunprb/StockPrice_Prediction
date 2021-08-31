import matplotlib.pyplot as plt
from matplotlib import style
plt.xkcd()
from sklearn.datasets import make_blobs
import numpy as np
import random 

centers = random.randrange(2, 8)

X, y = make_blobs(n_samples=50, centers=centers, n_features=2)

colors = 10*['g', 'r', 'c', 'b', 'k']

class Mean_Shift:
	"""docstring for Mean_Shift"""
	def __init__(self,  radius=None, radius_norm_step = 100):
		super(Mean_Shift, self).__init__()
		self.radius = radius
		self.radius_norm_step = radius_norm_step

	def fit(self, data):

		if self.radius == None:
			all_data_centroid = np.average(data, axis=0)
			all_data_norm = np.linalg.norm(all_data_centroid)
			self.radius = all_data_norm / self.radius_norm_step



		centeroids = {}

		for i in range(len(data)):
			centeroids[i] = data[i]
		
		weights = [i for i in range(self.radius_norm_step)][::-1]

		while True:
			new_centroids = []
			for i in centeroids:
				in_bandwidth = []
				centeroid = centeroids[i]

				

				for featureset in data:
					distance = np.linalg.norm(featureset-centeroid)
					if distance == 0:
						distance = 0.000000001
					weight_index = int(distance/self.radius)
					if weight_index > self.radius_norm_step-1:
						weight_index = self.radius_norm_step-1

					to_add = (weights[weight_index]**2)*[featureset]
					in_bandwidth += to_add



					if np.linalg.norm(featureset-centeroid) < self.radius:
						in_bandwidth.append(featureset)

				new_centroid = np.average(in_bandwidth, axis=0)
				new_centroids.append(tuple(new_centroid))

			uniques = sorted(list(set(new_centroids)))

			to_pop = []

			for i in uniques:
				for ii in uniques:
					if i == ii:
						pass
					elif np.linalg.norm(np.array(i)-np.array(ii))<= self.radius:
						to_pop.append(ii)
						break

			for i in to_pop:
				try:
					uniques.remove(i)
				except:
					pass

						

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

		self.classifications = {}

		for i in range(len(self.centeroids)):
			self.classifications[i] = []

		for featureset in data:
			distances = [np.linalg.norm(featureset - self.centeroids[centeroid]) for centeroid in self.centeroids]
			classification = distances.index(min(distances))
			self.classifications[classification].append(featureset)


	def predict(self, data):
		distances = [np.linalg.norm(featureset - self.centeroids[centeroid]) for centeroid in self.centeroids]
		classification = distances.index(min(distances))
		return classification


clf = Mean_Shift()
clf.fit(X)

centeroids = clf.centeroids

#plt.scatter(X[: ,0], X[:, 1], s=150)

for classification in clf.classifications:
	color = colors[classification]
	for featureset in clf.classifications[classification]:
		plt.scatter(featureset[0], featureset[1], marker='x', color = color, s=150, linewidth=5)



for c in centeroids:
	plt.scatter(centeroids[c][0], centeroids[c][1], color='k', marker='*', s=150)
plt.show()





		