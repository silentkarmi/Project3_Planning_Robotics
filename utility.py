#!/usr/bin/env python3
# Author @ Kartikeya Mishra

from dataclasses import dataclass
from constants import CONSTANT

@dataclass
class Utility:
    @staticmethod
    def getCoordinatesInWorldFrame(coord):
        x, y = coord
        y = CONSTANT.ORIGIN_POINT_OFFSET - y
        return (x, y)