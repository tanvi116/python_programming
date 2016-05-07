"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

#from alg_cluster import Cluster

import urllib2
import math
import alg_cluster 

"""
Defining urls to load data
"""

BASE_URL = "http://storage.googleapis.com/codeskulptor-assets/data_clustering/"

COUNTIES_3108 = BASE_URL + "unifiedCancerData_3108.csv"
COUNTIES_896 = BASE_URL + "unifiedCancerData_896.csv"
COUNTIES_290 = BASE_URL + "unifiedCancerData_290.csv"
COUNTIES_111 = BASE_URL + "unifiedCancerData_111.csv"

def load_cluster_data(url):
    """
    Function that loads a cluster data from csv.
    Returns cluster list
    Load cancer risk data from .csv file
    """    
    # open url and read cluster data
    data_file = urllib2.urlopen(url)
    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    # populate cluster info in Cluster class
    data_tokens = [line.split(',') for line in data_lines]
    cluster_list = []
    cluster_items = [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])] for tokens in data_tokens]    
    for cluster_item in cluster_items:
        cluster_list.append(alg_cluster.Cluster(set([cluster_item[0]]),cluster_item[1], cluster_item[2],cluster_item[3],cluster_item[4]))
    return cluster_list


######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1,idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    result = (float('Inf'),-1,-1)
    min_dist = float('Inf')
    for idx1 in range(0,len(cluster_list)):
        for idx2 in range(idx1 + 1, len(cluster_list)):
            dist = pair_distance(cluster_list, idx1, idx2)[0]
            if float(min_dist) > dist:
                min_dist = dist
                result = (min_dist, idx1, idx2)
                #print min_dist
            #if float(min_dist) == dist:
                #result.add((min_dist,idx1,idx2))
                #print result            
    return result

def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    #base case    
        
    size_n = len(cluster_list)  
    if size_n <= 3:
        result = slow_closest_pair(cluster_list)
    else:
        mid_idx = int(math.ceil(size_n/2))
        cluster_list.sort(key = lambda Cluster: Cluster.horiz_center())
        
        pleft = cluster_list[0:mid_idx]
        pright = cluster_list[mid_idx:size_n]

        result_left = fast_closest_pair(pleft)
        
        result_right = fast_closest_pair(pright)
        
        if result_left[0] < result_right[0]:
            result = result_left
        else:
            result = (result_right[0], result_right[1] + mid_idx, result_right[2] + mid_idx)

        mid_hcoord = 0.5 * (cluster_list[mid_idx-1].horiz_center() + cluster_list[mid_idx].horiz_center())        
        
        closest_pair = closest_pair_strip(cluster_list, mid_hcoord, result[0])
        if result[0] > closest_pair[0]:
            result = closest_pair
    return result 


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """
    #vert_list = [item for item in cluster_list if math.fabs(cluster_list[item].horiz_center() - mid) < w] 
    #vert_list.sort(key = lambda Cluster: Cluster.vert_center())

    s_list = []
    for idx in xrange(len(cluster_list)):
        if cluster_list[idx].horiz_center() - horiz_center < half_width:
            s_list.append(cluster_list[idx])

    s_list.sort(key = lambda Cluster: Cluster.vert_center())

    count = len(s_list)
    result = (float('Inf'),-1,-1)
    min_dist = float('Inf')
    for idx1 in xrange(0,count - 1):
        for idx2 in xrange(idx1 + 1, min(idx1 + 4, count)):
            if min_dist > pair_distance(s_list,idx1,idx2):
                min_dist = pair_distance(s_list,idx1,idx2)
                result = (min_dist,s_list[idx1],s_list[idx2])
    return result     
 
    
######################################################################
# Code for hierachical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    
    return []


######################################################################
# Code for k-means clustering

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # position initial clusters at the location of clusters with largest populations
            
    return []

#cl=load_cluster_data(COUNTIES_111)

#print slow_closest_pair(cl)

#print fast_closest_pair(cl)

#print load_cluster_data(COUNTIES_3108)