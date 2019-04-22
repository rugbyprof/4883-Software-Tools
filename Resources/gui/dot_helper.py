#!/usr/local/bin/python3
import os
from random import randint
import pprint
from math import sqrt
from math import pow
from math import atan2,degrees



class Node():
    """
    Represents a node in a graph.

    nid     [int]         : unique identifier
    value   [any]         : some value to associate with node
    color   [tuple,string]: (r,g,b) , '#FFFFFF'
    coord   [tuple]       : (x,y)
    cell    [tuple]       : (col,row)
    visited [bool]        : True = visited
    size    [int]         : size of ellipse in pixels 
    """
    def __init__(self,**kwargs):
        if 'nid' in kwargs:
            self.nid = kwargs['nid']
        else:
            self.nid = randint()

        if 'value' in kwargs:
            self.value = kwargs['value']
        else:
            self.value = None

        if 'color' in kwargs:
            self.color = kwargs['color']
        else:
            self.color = None

        if 'coord' in kwargs:
            self.coord = kwargs['coord']
        else:
            self.coord = None

        if 'size' in kwargs:
            self.size = kwargs['size']
        else:
            self.size = 3
        
        if 'cell' in kwargs:
            self.cell = kwargs['cell']
        else:
            self.cell = None        

        self.visited = False
    
    def __repr__(self):
        """
        calls __str__ but should be slightly different (look up docs)
        """
        return self.__str__()

    def __str__(self):
        """
        print class representation as readable string
        """
        a = self.nid
        b = self.value
        c = self.color
        d = self.coord
        e = self.visited
        f = self.cell
        return "[nid:{},value:{},color:{},coord:{},visited:{},cell:{}]".format(a,b,c,d,e,f)


class Graph():
    """
    Dictionary based representation of a graph
    graph       [dict]: node id as dict key points to list with neighbor ids
    nodes       [dict]: dict of nodes, used to hold node info
    node_count  [int]: :)
    edge_count  [int]: :)
    """
    def __init__(self):
        self.graph = {}
        self.nodes = {}
        self.node_count = 0
        self.edge_count = 0


    def add_node(self,**kwargs):
        """
        Add a node to a graph
        Params:
            kwargs [dict]: dictionary holding node info (see Node)
        Returns: 
            [bool]: True = success
        """

        if 'node' in kwargs:
            node = kwargs['node']
        else:
            node = Node(**kwargs)

        if not node.nid in self.nodes:
            self.nodes[node.nid] = node
            self.graph[node.nid] = []

            self.node_count = len(self.nodes)
            return True
        return False

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

    def __str__(self):
        """
        print class representation as readable string
        """
        out = ''
        for g in self.graph:
            out = out + self.nodes[g].__str__() + "\n"
            for n in self.graph[g]:
                out = out + "\t" +n.__str__() + "\n"
        return out

    def __repr__(self):
        """
        calls __str__ but should be slightly different (look up docs)
        """
        return self.__str__()

class sqauresBoard(Graph):
    """
    Represents a squares board game.
    
    players     [list]: list of player identifiers
    width       [int]: width of game board
    height      [int]: height of game board
    gap         [int]: space between "dots" or square size
    gutter      [int]: buffer between game edge and dots (squares)
    dot_size    [int]: size of dots
    dot_color   [tuple,string]: (r,g,b) , '#FFFFFF'
    """
    def __init__(self,**kwargs):
        super().__init__()

        if 'players' in kwargs:
            self.players = kwargs['players']
        else:
            self.players = []

        if 'width' in kwargs:
            self.width = kwargs['width']
        else:
            self.width = 500

        if 'height' in kwargs:
            self.height = kwargs['height']
        else:
            self.height = None

        if 'gap' in kwargs:
            self.gap = kwargs['gap']
        else:
            self.gap = 10

        if 'gutter' in kwargs:
            self.gutter = kwargs['gutter']
        else:
            self.gutter = 10

        if 'dot_size' in kwargs:
            self.dot_size = kwargs['dot_size']
        else:
            self.dot_size = 3

        if 'dot_color' in kwargs:
            self.dot_color = kwargs['dot_color']
        else:
            self.dot_color = (255,0,0)

        # if (self.width - self.gutter*2) % self.gap != 0:
        #     raise Exception("width - gutter is not divisible by gap!")

        # if (self.height - self.gutter*2) % self.gap != 0:
        #     raise Exception("width - gutter is not divisible by gap!")

        self.generateSquares()

    def generateSquares(self):
        """
        Using a "graph" representation create nodes with x,y coords that when printed 
        will look to be "dots" aligned like the dot game.
        """
        self.cols = int((self.width) / self.gap)
        self.rows = int((self.height) / self.gap)

        x = self.gutter 
        y = self.gutter

        i = 0
        for r in range(self.rows):
            for c in range(self.cols):
                self.add_node(nid=i,
                              coord=(x,y),
                              cell=(c,r),
                              size=self.dot_size,
                              color=self.dot_color)
                i += 1
                x += self.gap
            x = self.gutter
            y += self.gap

    def select_edge(self,cx,cy):
        """
        Start by finding upper left node that click was closest to. 
        Params:
            cx [int]: clicked x
            cy [int]: clicked y
        Returns:
            success [bool]: true if edge found
        """
        #closest = self.__find_node(cx,cy)
        closest_node = self.__closest_node(cx,cy)
        nx,ny = closest_node.coord
        angle = self.__angle(cx,cy,nx,ny)

        print("closest_node:{} angle:{}".format(closest_node,angle))

        if closest_node != None:
            connect_to = self.__pick_edge(closest_node,angle)
            print("connect_to: {}".format(connect_to))
            if connect_to != None:
                self.add_edge(closest_node.nid,connect_to,2)

    def __pick_edge(self,node,angle):
        """
        Find correct clicked edge based angle to node.
        Params:
        node [Node]: the node we clicked close to
        angle[float]: 0=N 90=E 180=S 270=W 360=N
        """

        print("cell:{}".format(node.cell))

        col,row = node.cell

        neighbor = None

        if angle >= 70 and angle <= 110:
            neighbor = node.nid + 1
        elif angle >= 160 and angle <= 200:
            neighbor = node.nid + self.cols
        elif angle >= 250 and angle <= 290:
            neighbor = node.nid - 1
        elif angle >= 340 or angle <= 20:
            neighbor = node.nid - self.cols

        if neighbor != None:
            if neighbor >= 0 and neighbor <= self.rows*self.cols-1:
                return neighbor

        return None

    def __angle(self,x1,y1,x2,y2):
        """
        Gives the angle of click relative to closest "node" (dot) on the game board.
        Used to figure out which "edge" to select on square.
        """
        xDiff = x2 - x1
        yDiff = y2 - y1
        d = degrees(atan2(yDiff, xDiff)) - 90
        # negative values were not what I expected so I adjusted so
        # North = 0,360, East = 90, South = 180, West = 270
        if d < 0.0:
            d = 270.0 - abs(d) + 90
        return round(d)

    def __find_node(self,cx,cy):
        """
        Finds node (cell) based on x,y.
        Params:
            cx [int]:  x coord
            cy [int]:  y coord
        Returns:
            success [Node]: returns node if found None otherwise.
        """
        
        for nid,node in self.nodes.items():
            nx,ny = node.coord
            if abs(cx-nx) < self.gap and cx >= nx:
                if abs(cy-ny) < self.gap and cy >= ny:
                    return node

        return None
    
    def __closest_node(self,cx,cy):
        """
        Finds closest node (cell) based on cx,cy.
        Params:
            cx [int]:  x coord
            cy [int]:  y coord
        Returns:
            success [int]: true if cell found
        """ 
        closest = pow(2.0,20)
        closest_node = None

        for nid,node in self.nodes.items():
            nx,ny = node.coord
            d = sqrt(pow(float(cx-nx),2.0) + pow(float(cy-ny),2.0))
            if d < closest:
                closest = d
                closest_node = node
        
        #print("closest:{},nid:{}".format(closest,closest_node.nid))

        return closest_node


    def __str__(self):
        out = ''
        for g in self.graph:
            out = out + self.nodes[g].__str__() + "\n"
            for n in self.graph[g]:
                out = out + "\t" +n.__str__() + "\n"
        return out

    def __repr__(self):
        return self.__str__()


if __name__=='__main__':
    g = Graph()

    for nid in range(100):
        n = Node(nid=nid,color=(13,99,100),coord=(99,88))
        g.add_node(node=n)
    
    for i in range(150):
        s = randint(0,g.node_count-1)

        e = s
        while e == s:
            e = randint(0,g.node_count-1)

        g.add_edge(s,e)
    

    board = sqauresBoard(players=['terry','dax'],width=400,height=400,gap=20)
    print(board.graph)




    


