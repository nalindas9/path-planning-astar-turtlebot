#!/usr/bin/env sh
# generated from catkin/cmake/template/local_setup.sh.in

# since this file is sourced either use the provided _CATKIN_SETUP_DIR
# or fall back to the destination set at configure time
: ${_CATKIN_SETUP_DIR:=/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-astar-turtlebot/turtlebot3_ws/devel}
CATKIN_SETUP_UTIL_ARGS="--extend --local"
. "$_CATKIN_SETUP_DIR/setup.sh"
unset CATKIN_SETUP_UTIL_ARGS
