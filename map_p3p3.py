import numpy as np 
import math
import cv2


world = 255 * np.ones((100,100,3))


def obstacle_circle1(world):
  crow= 80 
  ccol= 30 
  rad= 10
  for row in range(100):
    for col in range(100):
      if (row- crow)**2+(col-ccol)**2- rad**2<= 0:
        world[row][col]=(255,0,0)

def obstacle_circle2(world):
  crow= 80 
  ccol= 70 
  rad= 10
  for row in range(100):
    for col in range(100):
      if (row- crow)**2+(col-ccol)**2- rad**2<= 0:
        world[row][col]=(255,0,0)

def obstacle_circle3(world):
  crow= 50 
  ccol= 50 
  rad= 10
  for row in range(100):
    for col in range(100):
      if (row- crow)**2+(col-ccol)**2- rad**2<= 0:
        world[row][col]=(255,0,0)

def obstacle_circle4(world):
  crow= 20 
  ccol= 70 
  rad= 10
  for row in range(100):
    for col in range(100):
      if (row- crow)**2+(col-ccol)**2- rad**2<= 0:
        world[row][col]=(255,0,0)

def obstacle_square1(world):
  p1=(22.5, 12.5)
  p2=(37.5, 12.5)
  p3=(22.5, 15.5)
  p4=(37.5, 15.5)
  for row in range(100):
     for col in range(100):
        if row -12.5>=0 and row-27.5<=0 and col - 22.5>=0 and col-37.5<=0:
          world[row][col]=(255,0,0)


def obstacle_square2(world):
  p1=(2.5, 57.5)
  p2=(17.5, 57.5)
  p3=(2.5, 42.5)
  p4=(17.5, 42.5)
  
  for row in range(100):
     for col in range(100):
        if row -42.5>=0 and row-57.5<=0 and col - 2.5>=0 and col-17.5<=0:
          world[row][col]=(255,0,0)

def obstacle_square3(world):
  p1=(87.5, 57.5)
  p2=(97.5, 57.5)
  p3=(87.5, 42.5)
  p4=(97.5, 42.5)
  
  for row in range(100):
     for col in range(100):
       if row -42.5>=0 and row-57.5<=0 and col - 97.5<=0 and col-82.5>=0:
          world[row][col]=(255,0,0)

obstacle_circle1(world)
obstacle_circle2(world)
obstacle_circle3(world)
obstacle_circle4(world)
obstacle_square1(world)
obstacle_square2(world)
obstacle_square3(world)
cv2.imshow("window",world)
cv2.waitKey(0)
