import alg_load_graph
import timeit
from collections import Counter

# code you want to evaluate

# Set timeout for CodeSkulptor
#import codeskulptor
#codeskulptor.set_timeout(100)

EX_GRAPH0 = {0: set([1,2]), 1: set([]), 2: set([])}

EX_GRAPH1 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3]), 3: set ([0]),4: set ([1]), 5: set([2]), 6:set([])}

def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the in-degrees for the nodes in the graph.
    """
    if(digraph):
        #node_set = digraph.keys()
        #print node_set
        in_degree_dict = dict((key, 0) for key in digraph.keys())
        #print in_degree_dict
        for head in digraph.keys():
            if(digraph[head]):
                #value = digraph[head]
                for tail in digraph[head]:
                    in_degree_dict[tail]+=1
        #print in_degree_dict
        return in_degree_dict
    return {}

def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the unnormalized distribution of the in-degrees of the graph.
    """
    if(digraph):
        in_degree_dict = compute_in_degrees(digraph)
        #compute in degree dictionary
        #degree_set = set(in_degree_dict.values())
        #create a set of all unique degree values
        return dict(Counter(in_degree_dict.values()))
        #create a dictionary from the degree set initialized with 0 values
        #for node in in_degree_dict.keys():
            #deg_distribution_dict[in_degree_dict[node]] += 1
            #calculating the number of nodes having same degree
        #return deg_distribution_dict
    return {}
    

#loading citation graph from url
citation_graph = alg_load_graph.load_graph(alg_load_graph.CITATION_URL)

#print citation_graph

#calculate in degree distribution (unnormalized) for citation graph


start_time = timeit.default_timer()
#distribution_dict = compute_in_degrees(EX_GRAPH1)
distribution_dict = in_degree_distribution(citation_graph)
elapsed = timeit.default_timer() - start_time

print distribution_dict

print elapsed

