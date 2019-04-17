#!/usr/local/bin/python3
import os
from random import randint
import pprint


class Node():
    def __init__(self,id):
        self.id = id
        self.value = None
        self.color = None
        self.coord = (0,0)
        self.visited = False
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        a = self.id
        b = self.value
        c = self.color
        d = self.coord
        e = self.visited
        return "[id:{},value:{},color:{},coord:{},visited:{}]".format(a,b,c,d,e)


class Graph():
    def __init__(self):
        self.graph = {}
        self.nodes = {}
        self.node_count = 0
        self.edge_count = 0

    def __str__(self):
        out = ''
        for g in self.graph:
            out = out + self.nodes[g].__str__() + "\n"
            for n in self.graph[g]:
                out = out + "\t" +n.__str__() + "\n"
        return out

    def add_node(self,node):
        """
        Add a node to a graph
        Params:
            node [Node]: node info
        """
        if not node.id in self.nodes:
            self.nodes[node.id] = node

        self.node_count = len(self.nodes)

    def add_edge(self,start_id,end_id,direction=1):
        """
        Add an edge to a node.
        Params:
            neighbor_id [int]: unique if of neighbor node
            direction [int]: (1,2) 1 = one way (away) 2 = bidirectional
        """

        if not start_id in self.graph:
            self.graph[start_id] = []

        if end_id in self.graph[start_id]:
            print("edge {} exists at node {}".format(end_id,start_id))
        else:
            self.graph[start_id].append(end_id)

        if direction == 2:
            if not start_id in self.graph:
                self.graph[start_id] = []

            if start_id in self.graph[end_id]:
                print("edge {} exists at node {}".format(start_id,end_id))
            else:
                self.graph[end_id].append(start_id)

        

if __name__=='__main__':
    g = Graph()

    for i in range(100):
        n = Node(i)
        g.add_node(n)
    
    for i in range(150):
        s = randint(0,g.node_count-1)

        e = s
        while e == s:
            e = randint(0,g.node_count-1)

        g.add_edge(s,e)

    print(g)



    


