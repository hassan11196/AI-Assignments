import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update_line(num, data, line):
    line.set_data(data[..., :num])
    return line,

    
g = nx.Graph()
# pos = nx.spring_layout(g)  

g.add_edge('Oradea', 'Zerind', weight=71)
g.add_edge('Oradea', 'Sibiu', weight=151)
g.add_edge('Zerind', 'Arad', weight=75)
g.add_edge('Arad', 'Sibiu', weight=140)
g.add_edge('Arad', 'Timisoara', weight=118)
g.add_edge('Timisoara', 'Lugoj', weight=111)
g.add_edge('Lugoj', 'Mehadia', weight=70)
g.add_edge('Mehadia', 'Drobeta', weight=75)
g.add_edge('Drobeta', 'Craiova', weight=120)
g.add_edge('Sibiu', 'Fagaras', weight=99)
g.add_edge('Sibiu', 'Rimnicu Vilcea', weight=80)
g.add_edge('Rimnicu Vilcea', 'Craiova', weight=146)
g.add_edge('Craiova', 'Pitesti', weight=138)
g.add_edge('Rimnicu Vilcea', 'Pitesti', weight=97)
g.add_edge('Fagaras', 'Bucharest', weight=211)
g.add_edge('Pitesti', 'Bucharest', weight=101)
g.add_edge('Bucharest', 'Urziceni', weight=85)
g.add_edge('Bucharest', 'Giurgiu', weight=90)
g.add_edge('Urziceni', 'Hirsova', weight=98)
g.add_edge('Hirsova', 'Eforie', weight=86)
g.add_edge('Urziceni', 'Vaslui', weight=92)
g.add_edge('Vaslui', 'Lasi', weight=92)
g.add_edge('Lasi', 'Nearmt', weight=87)


# nx.set_node_attributes(g, {'a':{'visited':True},'b':{'visited':False}, 'c':{'visited':True}, 'd':{'visited':False}, 'e':{'visited':False}, 'f':{'visited':True}})

# for i in range(0,4):
#     edge_colors = ['blue' if g.nodes[e[0]]['visited'] == True else 'black' for e in g.edges]
#     nx.draw(g, with_labels=True, font_weight='bold', edge_color=edge_colors)
#     plt.show()
#     g.add_edge('f', 'b', weight=1)
# n = g.neighbors('b')
# print([x for x in n])

nx.draw(g, with_labels=True, font_weight='bold')
plt.show()
