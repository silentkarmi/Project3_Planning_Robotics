#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from constants import CONSTANT
import cv2
from traversal import Traversal
from node import Node
import time

if __name__ == "__main__":
    
    while (1):
        
        startXCoord, startYCoord, startGoalThetha = (input("\nStart X, Y, Theta [Add Space between values]:")).split()
        startXCoord, startYCoord, startGoalThetha = int(startXCoord), int(startYCoord), int(startGoalThetha)
        
        if(startGoalThetha % 30 != 0 and 
           startGoalThetha >= -60 and startGoalThetha <=60):
            print("Invalid Start Goal Thetha")
            continue
        
        CONSTANT.START_NODE = (startXCoord, startYCoord, startGoalThetha)
        
        objTraversal = Traversal()
        objTraversal.startNode = Node(CONSTANT.START_NODE, None)
        if Node.isCoordValid(CONSTANT.START_NODE) and \
            objTraversal.canvaArea.isOutsideObstacleSpace(objTraversal.startNode):
                
            endXCoord, endYCoord, endGoalThetha = (input("End X, Y, Theta [Add Space in between]:")).split()
            endXCoord, endYCoord, endGoalThetha = int(endXCoord), int(endYCoord), int(endGoalThetha)
        
            if not (endGoalThetha % 30 == 0 and 
            endGoalThetha >= -60 and endGoalThetha <=60):
                print("Invalid End Goal Thetha")
                continue
            
            CONSTANT.GOAL_NODE = (endXCoord, endYCoord, -30)
            objTraversal.endNode = Node(CONSTANT.GOAL_NODE , None)
            objTraversal.startNode = Node(CONSTANT.START_NODE, None)
            
            if (Node.isCoordValid(CONSTANT.GOAL_NODE ) and 
                objTraversal.canvaArea.isOutsideObstacleSpace(objTraversal.endNode)):
                
                CONSTANT.CLEARANCE = int(input("What's the Clearance from the Mobile Robot:"))
                CONSTANT.MOBILE_ROBOT_RADIUS = int(input("What's the Mobile Robot Radius:"))
                CONSTANT.VECTOR_LEN = int(input("Enter a Step size [1 - 10]:"))
                
                if not(CONSTANT.VECTOR_LEN > 0 and CONSTANT.VECTOR_LEN < 11):
                    print("Invalid Step Length")
                    continue
                            
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
    
    
    
    