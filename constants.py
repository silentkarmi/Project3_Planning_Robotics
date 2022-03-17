#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from curses import COLOR_WHITE
from dataclasses import dataclass

@dataclass
class CONSTANT:
    
    START_NODE = (0, 0, 0)
    GOAL_NODE = (0, 0, 0)
       
    CANVAS_WIDTH = 400
    CANVAS_HEIGHT = 250
    
    VECTOR_LEN = 10
    GOAL_THRESOLD = 1.5 * 20
    
    MOBILE_ROBOT_RADIUS = 10
    CLEARANCE = 5 + MOBILE_ROBOT_RADIUS 
    
    WINDOW_NAME = "Project3_Phase_1"
        
    # Internal Constants
    
    ORIGIN_POINT_OFFSET = CANVAS_HEIGHT
    COLOR_RED = (0,0,255)
    COLOR_GREEN = (0, 100, 0)
    COLOR_BLUE = (255, 0, 0)
    COLOR_WHITE = (255, 255, 255)