cmake_minimum_required(VERSION 2.8.3)
project(corin_description)

find_package(catkin REQUIRED COMPONENTS
  robot_state_publisher
  urdf
  xacro
  gazebo_msgs
  geometry_msgs
  tf
  angles
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES corin_description
#  CATKIN_DEPENDS robot_state_publisher urdf xacro
#  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)