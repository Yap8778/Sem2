#Task 3
#Import network library
import networkx as nx

#Define the edge of each nodes
adjacency_dict_graph1 = {'A': ('B','F','J'), 'B': ('H','I','G','A'), 'C': ('F','E','J','G'),'D': ('F','I','J'),'E': ('H','C','G'),'F':('D','A','C'),'G': ('B','C','E'),
                         'H': ('B','E','I'),'I': ('H','D','B'),'J': ('D','A','C')}

#Create a Graph dict mapping nodes
H = nx.Graph(adjacency_dict_graph1)

#Import diagram
import matplotlib.pyplot as plt
#Using the nx to draw the diagram
print("This is the Figure 1:")
nx.draw(H, with_labels=True,edge_color='grey')
plt.show()

#Define the edge of each nodes
adjacency_dict_graph2 = {'A': ('B','C','D'), 'B': ('H','E','G','A'), 'C': ('A'),'D': ('A','I','J','F'),'E': ('B'),'F': ('D'),'G': ('B'),'H': ('B'),'I': ('D'),'J': ('D')}

#Create a Graph dict mapping nodes
G = nx.Graph(adjacency_dict_graph2)

#Using the nx to draw the diagram
print("\nThis is the Figure 2:")
nx.draw(G, with_labels=True,edge_color='blue')
plt.show()

#Calculate the average clustering
#https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.approximation.clustering_coefficient.average_clustering.html#networkx.algorithms.approximation.clustering_coefficient.average_clustering
clutering_graph1 = nx.average_clustering(H)
clutering_graph2 = nx.average_clustering(G)
print(f"This is the clustering of graph 1: {clutering_graph1}.")
print(f"This is the clustering of graph 2: {clutering_graph2}.")
print("")

#Find the center node
#https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.distance_measures.center.html#networkx.algorithms.distance_measures.center
center_graph1 = nx.center(H)
center_graph2 = nx.center(G)
print(f"This is the center for graph 1: {center_graph1}.")
print(f"This is the center for graph 2: {center_graph2}.")
print("")

#Define the graph is a tree or not
#https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.recognition.is_tree.html#networkx.algorithms.tree.recognition.is_tree
tree_graph1 = nx.is_tree(H)
tree_graph2 = nx.is_tree(G)
print(f"Grap 1 is a tree?\n{tree_graph1}.")
print("")
print(f"Grap 2 is a tree?\n{tree_graph2}.")
