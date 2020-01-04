import cv2, numpy as np
from sklearn.cluster import KMeans

ans = {}

def get_colors_names(image_path):
    return read_image(image_path)

def visualize_colors(cluster, centroids):
    # Get the number of different clusters, create histogram, and normalize
    labels = np.arange(0, len(np.unique(cluster.labels_)) + 1)
    (hist, _) = np.histogram(cluster.labels_, bins = labels)
    hist = hist.astype("float")
    hist /= hist.sum()

    # Create frequency rect and iterate through each cluster's color and percentage
    colors = sorted([(percent, color) for (percent, color) in zip(hist, centroids)])
    index = 0
    for (percent, color) in colors:
        ans[index] = {}
        ans[index]['color'] = color
        ans[index]['perecent'] = percent
        index +=1
        print(color, "{:0.2f}%".format(percent * 100))
    return ans

def read_image(image_path):
    # Load image and convert to a list of pixels
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    reshape = image.reshape((image.shape[0] * image.shape[1], 3))

    # Find and display most dominant colors
    cluster = KMeans(n_clusters=4).fit(reshape)
    return visualize_colors(cluster, cluster.cluster_centers_)


