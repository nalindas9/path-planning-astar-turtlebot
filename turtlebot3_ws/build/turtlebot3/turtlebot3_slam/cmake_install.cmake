# Install script for directory: /home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-astar-turtlebot/turtlebot3_ws/src/turtlebot3/turtlebot3_slam

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-astar-turtlebot/turtlebot3_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-astar-turtlebot/turtlebot3_ws/build/turtlebot3/turtlebot3_slam/catkin_generated/installspace/turtlebot3_slam.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_slam/cmake" TYPE FILE FILES
    "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-astar-turtlebot/turtlebot3_ws/build/turtlebot3/turtlebot3_slam/catkin_generated/installspace/turtlebot3_slamConfig.cmake"
    "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-astar-turtlebot/turtlebot3_ws/build/turtlebot3/turtlebot3_slam/catkin_generated/installspace/turtlebot3_slamConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_slam" TYPE FILE FILES "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-astar-turtlebot/turtlebot3_ws/src/turtlebot3/turtlebot3_slam/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_slam/flat_world_imu_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_slam/flat_world_imu_node")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_slam/flat_world_imu_node"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_slam" TYPE EXECUTABLE FILES "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-astar-turtlebot/turtlebot3_ws/devel/lib/turtlebot3_slam/flat_world_imu_node")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_slam/flat_world_imu_node" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_slam/flat_world_imu_node")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_slam/flat_world_imu_node"
         OLD_RPATH "/opt/ros/kinetic/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/turtlebot3_slam/flat_world_imu_node")
    endif()
  endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/turtlebot3_slam" TYPE DIRECTORY FILES "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-astar-turtlebot/turtlebot3_ws/src/turtlebot3/turtlebot3_slam/include/turtlebot3_slam/")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/turtlebot3_slam" TYPE DIRECTORY FILES
    "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-astar-turtlebot/turtlebot3_ws/src/turtlebot3/turtlebot3_slam/bag"
    "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-astar-turtlebot/turtlebot3_ws/src/turtlebot3/turtlebot3_slam/config"
    "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-astar-turtlebot/turtlebot3_ws/src/turtlebot3/turtlebot3_slam/launch"
    "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM661_Planning_For_Autonomous_Robots/Github/Project_3/path-planning-astar-turtlebot/turtlebot3_ws/src/turtlebot3/turtlebot3_slam/rviz"
    )
endif()
