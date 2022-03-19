#!/usr/bin/env python3
# Author @ Kartikeya Mishra @ Chang-Hong Chen

from platform import node
import cv2
import heapq
from dataclasses import dataclass

from constants import CONSTANT
from canvas import Canvas
from node import Node
from utility import Utility
from obstacles.circleObstacle import CircleObstacle
from obstacles.hexagonObstacle import HexagonObstacle
from obstacles.polygonObstacle import PolygonObstacle

@dataclass
class Traversal:

    def __init__(self):
        self._closedList = set() #ToDo: Create a matrix and go to that do a 1, to tell the node has been visited
        self._closeListNodes = []
        self._openList = []
        self._listSolution = []
        
        self.canvaArea = Canvas()
        
        objCircle = CircleObstacle((300, 185), 40)
        self.canvaArea.addObstacle(objCircle)
        
        objTriangularPolygon = PolygonObstacle([(36, 185),
                                                (115, 210),
                                                (80, 180),
                                                (105, 100)])
        self.canvaArea.addObstacle(objTriangularPolygon)
        
        objHexagonPolygon = HexagonObstacle([(165, round(79.79275)),
                                            (165, round(120.2073)),
                                            (200, round(140.4145)),
                                            (235, round(120.2073)),
                                            (235, round(79.79275)),
                                            (200, round(59.5855))])
        self.canvaArea.addObstacle(objHexagonPolygon)
        
        self.startNode = None
        self.endNode = None
        self.solutionNode = None
        
    def expandNodesAndPushIntoWorkspace(self, node):
        listNodes = node.createNodes()
        for subNode in listNodes:
            self.pushNode(subNode)       

   
    def pushNode(self, node):
        if node != None:
            isNodeSafe = self.canvaArea.isOutsideObstacleSpace(node)
            
            if isNodeSafe:
                isNodeInClosedList = (node.coord[0], node.coord[1]) in self._closedList
                if not isNodeInClosedList:
                    nodeInWorkspace = self.isNodeInOpenListThenUpdate(node)
                    if not nodeInWorkspace:
                        heapq.heappush(self._openList, node)
    
    def isNodeInOpenListThenUpdate(self, node):
        isInOpenList = False
        if isinstance(node, Node):
            for tempNode in self._openList:
                if tempNode.isEqual(node):
                    if node.cost2come < tempNode.cost2come:
                        tempNode = node
                        
                    isInOpenList = True 
                    break
                    
        return isInOpenList
                
    def isThisGoalNode(self, nodeToCheck):
        xcentre, ycentre, end_theta = self.endNode.coord
        x, y, node_theta = nodeToCheck.coord
        in_goal = (x - xcentre)**2 + (y -ycentre)**2 - (CONSTANT.GOAL_THRESOLD)**2 < 0
        is_goal = False
        if in_goal:
            if (Utility.actionInDegree(end_theta) == 
                            Utility.actionInDegree(node_theta)):
                is_goal = True

        return is_goal
        
    
    def createNodeTree(self):
        print("Generating Node Tree...")
        self.pushNode(self.startNode)
        while(self._openList):

            # Run spinning cursor while creating node tree
            Utility.run_spinning_cursor()
            
            # pops an element from the top of the list
            tempNode = heapq.heappop(self._openList)     
            self._closeListNodes.append(tempNode)
            self._closedList.add((round(tempNode.coord[0]),
                                        round(tempNode.coord[1])))  
             
            if(self.isThisGoalNode(tempNode)):
                self.solutionNode = tempNode
                break
            
            self.expandNodesAndPushIntoWorkspace(tempNode)
            
        else:
            print("SOLUTION NOT FOUND")
            
    def drawNodeTree(self):
        print("Drawing Node Tree...")
        counter = 0
        for tempNode in self._closeListNodes:
            self.canvaArea.drawNode(tempNode)
            counter +=1
            cv2.waitKey(1)
            
    def backTrack(self):
        print("Backtracking...")
        self._listSolution = []
        tempNode = self.solutionNode
        while tempNode != None:
            self._listSolution.append(tempNode)
            tempNode = tempNode.parentNode
            
    def drawSolution(self):  
        print("Drawing the solution...")          
        for node in self._listSolution[::]:
            self.canvaArea.drawMobileRobot(node)
            cv2.waitKey(1)
            
        for node in self._listSolution[::-1]:
            self.canvaArea.drawNode(node, CONSTANT.COLOR_BLUE)
            cv2.waitKey(1)
