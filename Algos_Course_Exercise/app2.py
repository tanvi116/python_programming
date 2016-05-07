from alg_upa_trial import UPATrial as UPA
from collections import Counter
import alg_application2_provided
import random
import module2
import matplotlib.pyplot as plt
import time

GRAPH2 = {1: set([2, 4, 6, 8,3]),
          2: set([1, 3, 5, 7]),
          3: set([2, 4, 6, 8,1]),
          4: set([1, 3, 7]),
          5: set([2, 6, 8]),
          6: set([1, 3, 5, 7]),
          7: set([2, 4, 6, 8]),
          8: set([1, 3, 5, 7])}

def uERAlgo(nodes, prob):
    """
    For every ordered pair of distinct nodes (i,j), 
    the modified algorithm adds the undirected edge between i and j
    with probability p.
    """    
    graph = {}
    if(nodes > 0 and prob > 0):
        for i in range(nodes):
            graph[i] = set([])
        for i in range(nodes):
            for j in range(i+1,nodes):
                if random.random() < prob:
                    graph[i].update([j])
                    graph[j].update([i])                                               
    return graph  

def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and returns a dictionary corresponding to a complete undirected graph with the specified number of nodes.
    """
    complete_graph = {}
    if(num_nodes > 0):
        #Checks if number of nodes is not positive and returns empty dictionary        
        #Create complete undirected graph dictionary where each node is the key and its value is a set of all nodes except itself
        for node in range(num_nodes):
            complete_graph[node] = set([connected_node for connected_node in range (num_nodes) if connected_node!= node])           
    return complete_graph

def compute_degrees(ugraph):
    """
    Takes an undirected graph digraph (represented as a dictionary) and computes the in-degrees for the nodes in the graph.
    """
    if(ugraph):               
        degree_dict = {}        
        for head in ugraph.keys():
            if ugraph.get(head):                
                for tail in ugraph[head]:
                    if degree_dict.get(tail):
                        degree_dict[tail]+=1
                    else:
                        degree_dict[tail] = 1        
    return degree_dict

def UPAalgo(n,m):
    m_graph = make_complete_graph(m)  
    random_connect = UPA(m)  
    for i in xrange(m,n):        
        if i not in m_graph.keys():
            m_graph[i] = set()
        m_graph[i] = random_connect.run_trial(m)                       
        for item in m_graph[i]:
            m_graph[item].update([i])
        #m_graph[i] = random_connect.run_trial(m)
    return m_graph

def countedges(ugraph):
    edges = 0
    for x in ugraph.keys():
        edges += len(ugraph[x])
    edges = edges/2
    print edges

def random_order(ugraph):
    nodes = ugraph.keys()
    random.shuffle(nodes)
    return nodes


#Ques3
def degreesets(ugraph):
    DegreeSets = {}
    #degree = list(len(ugraph[node]) for node in ugraph.keys() if ugraph.get(node))
    #for k in xrange(len(ugraph)):
    #    nodes = [i for i,x in enumerate(degree) if x == k]
    #    DegreeSets[k] = set(nodes)    
    for k in xrange(len(ugraph)):
        DegreeSets[k] = set()
    for k in ugraph.keys():
        DegreeSets[len(ugraph[k])].add(k)
    return DegreeSets

def fast_targeted_order(ugraph):
    new_graph = alg_application2_provided.copy_graph(ugraph)
    DegreeSets = degreesets(new_graph)
    #print DegreeSets
    #print new_graph
    L = list()
    i = 0
    for k in range(len(new_graph)-1,-1,-1):
        while DegreeSets[k] != set():
            u = DegreeSets[k].pop()     
            #print u       
            #print new_graph[u]
            for neighbor in new_graph[u]:                
                d = len(new_graph[neighbor])               
                DegreeSets[d].remove(neighbor)
                DegreeSets[d-1].add(neighbor)   
                #print "DegreeSets", DegreeSets
            L.insert(i,u)            
            i = i + 1
            #if new_graph.get(u): 
            alg_application2_provided.delete_node(new_graph,u)
    return L
            
def legend_example():
    """
    Plot an example with two curves with legends
    """
    
    ERGraph = uERAlgo(1239,0.004)
    UPAGraph = UPAalgo(1239,3)
    computer_nw = alg_application2_provided.load_graph(alg_application2_provided.NETWORK_URL)

    print countedges(ERGraph)
    print countedges(UPAGraph)
    print countedges(computer_nw)

    #deg_dict = compute_degrees(computer_nw)
    #total_deg = (sum(x for x in deg_dict.values()))/1239
    #print total_deg
    xvals = range(0,1240)

    yvals1 = module2.compute_resilience(ERGraph,random_order(ERGraph))
    yvals2 = module2.compute_resilience(UPAGraph,random_order(UPAGraph))
    yvals3 = module2.compute_resilience(computer_nw,random_order(computer_nw))

    #yvals1 = module2.compute_resilience(ERGraph,alg_application2_provided.targeted_order(ERGraph))
    #yvals2 = module2.compute_resilience(UPAGraph,alg_application2_provided.targeted_order(UPAGraph))
    #yvals3 = module2.compute_resilience(computer_nw,alg_application2_provided.targeted_order(computer_nw))

    #yvals1 = module2.compute_resilience(ERGraph,fast_targeted_order(ERGraph))
    #yvals2 = module2.compute_resilience(UPAGraph,fast_targeted_order(UPAGraph))
    #yvals3 = module2.compute_resilience(computer_nw,fast_targeted_order(computer_nw))

    print len(yvals1)
    print len(yvals2)
    print len(yvals3)

       
    plt.xlabel("Number of Nodes Removed")
    plt.ylabel("Size of Largest Connected Component")
    plt.title("Size of Largest Connected Component vs Nodes Removed")
    plt.plot(xvals, yvals1, '-g', label='ERGraph n = 1239,p = 0.004')
    plt.plot(xvals, yvals2, '-r', label='UPAGraph n = 1239, m = 3')
    plt.plot(xvals, yvals3, '-b', label='computer network')
    plt.legend(loc='upper right')
    plt.show()

#legend_example()

def ques3_plot():
    """
    Plot an example with two curves with legends
    """
    target_order = []
    fast_target_order = []

    m = 5
    for n in range(10,1000,10):
        UPAGraph = UPAalgo(n,m)
        start_time = time.time()
        alg_application2_provided.targeted_order(UPAGraph)
        end_time = time.time()
                
        target_order.append(end_time - start_time)

        start_time2 = time.time()
        fast_targeted_order(UPAGraph)
        end_time2 = time.time()
                
        fast_target_order.append(end_time2 - start_time2)

    #print target_order
    #print fast_target_order

    xvals = range(10,1000,10)

    yvals1 = target_order 
    yvals2 = fast_target_order
        
    plt.ylabel("Running times")
    plt.xlabel("No. of Nodes")
    plt.title("Running time vs No. of nodes for UPA graph(Desktop Python)")
    plt.plot(xvals, yvals1, 'b.-', label='Target Order')
    plt.plot(xvals, yvals2, 'r.-', label='Fast Target Order')
    
    plt.legend(loc='upper left')
    plt.show()

ques3_plot()




#ERGraph = uERAlgo(1239,0.004)
#UPAGraph = UPAalgo(1239,3)
#computer_nw = alg_application2_provided.load_graph(alg_application2_provided.NETWORK_URL)

#degreesets(computer_nw)

def ques4_plot():
    """
    Plot an example with two curves with legends
    """
    
    ERGraph = uERAlgo(1239,0.004)
    UPAGraph = UPAalgo(1239,3)
    computer_nw = alg_application2_provided.load_graph(alg_application2_provided.NETWORK_URL)    

    xvals = range(0,1240)

    yvals1 = module2.compute_resilience(ERGraph,alg_application2_provided.targeted_order(ERGraph))
    yvals2 = module2.compute_resilience(UPAGraph,alg_application2_provided.targeted_order(UPAGraph))
    yvals3 = module2.compute_resilience(computer_nw,alg_application2_provided.targeted_order(computer_nw))

    #yvals1 = module2.compute_resilience(ERGraph,fast_targeted_order(ERGraph))
    #yvals2 = module2.compute_resilience(UPAGraph,fast_targeted_order(UPAGraph))
    #yvals3 = module2.compute_resilience(computer_nw,fast_targeted_order(computer_nw))

    
    plt.xlabel("Number of Nodes Removed")
    plt.ylabel("Size of Largest Connected Component")
    plt.title("Size of Largest Connected Component vs Nodes Removed (using Targeted Order)")
    plt.plot(xvals, yvals1, '-g', label='ERGraph n = 1239,p = 0.004')
    plt.plot(xvals, yvals2, '-r', label='UPAGraph n = 1239, m = 3')
    plt.plot(xvals, yvals3, '-b', label='computer network')
    plt.legend(loc='upper right')
    plt.show()

#ques4_plot()