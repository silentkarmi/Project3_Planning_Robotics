#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from constants import CONSTANT
import cv2
from traversal import Traversal
from node import Node
import time

if __name__ == "__main__":
    
    while (1):
        #to do input start goal thetha
        startXCoord = 50#int(input("\nStart X Coordinate:"))
        startYCoord = 50#int(input("Start Y Coordinate:"))
        
        CONSTANT.START_NODE = (startXCoord, startYCoord, 0)
        
        objTraversal = Traversal()
        objTraversal.startNode = Node(CONSTANT.START_NODE, None)
        if Node.isCoordValid(CONSTANT.START_NODE) and \
            objTraversal.canvaArea.isOutsideObstacleSpace(objTraversal.startNode):
                
            endXCoord =  230#int(input("End X Coordinate:"))
            endYCoord =  200#int(input("End Y Coordinate:"))
        
            CONSTANT.GOAL_NODE = (endXCoord, endYCoord, -30)
            objTraversal.endNode = Node(CONSTANT.GOAL_NODE , None)
            objTraversal.startNode = Node(CONSTANT.START_NODE, None)
            
            if (Node.isCoordValid(CONSTANT.GOAL_NODE ) and 
                objTraversal.canvaArea.isOutsideObstacleSpace(objTraversal.endNode)):
                
                start_time = time.time()
                objTraversal.createNodeTree()
                objTraversal.backTrack() # backtracks the solution
                print(f"Total Nodes Searched:{len(objTraversal._closedList)}")
                print("--- %s seconds for finding the solution ---" % (time.time() - start_time))
                
                # VISUALIZATION PART
                objTraversal.canvaArea.drawObstacles()
                objTraversal.drawNodeTree() # draws the node tree after solution is found
                objTraversal.drawSolution() # draws the solution
                cv2.waitKey(0)
                quit()
            else:
                print("Invalid End Coordinates. Try Again.\n")
        else:
            print("Invalid Start Coordinates. Try Again.\n")
    
    
    
    
