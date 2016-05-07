"""
Beadth-First Seach and Connected Components
Connected Components and graph resilience
"""

#importing necessary files: deque

from collections import deque

def bfs_visited(ugraph, start_node):
    """
    Takes the undirected graph ugraph and the node start_node and returns the set consisting
    of all nodes that are visited by a breadth-first search that starts at start_node. 
    """  
    if ugraph:  
        new_queue = deque()
        visited = set([start_node])
        new_queue.append(start_node)
        while len(new_queue) > 0:
            node_j = new_queue.popleft()
            if ugraph.get(node_j):
                for neighbor in ugraph[node_j]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        new_queue.append(neighbor)
        return visited
    else:
        return set()


def cc_visited(ugraph):
    """
    Takes the undirected graph ugraph and returns a list of sets, 
    where each set consists of all the nodes (and nothing else) in a connected component, 
    and there is exactly one set in the list for each connected component in ugraph and nothing else.
    """    
    connected_components = list()
    if ugraph:
        remaining_nodes = set(ugraph.keys())        
        while remaining_nodes:
            node_i = remaining_nodes.pop()
            visited = bfs_visited(ugraph,node_i)
            connected_components.append(visited)
            remaining_nodes.difference_update(visited)
    return connected_components

def largest_cc_size(ugraph):
    """
        Takes the undirected graph ugraph and returns the size (an integer)
        of the largest connected component in ugraph.
    """
    connected_components = cc_visited(ugraph)
    max_len = 0
    if connected_components:
        for connected_component in connected_components:
            if max_len < len(connected_component):
                max_len = len(connected_component)
    return max_len

def compute_resilience(ugraph, attack_order):
    """
    Takes the undirected graph ugraph, a list of nodes attack_order and iterates through the nodes in attack_order.
    For each node in the list, the function removes the given node and its edges from the graph
    and then computes the size of the largest connected component for the resulting graph.
The function should return a list whose k+1 th entry is the size of the largest connected component in the graph
 after the removal of the first k nodes in attack_order. 
 The first entry (indexed by zero) is the size of the largest connected component in the original graph. 
    """
    if ugraph:
        resilience_list = [largest_cc_size(ugraph)]
        for node in attack_order:
            if ugraph.get(node):            
                edges = ugraph.pop(node)
                for edge in edges:
                    if ugraph.get(edge) and node in ugraph[edge]:
                        ugraph[edge].remove(node)
                resilience_list.append(largest_cc_size(ugraph))
            else:
                resilience_list.append(0)
            #print resilience_list
        return resilience_list
    else:
        return []

#print cc_visited(GRAPH10)
#print largest_cc_size(GRAPH10)
#print compute_resilience(GRAPH10, (1,2))

