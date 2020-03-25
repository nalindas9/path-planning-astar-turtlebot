"""
Path Planning for Turtlebot using A* Algorithm

Authors:
Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""

def main():
  start_point = eval(input('Please enter the start coordinates for the robot in this format - [X_coord, Y_coord, Theta]:'))
  print('The start point you entered is:', start_point)
  print('')  
  goal_point = eval(input('Please enter the goal coordinates of the robot in this format - [X_coord, Y_coord]:'))
  print('The goal point you entered is:', goal_point)
  print('')
  rpm = eval(input('Please enter the RPM for both the wheels in this format - [RPM1,RPM2]:'))
  print("The wheel RPM's you entered for both the wheels are:", rpm)
  print('')
  clearance = eval(input('Please enter the clearance value of the robot from the obstacle:'))
  print('The clearance value you entered is:', clearance)
  
  
if __name__ == '__main__':
  main()
