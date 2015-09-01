__author__ = 'spandey2405'

import math,os,sys

def get_pos(graph):
    parents_node = []
    nodes_sucessor = {}
    new_pos = {}
    new_pos["BR"] = (100,100)
    parents_node.append("BR")
    nodes = graph.nodes()
    edges = graph.edges()
    for edge in edges:
        if edge[0] not in parents_node:
            parents_node.append(edge[0])
    for p_node in parents_node:
        no_of_nodes = len(graph.successors(p_node))
        try:
            angel = 360/no_of_nodes
        except:
            angel = 0

        count = 1
        for edge in edges:
            if edge[0] == p_node:

                try:
                    p_x = new_pos[p_node][0]

                    p_y = new_pos[p_node][1]

                except:
                    print("Unwanted Routes")

                    sys.exit(0)
                try :
                    ppx = float(new_pos[graph.predecessors(p_node)[0]][1])
                    ppy = float(new_pos[graph.predecessors(p_node)[0]][0])
                    d_y = p_y - ppx
                    d_x = p_x - ppy

                    angel = math.degrees(math.atan2(d_y,d_x)) + ((count-1) *15)
                    x = p_x + 30 * math.cos(math.radians(angel))
                    y = p_y + 30 * math.sin(math.radians(angel))

                except IndexError:
                    node_angel = angel * count
                    node_angel = math.radians(node_angel)
                    y = p_y + 30 * math.sin(node_angel)
                    x = p_x + 30 * math.cos(node_angel)

                new_pos[edge[1]]= (x,y)
                count = count + 1

    return new_pos

