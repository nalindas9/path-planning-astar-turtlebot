"""
Path Planning for Turtlebot using A* Algorithm

Authors:
Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import map 
import matplotlib.pyplot as plt
import numpy as np
import utils
import algo

def main():
  # Taking inputs from the user
  clearance = eval(input('Please enter the clearance value of the robot from the obstacle:'))
  print('The clearance value you entered is:', clearance)
  print('')
  start_point = eval(input('Please enter the start coordinates for the robot in this format - [X_coord, Y_coord, Theta]:'))
  while not utils.check_node(start_point, clearance):
    start_point = eval(input('Please enter the start coordinates in this format - [X_coord, Y_coord, Theta]:'))
  start_circle = plt.scatter(start_point[0], start_point[1], c = 'b')
  print('The start point you entered is:', start_point)
  print('')  
  goal_point = eval(input('Please enter the goal coordinates of the robot in this format - [X_coord, Y_coord]:'))
  while not utils.check_node(goal_point, clearance):
    goal_point = eval(input('Please enter the goal coordinates of the robot in this format - [X_coord, Y_coord]:'))
  goal_circle = plt.scatter(goal_point[0], goal_point[1], c = 'g')
  print('The goal point you entered is:', goal_point)
  print('')
  rpm = eval(input('Please enter the RPM for both the wheels in this format - [RPM1,RPM2]:'))
  print("The wheel RPM's you entered for both the wheels are:", rpm)
  print('')

  robot_radius = 0.177
  s1 = algo.Node(start_point, goal_point, [0,0], robot_radius+clearance, rpm[0], rpm[1])
  path, explored = s1.astar()
  
  plt.title('Path planning implemented for a Rigid Robot using A* Algorithm',fontsize=10)
  
  # Plotting the explored nodes and final path
  points1x = []
  points1y = []
  points2x = []
  points2y = []
  points3x = []
  points3y = []
  points4x = []
  points4y = []
  
  for point in range(len(explored)):
    if point+1 < len(explored):
      points1x.append(explored[point][0])
      points1y.append(explored[point][1])
      points2x.append((explored[point+1][0])-(explored[point][0]))
      points2y.append((explored[point+1][1])-(explored[point][1]))
    else:
      points1x.append(explored[point][0])
      points1y.append(explored[point][1])
      points2x.append((explored[-1][0])-(explored[point][0]))
      points2y.append((explored[-1][1])-(explored[point][1]))
      
  for point in range(len(path)):
    if point+1 < len(path):
      points3x.append(path[point][0])
      points3y.append((path[point][1]))
      points4x.append((path[point+1][0])-(path[point][0]))
      points4y.append((path[point+1][1])-(path[point][1]))
    else:
      points3x.append(path[point][0])
      points3y.append((path[point][1]))
      points4x.append((path[-1][0])-(path[point][0]))
      points4y.append((path[-1][1])-(path[point][1]))
  
  plt.quiver(np.array(points1x), np.array(points1y), np.array(points2x), np.array(points2y), units='xy' ,scale=1, label = 'Final Path', color = 'g', headwidth = 1,headlength=1)
     
  plt.quiver(np.array(points3x), np.array(points3y), np.array(points4x), np.array(points4y), units='xy' ,scale=1, label = 'Final Path', color = 'b')
  
  plt.show()
  
if __name__ == '__main__':
  main()
