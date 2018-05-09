
#!/usr/bin/env python
__maintainer__ 	= "jefferson amado <JAPeTo>"
__email__ = "jeffersonamado@gmail.com"
import sys, os, time
from constants import *
import numpy as np
import time
from sklearn.cluster import KMeans
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer

def load_embendding(filename):
    print("Load file embendding ... ")
    with open(filename, 'r') as f:
        start = time.time()
        word_vec = {}
        data_vector, words = [], []
        for line in f:
            word, vec = line.split(' ')[0], np.asarray([float(x) for x in line.split(' ')[1:]])
            word_vec[word] = np.asarray(vec).reshape(-1, 1)
            words.append(word)
            data_vector.append(vec)
        n_words = len( word_vec )
        vec_size = len( word_vec[word] )
        print("#words = {0}, vector size = {1}".format(n_words, vec_size))
        return word_vec, data_vector, words

def compute_clustering(n_clusters= 100, output_file="embed_cluster.txt", word_vec= None):
    start = time.time()
    #print("Compute clustering ... ")

    # i will change it into numpy matrix
    #word_vec = np.array(word_vec)
    #print ("word_vec ", word_vec)
    # normalize into positive value, std deviation
    #word_vec = StandardScaler().fit_transform(word_vec)
    #print ("word_vec ", word_vec)
    # normalize it between 0 and 1
    word_vec = np.asarray(word_vec).reshape(-1, 1)
    print ("word_vec ", word_vec)

    print("Compute clustering ... ")
    kmeans = KMeans(n_clusters=n_clusters, n_jobs=-1, random_state=0)
    print("idx")
    idx = kmeans.fit(word_vec[0])
    #idx = kmeans.fit_predict(word_vec[0])

    #print("finished in {:.2f} sec.".format(
    #	time.time() - start))
    #start = time.time()
    #print("Generate output file ... ")
    #word_centroid_list = list(zip(word_vec, idx))
    #word_centroid_list_sort = sorted(word_centroid_list, key=lambda el: el[1], reverse=False)
    #file_out = open(output_file, "w")
    #file_out.write("WORD\tCLUSTER_ID\n")
    #for word_centroid in word_centroid_list_sort:
    #    line = word_centroid[0] + '\t' + str(word_centroid[1]) + '\n'
    #    file_out.write(line)
    #file_out.close()
    #print("finished in {:.2f} sec.".format(time.time() - start))

if __name__ == '__main__':
    word_vec,  data_vector, words = load_embendding(filename = DATA_DIR+"SBW-vectors-300-min5-1.20000.txt")
    compute_clustering(output_file= DATA_DIR+"embed_cluster-1.20000.txt", word_vec=data_vector)
    #print( np.array(word_vec['grandes']) )












