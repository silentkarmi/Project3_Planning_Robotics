#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from constants import CONSTANT
import cv2
from traversal import Traversal
from node import Node
import time

if __name__ == "__main__":
    
    while (1):
        startXCoord = 16 #int(input("\nStart X Coordinate:"))
        startYCoord = 16 #int(input("Start Y Coordinate:"))
        
        CONSTANT.START_NODE = (startXCoord, startYCoord)
        
        objTraversal = Traversal()
        objTraversal.startNode = Node(CONSTANT.START_NODE, None)
        if Node.isCoordValid(CONSTANT.START_NODE) and \
            objTraversal.canvaArea.isOutsideObstacleSpace(objTraversal.startNode):
                
            endXCoord = 384 #int(input("End X Coordinate:"))
            endYCoord = 234 #int(input("End Y Coordinate:"))
        
            CONSTANT.GOAL_NODE = (endXCoord, endYCoord)
            objTraversal.endNode = Node(CONSTANT.GOAL_NODE , None)
            objTraversal.startNode = Node(CONSTANT.START_NODE, None)
            
            if Node.isCoordValid(CONSTANT.GOAL_NODE ) and \
                objTraversal.canvaArea.isOutsideObstacleSpace(objTraversal.endNode):
                
                start_time = time.time()
                objTraversal.canvaArea.drawObstacles()
                objTraversal.createNodeTree()
                objTraversal.backTrack()
                objTraversal.drawSolution()
                print("--- %s seconds for finding the solution ---" % (time.time() - start_time))
                cv2.waitKey(0)
                quit()
            else:
                print("Invalid End Coordinates. Try Again.\n")
        else:
            print("Invalid Start Coordinates. Try Again.\n")
    
    
    
    
