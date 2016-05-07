"""
Project 1 - Degree distributions for graphs
"""

EX_GRAPH0 = {0: set([1,2]), 1: set([]), 2: set([])}

EX_GRAPH1 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3]), 3: set ([0]),4: set ([1]), 5: set([2]), 6:set([])}

EX_GRAPH2 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3,7]), 3: set ([7]), 4: set ([1]), 5: set([2]), 6:set([]), 7:set([3]), 8:set([1,2]), 9:set([0,3,4,5,6,7])}
#Global graph constants

def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete directed graph with the specified number of nodes.
    """
    complete_graph = {}
    if(num_nodes < 0):
        #Checks if number of nodes is not positive and returns empty dictionary
        return complete_graph
    else:
        #Create complete directed graph dictionary where each node is the key and its value is a set of all nodes except itself
        for node in range(0,num_nodes):
            complete_graph[node] = set([connected_node for connected_node in range (0,num_nodes)])
            complete_graph[node].discard(node)
            #print complete_graph
        return complete_graph

def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) and computes the in-degrees for the nodes in the graph.
    """
    if(digraph):
        node_set = set(digraph.keys())
        #print node_set
        in_degree_dict = dict.fromkeys(node_set,0)
        #print in_degree_dict
        for head in node_set:
            #This loop checks for each node as a head node
            for tail in node_set:
                #This loop checks the existence of an edge from the all nodes in the graph to head node
                if(head in digraph[tail]):
                    in_degree_dict[head] = in_degree_dict[head] + 1
                    #incremenet degree if edge exists
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
        degree_set = set(in_degree_dict.values())
        #create a set of all unique degree values
        deg_distribution_dict = dict.fromkeys(degree_set,0)
        #create a dictionary from the degree set initialized with 0 values
        for node in in_degree_dict.keys():
            deg_distribution_dict[in_degree_dict[node]] = deg_distribution_dict[in_degree_dict[node]] + 1
            #calculating the number of nodes having same degree
        return deg_distribution_dict
    return {}
    
#print in_degree_distribution(GRAPH4)
