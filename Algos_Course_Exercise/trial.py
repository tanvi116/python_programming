"""
Solution for Question 3 of Application Module 1
"""
from alg_dpa_trial import DPATrial as DPA
from collections import Counter


def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete directed graph with the specified number of nodes.
    """
    complete_graph = {}
    if(num_nodes > 0):
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
        in_degree_dict = {}
        #print in_degree_dict
        for head in digraph.keys():
            if(digraph[head]):
                #value = digraph[head]
                for tail in digraph[head]:
                    if(in_degree_dict.get(tail)):
                        in_degree_dict[tail]+=1
                    else:
                        in_degree_dict[tail] = 0
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

def DPAalgo(n,m):
    distribution = {}
    if(1 <= m < n):
        m_graph = make_complete_graph(m)
        #random_connect = DPA(m)
        for i in xrange(m,n):
            in_deg_dict = compute_in_degrees(m_graph)
            total_in = sum(x for x in in_deg_dict.values())
            trial = DPA(total_in)
            m_graph[i] = trial.run_trial(m)
        distribution = in_degree_distribution(m_graph)
        distribution.pop(0)
    return distribution

print DPAalgo(27770,12)