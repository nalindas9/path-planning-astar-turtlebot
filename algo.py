"""
Node class for A* Algorithm

Authors:
Nalin Das (nalindas9@gmail.com)
Graduate Student pursuing Masters in Robotics,
University of Maryland, College Park
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import utils
import operator
import random 

k = 0
# 3D array with (x,y,theta) as index
visited_nodes = np.zeros((50,50,37))
# Dictionary for backtracking 
valid_childs_dict = {}
# List to store all the explored nodes for visualization
explored = []
# Node class containing action set, graph generation and Astar Algorithm
weight = 5
class Node():
  # Constructor for Node class
  def __init__(self, start_node, goal_node, parent_node, clearance, rpm1, rpm2):
    self.start_node = start_node
    self.parent_node = parent_node
    self.clearance = clearance
    self.goal_node = goal_node
    self.rpm1 = rpm1
    self.rpm2 = rpm2
    
  
  # Method to find new coordinates for non holonomic constraints
  def move(self,Xi,Yi,Thetai,UL,UR):
    t = 0
    r = 0.038
    L = 0.354
    dt = 0.1
    Xn=Xi
    Yn=Yi
    Thetan = 3.14 * Thetai / 180

# Xi, Yi,Thetai: Input point's coordinates
# Xs, Ys: Start point coordinates for plot function
# Xn, Yn, Thetan: End point coordintes

    while t<1:
        t = t + dt
        Xs = Xn
        Ys = Yn
        Xn += 0.5*r * (UL + UR) * math.cos(Thetan) * dt
        Yn += 0.5*r * (UL + UR) * math.sin(Thetan) * dt
        Thetan += (r / L) * (UR - UL) * dt
        #plt.plot([Xs, Xn], [Ys, Yn], color="blue")

    Thetan = 180 * (Thetan) / 3.14
    return Xn, Yn, Thetan
    
  # Defining action set and graph generation
  def move1(self,node, cost):
    x_new, y_new, theta_new = self.move(node[0], node[1], node[2], 0, self.rpm1)
    angle = (theta_new)%360
    new_node = [x_new, y_new, angle]
    cost2come = cost + 1.5
    cost2go = weight*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move2(self,node, cost):
    x_new, y_new, theta_new = self.move(node[0], node[1], node[2], self.rpm1, 0)
    angle = (theta_new)%360
    new_node = [x_new, y_new, angle]
    cost2come = cost + 1.3
    cost2go = weight*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move3(self,node, cost):
    x_new, y_new, theta_new = self.move(node[0], node[1], node[2], self.rpm1, self.rpm1)
    angle = (theta_new)%360
    new_node = [x_new, y_new, angle]
    cost2come = cost + 1
    cost2go = weight*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move4(self,node, cost):
    x_new, y_new, theta_new = self.move(node[0], node[1], node[2], 0, self.rpm2)
    angle = (theta_new)%360
    new_node = [x_new, y_new, angle]
    cost2come = cost + 1.5
    cost2go = weight*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move5(self,node, cost):
    x_new, y_new, theta_new = self.move(node[0], node[1], node[2], self.rpm2, 0)
    angle = (theta_new)%360
    new_node = [x_new, y_new, angle]
    cost2come = cost + 1.5
    cost2go = weight*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move6(self,node, cost):
    x_new, y_new, theta_new = self.move(node[0], node[1], node[2], self.rpm2, self.rpm2)
    angle = (theta_new)%360
    new_node = [x_new, y_new, angle]
    cost2come = cost + 1
    cost2go = weight*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move7(self,node, cost):
    x_new, y_new, theta_new = self.move(node[0], node[1], node[2], self.rpm1, self.rpm2)
    angle = (theta_new)%360
    new_node = [x_new, y_new, angle]
    cost2come = cost + 1.3
    cost2go = weight*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  def move8(self,node, cost):
    x_new, y_new, theta_new = self.move(node[0], node[1], node[2], self.rpm2, self.rpm1)
    angle = (theta_new)%360
    new_node = [x_new, y_new, angle]
    cost2come = cost + 1.3
    cost2go = weight*((self.goal_node[0]-new_node[0])**2 + (self.goal_node[1]-new_node[1])**2)**(1/2)
    total_cost = cost2come + cost2go
    new_node.append(total_cost)
    new_node.append(cost2come)
    return new_node
    
  # Method to generate index given a node
  def index(self, node):
    return (node[0], node[1], node[2])
    
  # Method that generates valid children given a node
  def child_generator(self, node, cost):
    # List to store all valid children
    valid_children = []
    # Generating the children
    n1 = self.move1(node, cost)
    n2 = self.move2(node, cost)
    n3 = self.move3(node, cost)
    n4 = self.move4(node, cost)
    n5 = self.move5(node, cost)
    n6 = self.move6(node, cost)
    n7 = self.move7(node, cost)
    n8 = self.move8(node, cost)
    # List to store all children
    childs = [n1,n2,n3,n4,n5,n6,n7,n8]
    # Dictionary with cost as key and child as value
    childs_cost = {n1[3]:n1,n2[3]:n2,n3[3]:n3,n4[3]:n4, n5[3]:n5, n6[3]:n6,n7[3]:n7, n8[3]:n8}
    # Check for valid children and append them to the list
    for cost in childs_cost.keys():
      if utils.check_node(childs_cost[cost], self.clearance) == True and visited_nodes[int(round(childs_cost[cost][0],1)/0.2)][int(round(childs_cost[cost][1],1)/0.2)][int(round(childs_cost[cost][2],1)/10)] == 0:
        valid_children.append((cost, childs_cost[cost], childs_cost[cost][4], self.index(childs_cost[cost]),node))
        valid_childs_dict[self.index(childs_cost[cost])] = [childs_cost[cost], node, self.index(node)]
        visited_nodes[int(round(childs_cost[cost][0],1)/0.2)][int(round(childs_cost[cost][1],1)/0.2)][int(round(childs_cost[cost][2],1)/10)] = 1
        
    return valid_children

  def astar(self):
    print('Started Search ... ')
    explored_nodes = [(0, self.start_node, self.index(self.start_node), self.parent_node)]
    explored.append(self.start_node)
    valid_childs_dict[self.index(self.start_node)] = [self.start_node, self.parent_node]
    cum_cost = 0
    itr = 0
    while len(explored_nodes) > 0:
      print('Explored Depth:', itr)
      min_cost_child = explored_nodes[0][1]
      explored_nodes.pop(0)
      child_costs= self.child_generator(min_cost_child, cum_cost)
      for child in child_costs:
        explored_nodes.append(child)
        explored.append(child)
      explored_nodes.sort(key=operator.itemgetter(0))
      #print('Explored Nodes:', explored_nodes)
      cum_cost = explored_nodes[0][2]
      itr = itr+1
      if ((min_cost_child[0] - self.goal_node[0]) ** 2 + (min_cost_child[1] - self.goal_node[1]) ** 2) <= 0.25 ** 2:
        final_node_key =  (min_cost_child[0], min_cost_child[1], min_cost_child[2])
        print('Goal node found!')
        break 
    print('Started Backtracking ...')
    final_path= self.back_track(final_node_key)
    print('Backtracking complete!')
    return final_path, explored
        
  def back_track(self, node_ind):
    path = [valid_childs_dict[node_ind][0]]
    while node_ind != self.index(self.start_node):
      parent = valid_childs_dict[node_ind][1]
      path.insert(0, parent)
      node_ind = valid_childs_dict[node_ind][2]
    print('The path is:', path)
    return path
    
