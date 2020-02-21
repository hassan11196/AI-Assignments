import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,

    
g = nx.Graph()
pos = nx.spring_layout(g)  
g.add_edge('a', 'b', weight=2)
g.add_edge('b', 'c', weight=1)
g.add_edge('c', 'd', weight=2)
g.add_edge('e', 'b', weight=1)
g.add_edge('d', 'e', weight=4)

print(g['b'])

for i in range(0,4):
    edge_colors = ['blue' if g.degree[e[0]] == i else 'black' for e in g.edges]
    nx.draw(g, with_labels=True, font_weight='bold', edge_color=edge_colors)
    plt.show()
    ans = input()
    g.add_edge('f', 'b', weight=1)
# n = g.neighbors('b')
# print([x for x in n])
