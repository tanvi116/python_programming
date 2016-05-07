"""
Solution for Question 3 of Application Module 1
"""
from alg_dpa_trial import DPATrial as DPA
from collections import Counter
import simpleplot
import math
import alg_load_graph

# Set timeout for CodeSkulptor
import codeskulptor
codeskulptor.set_timeout(50)

def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete directed graph with the specified number of nodes.
    """
    complete_graph = {}
    if(num_nodes > 0):
        #Checks if number of nodes is not positive and returns empty dictionary
        #return complete_graph
        #Create complete directed graph dictionary where each node is the key and its value is a set of all nodes except itself
        for node in range(num_nodes):
            complete_graph[node] = set([connected_node for connected_node in range (num_nodes) if connected_node!= node])           
        #print complete_graph
    return complete_graph

#print make_complete_graph(5)

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
        degree_distribution_dict = dict(Counter(in_degree_dict.values()))
        num_nodes = len(in_degree_dict)
        for key in degree_distribution_dict.keys():
            degree_distribution_dict[key] = float(degree_distribution_dict[key])/float(num_nodes)
        return degree_distribution_dict        
    return {}

def DPAalgo(n,m,add):
    m_graph = make_complete_graph(m)
    random_connect = DPA(m)
    for i in xrange(m,n):
        m_graph[i]=random_connect.run_trial(add)
    distribution = in_degree_distribution(m_graph)
    distribution.pop(0)
    return distribution

def build_plot(distribution_dict):
    """
    Build log log plot of normalized indegree distribution
    """
    #create the log/log plot of normalized indegree distribution
    plot = []
    for input_val in distribution_dict.keys():
        if input_val != 0:
            plot.append([math.log(input_val), math.log(distribution_dict[input_val])])
    return plot

citation_graph = alg_load_graph.load_graph(alg_load_graph.CITATION_URL)
plot1 = build_plot(in_degree_distribution(citation_graph))
plot2 = build_plot(DPAalgo(27770,12,12))

simpleplot.plot_scatter("log/log plot of Normalized in-degree distribution(using simpleplot)", 600, 600,"log(indegree) base e", "log(Normalized Distribution) base e", [plot1,plot2],['plot of citation graph','plot of DPA graph (n=27770,m=12)'])