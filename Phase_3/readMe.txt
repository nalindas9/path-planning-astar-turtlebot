# PROJECT3- PHASE3: Path Planning for non-holonomic robot using A* Algorithm
This is the repository for the project - Path planning implemented for a turtlebot 3 making use of A* Algorithm.

## System and library requirements.
 - Python3
 - Numpy
 - matplotlib
 - math
 
## How to Run
1. Clone this repo or extract the "proj3_5_gazebo.zip" file. <br>
2. Navigate to the folder "Phase_3" <br>
3. To view the simulation video for the following parameters - 
Start : (-4, 3, 0)
Goal : (4, -3)
Radius and clearance : Robot radius and 0.2 meters
Open the video "Phase3_video.avi"<br>
4. To run the code, from the terminal, run the command `python3 main.py` <br>
5. The program will ask for the clearance (in meters) from the obstacles, provide input in 'float' format. For eg: 0.2<br>
6. Next program will ask for start point, provide input in [x,y,theta] format. For eg: [-4,3,0]. If the points provided are in the obstacle space or out of bounds, program will ask you to re-enter points.<br>
7. Next program will ask for goal point, provide input in [x,y] format. For eg: [4,-3].
If the points provided are in the obstacle space or out of bounds, program will ask you to re-enter points.<br>
8. You will then be asked the two RPM's for the wheels, provide input in [rpm1,rpm2] format, For eg: [6,4] <br>

Github link: https://github.com/nalindas9/path-planning-astar-turtlebot

The blue circle is the start point, and the yellow circle is the goal with threshold radius of 0.25 meters. The green color is for the explored nodes, while the black color signifies the final path. 


