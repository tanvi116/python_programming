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

from alg_cluster import Cluster
import urllib2
import math


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
        cluster_list.append(Cluster(set([cluster_item[0]]),cluster_item[1], cluster_item[2],cluster_item[3],cluster_item[4]))
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
    return (cluster_list[idx1].distance(cluster_list[idx2]), idx1, idx2)


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    result = [(float('Inf'),-1,-1)]
    min_dist = float('Inf')
    for idx1 in range(0,len(cluster_list)):
        for idx2 in range(idx1 + 1, len(cluster_list)):
            dist = pair_distance(cluster_list, idx1, idx2)[0]
            if float(min_dist) > dist:
                min_dist = dist
                result = [(min_dist, idx1, idx2)]
                #print min_dist
            if float(min_dist) == dist:
                result.append((min_dist,idx1,idx2))
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
    def fast_helper(cluster_list, horiz_order, vert_order):
        """
        Divide and conquer method for computing distance between closest pair of points
        Running time is O(n * log(n))
        
        horiz_order and vert_order are lists of indices for clusters
        ordered horizontally and vertically
        
        Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where
        cluster_list[idx1] and cluster_list[idx2]
        have the smallest distance dist of any pair of clusters
    
        """
        #base case    
        
        size_n = len(horiz_order)
        if size_n <= 3:
            s_list = []
            for idx in horiz_order:
                s_list.append(cluster_list[idx])
            (distance,idx1,idx2) = slow_closest_pair(s_list).pop()
            return (distance, horiz_order[idx1], horiz_order[idx2])
        else:
            mid_idx = int(math.ceil(size_n/2))
            horiz_order_left = horiz_order[0:mid_idx]
            horiz_order_right = horiz_order[mid_idx:size_n]
            
            vert_coord_index_left = [(cluster_list[idx].vert_center(),idx) for idx in horiz_order_left]
            vert_coord_index_left.sort()

            vert_coord_index_right = [(cluster_list[idx].vert_center(),idx) for idx in horiz_order_right]
            vert_coord_index_right.sort()

            vert_order_left = [vert_coord_index_left[idx][1] for idx in range(len(vert_coord_index_left))]
            vert_order_right = [vert_coord_index_right[idx][1] for idx in range(len(vert_coord_index_right))]

            closest_pair_left = fast_helper(cluster_list,horiz_order_left,vert_order_left)
            closest_pair_right = fast_helper(cluster_list,horiz_order_right,vert_order_right)

            if closest_pair_left[0] < closest_pair_right[0]:
                closest_pair = closest_pair_left
            else:
                closest_pair = closest_pair_right
            
            mid_hcoord = 0.5 * (cluster_list[horiz_order[mid_idx-1]].horiz_center() + cluster_list[horiz_order[mid_idx]].horiz_center())

            s_list = []
            for idx in vert_order:
                if cluster_list[idx].horiz_center() - mid_hcoord < closest_pair[0]:
                    s_list.append(idx)

            for idx in range(0, len(s_list) - 1):
                for jdx in range(idx + 1, min(idx + 4, len(s_list))):
                    distance = cluster_list[s_list[idx]].distance(cluster_list[s_list[jdx]])
                    if distance < closest_pair[0]:
                        closest_pair = (distance, s_list[idx], s_list[jdx])
  
        return closest_pair
            
    # compute list of indices for the clusters ordered in the horizontal direction
    hcoord_and_index = [(cluster_list[idx].horiz_center(), idx) 
                        for idx in range(len(cluster_list))] 
    
    hcoord_and_index.sort()
    
    horiz_order = [hcoord_and_index[idx][1] for idx in range(len(hcoord_and_index))]
    
    # compute list of indices for the clusters ordered in vertical direction
    vcoord_and_index = [(cluster_list[idx].vert_center(), idx) 
                        for idx in range(len(cluster_list))]    
    vcoord_and_index.sort()
    
    vert_order = [vcoord_and_index[idx][1] for idx in range(len(vcoord_and_index))]
    
    # compute answer recursively
    answer = fast_helper(cluster_list, horiz_order, vert_order) 
    
    return (answer[0], min(answer[1:]), max(answer[1:]))

        #        set([(dist_right[0],dist_right[1]+m,dist_right[2]+m)])
        #mid = 0.5 * (cluster_list[m-1].horiz_center() + cluster_list[m].horiz_center())
        #pair_strip = closest_pair_strip(cluster_list, mid, result[0])
        #if result[0] > pair_strip[0]:
        #    result = pair_strip
    #return result

        #print pleft
        #print pright     


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
    vert_list = [item for item in cluster_list if math.fabs(cluster_list[item].horiz_center() - mid) < w] 
    vert_list.sort(key = lambda Cluster: Cluster.vert_center())
    count = len(vert_list)
    result = set([(Decimal('Infinity'),-1,-1)])
    min_dist = Decimal('Infinity')
    for idx1 in xrange(0,count -2):
        for idx2 in xrange(idx1+1,min(idx1+3,count -1)):
            if min_dist > pair_distance(vert_list,idx1,idx2):
                min_dist = pair_distance(vert_list,idx1,idx2)
                result = set([(min_dist,vert_list[idx1],vert_list[idx2])])
    return result
            
 
    
######################################################################
# Code for hierarchical clustering


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



cl=load_cluster_data(COUNTIES_111)

#print slow_closest_pair(cl)

print fast_closest_pair(cl)

#print load_cluster_data(COUNTIES_3108)