from sklearn.cluster import KMeans
from sklearn.cluster import FeatureAgglomeration
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import SpectralClustering
from yellowbrick.cluster import KElbowVisualizer
import numpy
import time
import pickle

if __name__ == '__main__':

    models = [KMeans(), AgglomerativeClustering(), SpectralClustering()]
    k_ranges = [(4,15)]

    cols, data = pickle.load(open('C:\\Users\\tom.lappas\\code\\travel\\data\\raw\\google_review_ratings.pkl', 'rb'))
    data = numpy.array(data)

    #main_start = time.time()

    for model in models:
        #print('{}:'.format(model.__name__))
        for ks in k_ranges:
            #print('\tk range: {}', end='')
            current_start = time.time()
            visualizer = KElbowVisualizer(model, k=ks)
            visualizer.fit(data)
            visualizer.poof()
            duration = time.time() - current_start
            #print(' - duration: {}'.format(duration.strptime('%H:%M:%S')))
            pickle.dump(visualizer, open('C:\\Users\\tom.lappas\\code\\travel\\models\\DBSCAN-4-15.pkl','wb'))

    #main_stop = time.time()