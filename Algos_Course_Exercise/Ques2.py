"""
Solution for Question 2 of Application Module 1
"""

#importing necessary files: simpleplot, math, and collections.Counter

import alg_load_graph
from collections import Counter
import simpleplot
import random

# Set timeout for CodeSkulptor
import codeskulptor
codeskulptor.set_timeout(400)

def edge(nodes, prob, x):
    edges = []
    for y in xrange(nodes):                                      
        if random.random() < prob and x != y:
            edges.append(y) 
    return edges

def ERAlgo(nodes, prob):
    """
    For every ordered pair of distinct nodes (i,j), 
    the modified algorithm adds the directed edge from i to j
    with probability p.
    """    
    graph = {}
    if(nodes > 0 and prob > 0):
        for x in xrange(nodes):
            graph[x] = edge(nodes,prob,x)           
    return graph    

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
        #create a set of all unique degree values
        degree_distribution_dict = dict(Counter(in_degree_dict.values()))
        num_nodes = len(in_degree_dict)
        for key in degree_distribution_dict.keys():
            degree_distribution_dict[key] = float(degree_distribution_dict[key])/float(num_nodes)
        return degree_distribution_dict
    return {}
    

#loading citation graph from url
citation_graph = alg_load_graph.load_graph(alg_load_graph.CITATION_URL)


def build_plot(graph):
    """
    Build log log plot of normalized indegree distribution
    """
    #calculate in degree distribution (normalized) for citation graph
    distribution_dict = in_degree_distribution(graph)
    if(distribution_dict):
    #create the log/log plot of normalized indegree distribution
        plot = []
        for input_val in distribution_dict.keys():
            #if input_val != 0:
            plot.append([input_val, distribution_dict[input_val]])
        return plot
    return set([])

plot1 = build_plot(ERAlgo(1000,0.4))
plot2 = build_plot(ERAlgo(1000,0.8))
plot3 = build_plot(ERAlgo(500,0.4))
plot4 = build_plot(citation_graph)
#plot4 = build_plot(ERAlgo(1000,1))

if plot1 and plot2 and plot3 and plot4:
    #if plot4:
    simpleplot.plot_lines("Linear plot of Normalized in-degree distribution(using simpleplot)",
                      600, 600,"indegree", "Normalized Distribution",
                      [plot1,plot2,plot3,plot4],True,['plot of n = 1000,p = 0.4',
                                                      'plot of n = 1000,p = 0.8',
                                                      'plot of n = 500,p = 0.4',
                                                      'plot of citation graph'])