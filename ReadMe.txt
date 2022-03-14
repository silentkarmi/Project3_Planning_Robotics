# PathPlannerDijkstra
It uses Dijikstra's algorithm to find path for the given map
--------------------------------------------------------------------------------------------------
>> When obstacle objects are drawn, they are inflated internally but not drawn on the screen.
>> Instead you will see the clearance of 5mm (= 5px in code) when nodes are traversed and see a gap.
>> I am assuming that when you add 5px clearance, (6,6) Coordinate is a valid coordinate. This hypothesis is used everywhere in the program.
>> Color Meaning
    - Red : obstacle
    - White : nodes traversed
    - Black : clearance from the boundary and the obstacles (in the end of traversal) / empty space
    - Green : Shortest path from start to end coordinates
>> Worst Condition of whole graph traversal can take upto 2 minutes
>> GitHub URL: https://github.com/silentkarmi/PathPlannerDijkstra
>> Structure of the Program
    - Dijkstra-pathplanning-Kartikeya-Mishra.py - main starting point of the Program
    - node.py - each coordinate is considered a node
    - canvas.py - deals with drawing opencv related details
    - obstacles package - contains the boomerang polygon obstacle, circle obstacle and regular hexagon obstacle related files
    - utility.py - functions which used throughout Program
    - constants.py - declare constants which used throughout the Program
    - traversal.py - this is where the Dijikstra algorithm is implemented
>> Video Ouput of the program, included in the zip: djikstra_output_mishra_k.mkv
>> Note: Python3 is used to write the code
>> Command to run from terminal:
python3 Dijkstra-pathplanning-Kartikeya-Mishra.py

