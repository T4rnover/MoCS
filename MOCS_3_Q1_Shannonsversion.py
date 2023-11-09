"""
Created on Wed Oct 25 11:53:08 2023

@author: Carlson and O'Connor
"""
import networkx as nx
import matplotlib.pyplot as plt

# Set up the parameters for the cascade model
N = 10  # Number of nodes
p = 0.50  # Probability of edge creation

def plot_directed_graph(G):
    pos = nx.spring_layout(G, k=3)
    nx.draw_networkx(G, pos=pos, with_labels=True)

# Create the undirected graph using the Erdos-Renyi model
#this will make it directed such that every node has bidirectional connection w its neighbors
#we want unidirectional connections, such that j < i 
#so we will remove nodes where j>i
G = nx.erdos_renyi_graph(N, p, directed=True)

#see our initial graph
plot_directed_graph(G)

#our initial graph edges, we have some bidirectional connections but we only want unidirectional
G.edges()

#remove edges that go from a lower num node to a higher num node
#so now we should only have edges running from higher num node to lower
#and all edges should be unidirectional
G.remove_edges_from([(i, j) for i in range(N) for j in range(N) if i < j])

#check
G.edges()

# Test if the graph is acyclic
if nx.is_directed_acyclic_graph(G):
    print("The graph is acyclic.")
else:
    print("The graph contains at least one cycle.")

#Calculate the average in-degree and out-degree of the graph
avg_in_degree = nx.average_degree_connectivity(G)
avg_out_degree = nx.average_degree_connectivity(G, source='out')
 
print("The average in-degree of the graph is:", avg_in_degree)
print("The average out-degree of the graph is:", avg_out_degree)

# Calculate the expected number of edges that run from all nodes in the graph
expected_edges = 0
for i in range(N):
    ni = G.degree(i)
    expected_edges += (ni * (N - ni - 1)) / 2
print("The expected number of edges that run from all nodes in the graph is:", expected_edges)

# Plot the directed graph
def plot_directed_graph(G):
    pos = nx.spring_layout(G, k=3)
    nx.draw_networkx(G, pos=pos, with_labels=True)
    plt.show()

plot_directed_graph(G)



    
