# PathPlannerDijkstra
It uses Dijikstra's algorithm to find path for the given map
--------------------------------------------------------------------------------------------------
>> When obstacle objects are drawn, they are inflated internally but not drawn on the screen.
>> Mobile robot is considered as a point robot and objects are inflated by the radius of the mobile robot
>> You will see the clearance of 5mm + Mobile Robot Radius when nodes are traversed and see a gap.
>> Color Meaning
    - Red : obstacle
    - White : nodes traversed
    - Black : clearance from the boundary and the obstacles (in the end of traversal) / empty space
    - Green : The mobile robot with the radius
    - Blue : Shortest path from start to end coordinates
>> Worst Condition of whole graph traversal can take upto 5 minutes
>> GitHub URL: https://github.com/silentkarmi/Project3_Planning_Robotics
>> Structure of the Program
    - main.py - main starting point of the Program
    - node.py - each coordinate is considered a node
    - canvas.py - deals with drawing opencv related details
    - obstacles package - contains the boomerang polygon obstacle, circle obstacle and regular hexagon obstacle related files
    - utility.py - functions which used throughout Program
    - constants.py - declare constants which used throughout the Program
    - traversal.py - this is where the A* algorithm is implemented
>> Note: Python3 is used to write the code
>> Command to run from terminal:
python3 main.py

