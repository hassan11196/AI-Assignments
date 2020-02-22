import matplotlib.pyplot as plt
import copy
import sys
import numpy as np


def _get_node_collection_object(G):
    fig = plt.gcf()
    axes = plt.gca()
    no_of_nodes = G.number_of_nodes()
    nodes_collection = axes.get_children()[no_of_nodes + 2]
    return fig, axes, no_of_nodes, nodes_collection


def _get_values_from_kwargs(dic, string):
    try:
        node = dic['node']
    except KeyError:
        node = None
    try:
        value = dic['string']
    except KeyError:
        print(string + "argument required")
        sys.exit(0)
    return node, value


def set_node_position(G, **kwargs):
    """
    Moves node to position along with its edges.
    Parameters
    ----------
    G        : Graph whose nodes are to be moved
    kwargs
    ------
    node     : The node to move if not specified moves all the nodes to the
               corresponding position in position
    position : The new position of the node. If node specified should be in
               form (x,y) or [x,y]. If node not specified should be in form
               [(x1,y1), (x2,y2), (x3,y3)]. It must have new position for
               each node in the graph.
    Example
    -------
    set_node_position(G, node=1, position=[0.5, 0.5])
    set_node_position(G, node=1, position=(0.5, 0.5))
    #Considering graph G has 3 nodes
    set_node_position(G, position=[(0.1,0.1), (0.2, 0.2), (0.3, 0.3)]
    """
    try:
        node = kwargs['node']
    except KeyError:
        node = None
    try:
        position = kwargs['position']
    except KeyError:
        print("postion argument required")
        sys.exit(0)

    if node:
        _set_single_node_position(G, node=node, position=position)
    else:
        for node_no in range(G.number_of_nodes()):
            _set_single_node_position(G, node=G.nodes()[node_no],
                                      position=position[node_no])


def _set_single_node_position(G, **kwargs):
    """
    Moves a single node specified in node to the specified position.
    """
    try:
        node = kwargs['node']
    except KeyError:
        node = None
    try:
        position = kwargs['position']
    except KeyError:
        print("position argument required")
        sys.exit(0)

    fig = plt.gcf()
    axes = plt.gca()
    node_index = G.nodes().index(node)
    no_of_nodes = G.number_of_nodes()

    def compare(li1, li2):
        for i, j in zip(li1, li2):
            if i != j:
                return False
        return True

    if node:
        # move node
        x, y = position
        nodes_collection = axes.get_children()[no_of_nodes + 2]
        prev_positions = nodes_collection.get_offsets()
        prev_position = copy.deepcopy(prev_positions[node_index])
        prev_positions[node_index] = [x, y]

        # move edge
        edges_collection = axes.get_children()[no_of_nodes + 3]
        for edge in edges_collection.get_paths():
            if compare(edge.vertices[0], prev_position):
                edge.vertices[0] = position
            elif compare(edge.vertices[1], prev_position):
                edge.vertices[1] = position

        # move label
        label = axes.get_children()[node_index + 2]
        label.set_position([x, y])

    plt.draw()


def set_node_facecolor(G, **kwargs):
    """
    Changes node's facecolor
    Parameters
    ----------
    G     : Graph whose node's facecolor needs to be changed
    kwargs
    ------
    node  : The node whose facecolor needs to be changed. If node not specified
            and only one color is specified changes all the nodes to that
            facecolor. If node not specified and color is a list or tuple of
            colors, each node will be changed to its corresponding color.
    color : Can be a single value of a list of colors.
    The following color abbreviations are supported:
    ==========  ========
    character   color
    ==========  ========
    'b'         blue
    'g'         green
    'r'         red
    'c'         cyan
    'm'         magenta
    'y'         yellow
    'k'         black
    'w'         white
    ==========  ========
    Examples:
    set_node_facecolor(G, node=1, color='b')
    set_node_facecolor(G, node=1, color=['b'])
    set_node_facecolor(G, color=['r', 'b', 'g', 'y', 'm', 'k', 'c'])
    set_node_facecolor(G, color='b')
    set_node_facecolor(G, color=('b'))
    """
    try:
        node = kwargs['node']
    except KeyError:
        node = None
    try:
        color = kwargs['color']
    except KeyError:
        print("color argument required")
        sys.exit(0)

    if (isinstance(color, list) or isinstance(color, tuple)) and \
            len(color) == 1:
        color = color[0]

    same_colors = {'blue': 'b',
                   'green': 'g',
                   'red': 'r',
                   'cyan': 'c',
                   'magenta': 'm',
                   'yellow': 'y',
                   'black': 'k',
                   'white': 'w'}

    if isinstance(color, str) and len(color) != 1:
        color = same_colors[color]

    colors_dict = {'b': (0.,    0.,    1.,  1.),
                   'g': (0.,    0.5,   0.,  1.),
                   'r': (1.,    0.,    0.,  1.),
                   'c': (0.,    0.75,  0.75,  1.),
                   'm': (0.75,  0.,    0.75,  1.),
                   'y': (0.75,  0.75,  0.,  1.),
                   'k': (0.,    0.,    0.,  1.),
                   'w': (1.,    1.,    1.,  1.)}

    fig = plt.gcf()
    axes = plt.gca()
    no_of_nodes = G.number_of_nodes()
    nodes_collection = axes.get_children()[no_of_nodes + 2]

    # if node is specified manually changing the facecolor array
    # so that the colors for other nodes are retained
    if node:
        node_index = G.nodes().index(node)
        facecolor_array = nodes_collection.get_facecolor().tolist()
        facecolor_array = [tuple(x) for x in facecolor_array]
        if len(facecolor_array) == 1:
            facecolor_array = [copy.deepcopy(facecolor_array[0])
                               for i in range(no_of_nodes)]
        facecolor_array[node_index] = colors_dict[color]
        nodes_collection.set_facecolor(facecolor_array)

    # if node not specified call the matplotlib's set_facecolor function
    else:
        nodes_collection.set_facecolor(color)

    plt.draw()


def set_node_edgecolor(G, **kwargs):
    """
    Changes node edgecolors
    Parameters
    ----------
    G     : Graph whose node's edgecolor needs to be changed
    kwargs
    ------
    node  : The node whose edgecolor needs to be changed. If node not specified
            and only one color is specified changes all the nodes to that
            color. If node not specified and color is a list or tuple of
            colors, each node will be changed to its corresponding color.
    color : Can be a single value of a list of colors.
    The following color abbreviations are supported:
    ==========  ========
    character   color
    ==========  ========
    'b'         blue
    'g'         green
    'r'         red
    'c'         cyan
    'm'         magenta
    'y'         yellow
    'k'         black
    'w'         white
    ==========  ========
    Examples:
    set_node_edgecolor(G, node=1, color='b')
    set_node_edgecolor(G, node=1, color=['b'])
    set_node_edgecolor(G, color=['r', 'b', 'g', 'y', 'm', 'k', 'c'])
    set_node_edgecolor(G, color='b')
    set_node_edgecolor(G, color=('b'))
    """
    try:
        node = kwargs['node']
    except KeyError:
        node = None
    try:
        color = kwargs['color']
    except KeyError:
        print("color argument required")
        sys.exit(0)

    if (isinstance(color, list) or isinstance(color, tuple)) and \
            len(color) == 1:
        color = color[0]

    same_colors = {'blue': 'b',
                   'green': 'g',
                   'red': 'r',
                   'cyan': 'c',
                   'magenta': 'm',
                   'yellow': 'y',
                   'black': 'k',
                   'white': 'w'}

    if isinstance(color, str) and len(color) != 1:
        color = same_colors[color]

    colors_dict = {'b': (0.,    0.,    1.,  1.),
                   'g': (0.,    0.5,   0.,  1.),
                   'r': (1.,    0.,    0.,  1.),
                   'c': (0.,    0.75,  0.75,  1.),
                   'm': (0.75,  0.,    0.75,  1.),
                   'y': (0.75,  0.75,  0.,  1.),
                   'k': (0.,    0.,    0.,  1.),
                   'w': (1.,    1.,    1.,  1.)}

    fig = plt.gcf()
    axes = plt.gca()
    no_of_nodes = G.number_of_nodes()
    nodes_collection = axes.get_children()[no_of_nodes + 2]

    # if node is specified manually changing the edgecolor array
    # so that the colors for other nodes are retained
    if node:
        node_index = G.nodes().index(node)
        edgecolor_array = nodes_collection.get_edgecolor().tolist()
        edgecolor_array = [tuple(x) for x in edgecolor_array]
        if len(edgecolor_array) == 1:
            edgecolor_array = [copy.deepcopy(edgecolor_array[0])
                               for i in range(no_of_nodes)]
        edgecolor_array[node_index] = colors_dict[color]
        nodes_collection.set_edgecolor(edgecolor_array)

    # if node not specified call the matplotlib's set_edgecolor function
    else:
        nodes_collection.set_edgecolor(color)

    plt.draw()


def set_node_color(G, **kwargs):
    """
    Changes node colors
    Parameters
    ----------
    G     : Graph whose node's color needs to be changed
    kwargs
    ------
    node  : The node whose color needs to be changed. If node not specified
            and only one color is specified changes all the nodes to that
            color. If node not specified and color is a list or tuple of
            colors, each node will be changed to its corresponding color.
    color : Can be a single value of a list of colors.
    The following color abbreviations are supported:
    ==========  ========
    character   color
    ==========  ========
    'b'         blue
    'g'         green
    'r'         red
    'c'         cyan
    'm'         magenta
    'y'         yellow
    'k'         black
    'w'         white
    ==========  ========
    Examples:
    set_node_color(G, node=1, color='b')
    set_node_color(G, node=1, color=['b'])
    set_node_color(G, color=['r', 'b', 'g', 'y', 'm', 'k', 'c'])
    set_node_color(G, color='b')
    set_node_color(G, color=('b'))
    """
    try:
        node = kwargs['node']
    except KeyError:
        node = None
    try:
        color = kwargs['color']
    except KeyError:
        print("color argument required")
        sys.exit(0)

    if (isinstance(color, list) or isinstance(color, tuple)) and \
            len(color) == 1:
        color = color[0]

    same_colors = {'blue': 'b',
                   'green': 'g',
                   'red': 'r',
                   'cyan': 'c',
                   'magenta': 'm',
                   'yellow': 'y',
                   'black': 'k',
                   'white': 'w'}

    if isinstance(color, str) and len(color) != 1:
        color = same_colors[color]

    fig = plt.gcf()
    axes = plt.gca()
    no_of_nodes = G.number_of_nodes()
    nodes_collection = axes.get_children()[no_of_nodes + 2]
    if node:
        set_node_facecolor(G, **kwargs)
        set_node_edgecolor(G, **kwargs)
    else:
        nodes_collection.set_color(color)

    plt.draw()


def set_node_size(G, **kwargs):
    """
    Change node size
    Parameters
    ----------
    G    : The graph whose nodes are to be resized
    kwargs
    ------
    node : The node whose size is to be changed. If node not specified size
           of all the nodes will be changed.
    size : If size is an int and node specified, that node's size would be
           changed. If size is a list of tuple and no node specified each
           node will be changed to it's corresponding size. If node not
           specified and size is int all the nodes will be changed to that
           value.
    Examples
    --------
    set_node_size(G, node=1, size=10)
    set_node_size(G, size=5)
    set_node_size(G, size=[1,2,3,4,5,6,7])
    """
    try:
        node = kwargs['node']
    except KeyError:
        node = None
    try:
        size = kwargs['size']
    except KeyError:
        print("size argument required")
        sys.exit(0)

    fig = plt.gcf()
    axes = plt.gca()
    no_of_nodes = G.number_of_nodes()
    nodes_collection = axes.get_children()[no_of_nodes + 2]

    if node:
        node_index = G.nodes().index(node)
        line_width_arr = nodes_collection.get_linewidth()
        if len(line_width_arr) == 1:
            element = line_width_arr[0]
            line_width_arr = [copy.deepcopy(element)
                              for i in range(no_of_nodes)]
        line_width_arr[node_index] = size
        nodes_collection.set_linewidth(line_width_arr)

    else:
        nodes_collection.set_linewidth(size)

    plt.draw()


def set_node_style(G, **kwargs):
    try:
        node = kwargs['node']
    except KeyError:
        node = None
    try:
        style = kwargs['position']
    except KeyError:
        print("style argument required")
        sys.exit(0)

    fig = plt.gcf()
    axes = plt.gca()
    no_of_nodes = G.number_of_nodes()
    nodes_collection = axes.get_children()[no_of_nodes + 2]

    linestyle_dict = {'solid':   (None, None),
                      'dotted':  (0, (1.0, 3.0)),
                      'dashdot': (0, (3.0, 5.0, 1.0, 5.0))}
    # TODO: Still incomplete Check what does the tuple values do


def set_node_alpha(G, alpha):
    fig = plt.gcf()
    axes = plt.gca()
    no_of_nodes = G.number_of_nodes()
    nodes_collection = axes.get_children()[no_of_nodes + 2]

    nodes_collection.set_alpha(alpha)
    plt.draw()

# TODO set_edge_style


def set_edge_color(G, **kwargs):
    """
    Change the color of the edges
    Parameters
    ----------
    G    : The graph whose edges color are to be changed.
    kwargs
    ------
    edge : The edge whose color is to be changed. If edge
           not specified and a single color value is given
           all the edges are changed to the specified color.
           If edge not given and color list is given the
           color of the corresponding edge is changed. The
           order of the edges can be seen from G.edges()
    color: Color value. Either a list of a single value
    Examples
    --------
    set_edge_color(G, edge=(1,2), color='g')
    set_edge_color(G, color='b')
    """
    try:
        edge = kwargs['edge']
    except KeyError:
        edge = None
    try:
        color = kwargs['color']
    except KeyError:
        print("color argument required")
        sys.exit(0)

    if (isinstance(color, list) or isinstance(color, tuple)) and \
            len(color) == 1:
        color = color[0]

    same_colors = {'blue': 'b',
                   'green': 'g',
                   'red': 'r',
                   'cyan': 'c',
                   'magenta': 'm',
                   'yellow': 'y',
                   'black': 'k',
                   'white': 'w'}

    if isinstance(color, str) and len(color) != 1:
        color = same_colors[color]

    colors_dict = {'b': (0.,    0.,    1.,  1.),
                   'g': (0.,    0.5,   0.,  1.),
                   'r': (1.,    0.,    0.,  1.),
                   'c': (0.,    0.75,  0.75,  1.),
                   'm': (0.75,  0.,    0.75,  1.),
                   'y': (0.75,  0.75,  0.,  1.),
                   'k': (0.,    0.,    0.,  1.),
                   'w': (1.,    1.,    1.,  1.)}

    fig = plt.gcf()
    axes = plt.gca()
    no_of_nodes = G.number_of_nodes()
    no_of_edges = G.number_of_edges()
    edges_collection = axes.get_children()[no_of_nodes + 3]
    edges = G.edges()

    if edge:
        edge_index = edges.indexof(edge)
        edgecolor_array = edges_collection.get_color().tolist()
        edgecolor_array = [tuple(x) for x in edgecolor_array]
        if len(edgecolor_array) == 1:
            edgecolor_array = [copy.deepcopy(edgecolor_array[0])
                               for i in range(no_of_edges)]
        edgecolor_array[edge_index] = colors_dict[color]
        edges_collection.set_facecolor(edgecolor_array)
    else:
        edges_collection.set_color(color)

    plt.draw()


def set_edge_linewidth(G, **kwargs):
    """
    Change the linewidth of the edges.
    parameters
    ----------
    G    : The graph whose edge widths are to be changed.
    kwargs
    ------
    edge : The edge whose width is to be changed. If edge
           not specified and a single width value is given
           all the edges are changed to the specified width.
           If edge not given and edge list is given the
           width of the corresponding edge is changed. The
           order of the edges can be seen from G.edges()
    width: Width value. Either a list of a single value
    Example
    -------
    set_edge_linewidth(G, edge=(1,2), width=4)
    set_edge_linewidth(G, width=(1, 2, 3, 4, 5, 6))
    """
    try:
        edge = kwargs['edge']
    except KeyError:
        edge = None
    try:
        linewidth = kwargs['width']
    except KeyError:
        print("width argument required")

    fig = plt.gcf()
    axes = plt.gca()
    no_of_nodes = G.number_of_nodes()
    no_of_edges = G.number_of_edges()
    edges_collection = axes.get_children()[no_of_nodes + 3]
    edges = G.edges()

    if edge:
        current_linewidth = edges_collection.get_linewidth()
        edge_index = edges.indexof(edge)
        if len(current_linewidth) == 1:
            current_linewidth = [copy.deepcopy(current_linewidth[0])
                                 for i in range(no_of_edges)]
        current_linewidth[edge_index] = linewidth
    else:
        edges_collection.set_linewidth(linewidth)

    plt.draw()


def set_edge_alpha(G, **kwargs):
    """
    Example
    -------
    set_edge_alpha(G, alpha=0)
    """
    try:
        edge = kwargs['edge']
    except KeyError:
        edge = None
    try:
        alpha = kwargs['alpha']
    except KeyError:
        print("alpha argument required")

    fig = plt.gcf()
    axes = plt.gca()
    no_of_nodes = G.number_of_nodes()
    edges_collection = axes.get_children()[no_of_nodes + 3]
    edges_collection.set_linewidth(alpha)

    plt.draw()