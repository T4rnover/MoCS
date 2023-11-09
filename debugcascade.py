import networkx as nx
import matplotlib.pyplot as plt

def analyze_graph(N, p):
    # Create the undirected graph using the Erdos-Renyi model
    G = nx.erdos_renyi_graph(N, p)

    # Add directed edges to the graph using list comprehension
    G.add_edges_from([(i, j) for i in range(1, N) for j in range(i) if G.has_edge(j, i)])

    # Test if the graph is acyclic
    if nx.is_directed_acyclic_graph(G):
        print("The graph is acyclic.")
    else:
        print("The graph contains at least one cycle.")

    # Calculate the average in-degree and out-degree of the graph
    avg_in_degree = nx.average_degree_connectivity(G)
    avg_out_degree = nx.average_degree_connectivity(G, source='out')

    print("The average in-degree of the graph is:", avg_in_degree)
    print("The average out-degree of the graph is:", avg_out_degree)

    # Calculate the expected number of edges from nodes i' > i to nodes i' ≤ i
    for i in range(1, N):
        expected_edges = (N - i) * i * p
        avg_out_degree = sum(nx.average_degree_connectivity(G, source='out').values()) / N
        ni = avg_out_degree * N
        expected_edges2 = (ni - i**2) * p
        if expected_edges == expected_edges2:
            print("The expected number of edges from nodes i' > i to nodes i' ≤ i is:", expected_edges)
            print("The result is equal to (ni − i^2)p.")
        else:
            print("The expected number of edges from nodes i' > i to nodes i' ≤ i is:", expected_edges)
            print("The result is not equal to (ni − i^2)p.")

    # Plot the directed graph
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos=pos, with_labels=True)
    plt.show()

# Set up the parameters for the cascade model
N = 10  # Number of nodes
p = 0.5  # Probability of edge creation

analyze_graph(N, p)

