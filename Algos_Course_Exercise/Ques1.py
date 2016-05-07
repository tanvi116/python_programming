"""
Solution for Question 1 of Application Module 1
"""

#importing necessary files: simpleplot, math, citation graph 
#input file and collections.Counter

import alg_load_graph
from collections import Counter
import simpleplot
import math

# Set timeout for CodeSkulptor
import codeskulptor
codeskulptor.set_timeout(20)

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
        degree_distribution_dict = dict(Counter(in_degree_dict.values()))
        num_nodes = len(in_degree_dict)
        for key in degree_distribution_dict.keys():
            degree_distribution_dict[key] = float(degree_distribution_dict[key])/float(num_nodes)
        return degree_distribution_dict
        #create a dictionary from the degree set initialized with 0 values
        #for node in in_degree_dict.keys():
            #deg_distribution_dict[in_degree_dict[node]] += 1
            #calculating the number of nodes having same degree
        #return deg_distribution_dict
    return {}
    

#loading citation graph from url
citation_graph = alg_load_graph.load_graph(alg_load_graph.CITATION_URL)


def build_plot():
    """
    Build log log plot of normalized indegree distribution
    """
    #calculate in degree distribution (normalized) for citation graph
    distribution_dict = in_degree_distribution(citation_graph)
    #create the log/log plot of normalized indegree distribution
    plot = []
    for input_val in distribution_dict.keys():
        if input_val != 0:
            plot.append([math.log(input_val), math.log(distribution_dict[input_val])])
    return plot

plot1 = build_plot()

simpleplot.plot_scatter("log/log plot of Normalized in-degree distribution(using simpleplot)", 600, 600,"log(indegree) base e", "log(Normalized Distribution) base e", [plot1],['plot of citation graph'])