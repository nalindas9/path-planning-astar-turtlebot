"""
Utility Functions

Authors:
Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import numpy as np
import math


# Function to check if the given point lies outside the final map or in the obstacle space
def check_node(node, clearance):
  # Checking if point inside map
  if node[0] + clearance >= 10 or node[0] - clearance <= 0 or node[1] + clearance >= 10 or node[1] - clearance <= 0:
    print('Sorry the point is out of bounds! Try again.')
    return False
  # Checking if point inside circles
  elif (node[0] - 3) ** 2 + (node[1] - 2) ** 2 <= (1+clearance) ** 2 :
    print('Sorry the point is in the circle 1 obstacle space! Try again')
    return False
  elif (node[0] - 7) ** 2 + (node[1] - 2) ** 2 <= (1+clearance) ** 2 :
    print('Sorry the point is in the circle 2 obstacle space! Try again')
    return False
  elif (node[0] - 5) ** 2 + (node[1] - 5) ** 2 <= (1+clearance) ** 2 :
    print('Sorry the point is in the circle 3 obstacle space! Try again')
    return False
  elif (node[0] - 7) ** 2 + (node[1] - 8) ** 2 <= (1+clearance) ** 2 :
    print('Sorry the point is in the circle 4 obstacle space! Try again')
    return False
  # Checking if point inside squares
  elif node[0] + clearance >= 0.25 and node[0] - clearance <=1.75 and node[1] + clearance>= 4.25 and node[1] - clearance< 5.75:
    print('Sorry the point is in the square 1 obstacle space! Try again')
    return False
  elif node[0] + clearance >= 2.25 and node[0] - clearance <= 3.75 and node[1] + clearance>= 7.25 and node[1] - clearance <= 8.75:
    print('Sorry the point is in the square 2 obstacle space! Try again')
    return False
  elif node[0] + clearance >= 8.25 and node[0] - clearance <= 9.75 and node[1] + clearance>= 4.25 and node[1] - clearance <= 5.75:
    print('Node is:', node[0] + clearance >= 8.25)
    print('Sorry the point is in the square 3 obstacle space! Try again')
    return False
  else:
    return True   
  
