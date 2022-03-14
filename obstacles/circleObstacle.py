#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from ast import Constant
import cv2
from dataclasses import dataclass
from obstacles.obstacleInterface import ObstacleInterface

from constants import CONSTANT
from utility import Utility

@dataclass
class CircleObstacle(ObstacleInterface):
    center: tuple()
    radius: int = 0
    
    def draw(self, canvasArea):
        cv2.circle(canvasArea, Utility.getCoordinatesInWorldFrame(self.center), 
                   self.radius, CONSTANT.COLOR_RED, -1)
        cv2.imshow(CONSTANT.WINDOW_NAME, canvasArea)
        
    def isOutside(self, coord):
        x, y = coord
        xcenter, ycenter = self.center
        result = (x - xcenter) ** 2 + (y - ycenter) ** 2 - (self.radius + CONSTANT.CLEARANCE) ** 2
        return result > 0