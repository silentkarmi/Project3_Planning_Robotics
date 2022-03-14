#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from ast import Constant
from dataclasses import dataclass
import math

from constants import CONSTANT

@dataclass
class Node:
    ACTION_SET = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
    
    coord: tuple()
    cost2come: int = 0
    cost2go: int = 0
    
    def __init__(self, coord, parent):
        self.coord = coord
        self.parentNode = parent
        self.cost2come = 0
        self.cost2go = 0
        self.calculateCost2Go()
        
    def __lt__(self, other):
        return self.cost2come + self.cost2go < other.cost2come + other.cost2go
        
    def __le__(self, other):
        return self.cost2come + self.cost2go <= other.cost2come + other.cost2go
    
    def calculateCost2Go(self):
        x, y = self.coord
        x1, y1 = CONSTANT.GOAL_NODE
        
        self.cost2go = round(math.sqrt((x1 - x)**2 + (y1 - y)**2))
    
    @staticmethod
    def actionCost(coord):
        x, y = coord
        
        # if x and y are non-zero that means its a diagonal traversal
        if x and y:
            return 1.414 # technically the distance is root of 2
        else:
            return 1
        
    @staticmethod   
    def isCoordValid(coord):
        x, y = coord
        if x < CONSTANT.CANVAS_WIDTH - CONSTANT.CLEARANCE and \
        y < CONSTANT.CANVAS_HEIGHT - CONSTANT.CLEARANCE and \
        x > CONSTANT.CLEARANCE  and \
        y > CONSTANT.CLEARANCE:
            return True
        else:
            return False
        
    def createNodes(self):
        nodes = []
        for action in Node.ACTION_SET:
            objNode = self._createNode(action)
            if objNode != None:
                nodes.append(objNode)    
        return nodes
    
    def _createNode(self, action):
        objNode = None
        res = tuple(map(sum, zip(self.coord, action)))
        
        if Node.isCoordValid(res):
            if res != self.coord:
                objNode = Node(res, self)
                #calculating the cost2come by adding the parent and action cost2come
                objNode.cost2come = round(Node.actionCost(action) + self.cost2come, 3)
            
        return objNode