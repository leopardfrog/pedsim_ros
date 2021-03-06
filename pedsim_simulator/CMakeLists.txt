cmake_minimum_required(VERSION 2.8)
project(pedsim_simulator)
add_definitions(-Wall -Wunused -std=c++0x -pipe) # C++ 11 is required
set(PEDSIM_SIMULATOR_DEPENDENCIES
    roscpp
    rospy
    std_msgs
    pedsim
    pedsim_msgs
    pedsim_srvs
    std_srvs
    visualization_msgs
    animated_marker_msgs
    nav_msgs
    geometry_msgs
    tf
    cmake_modules
    dynamic_reconfigure
)

## Find catkin macros and libraries
find_package(catkin REQUIRED COMPONENTS ${PEDSIM_SIMULATOR_DEPENDENCIES})
find_package(Boost REQUIRED)
find_package(Qt5Widgets REQUIRED)
find_package(Eigen REQUIRED)

# dynamic reconfigure parameters
generate_dynamic_reconfigure_options(config/PedsimSimulator.cfg)

catkin_package(
    CATKIN_DEPENDS ${PEDSIM_SIMULATOR_DEPENDENCIES}
    INCLUDE_DIRS include
)

include_directories(include)
include_directories(${Eigen_INCLUDE_DIRS})
include_directories(${catkin_INCLUDE_DIRS})
#include(Qt5::Widgets)

set(SOURCES
    src/simulator_node.cpp
	src/simulator.cpp
    src/scene.cpp
    src/config.cpp
    src/orientationhandler.cpp
    src/agentstatemachine.cpp
    src/scenarioreader.cpp
	src/rng.cpp

	# elements
	src/element/agent.cpp
	src/element/agentgroup.cpp
	src/element/agentcluster.cpp
	src/element/areawaypoint.cpp
	src/element/attractionarea.cpp
	src/element/queueingwaypoint.cpp
	src/element/waitingqueue.cpp
	src/element/waypoint.cpp
	src/element/obstacle.cpp
	src/element/scenarioelement.cpp

	# forces
	src/force/alongwallforce.cpp
	src/force/force.cpp
	src/force/groupcoherenceforce.cpp
	src/force/groupgazeforce.cpp
	src/force/grouprepulsionforce.cpp
	src/force/randomforce.cpp

	# waypointplanner
	src/waypointplanner/waypointplanner.cpp
	src/waypointplanner/individualwaypointplanner.cpp
	src/waypointplanner/queueingplanner.cpp
	src/waypointplanner/shoppingplanner.cpp
	src/waypointplanner/groupwaypointplanner.cpp
)


set(MOC_FILES
	include/pedsim_simulator/config.h
	include/pedsim_simulator/scene.h
	include/pedsim_simulator/agentstatemachine.h

	include/pedsim_simulator/element/scenarioelement.h
	include/pedsim_simulator/element/agent.h
	include/pedsim_simulator/element/agentcluster.h
	include/pedsim_simulator/element/agentgroup.h
	include/pedsim_simulator/element/attractionarea.h
	include/pedsim_simulator/element/obstacle.h
	include/pedsim_simulator/element/waypoint.h
	include/pedsim_simulator/element/areawaypoint.h
	include/pedsim_simulator/element/waitingqueue.h
	include/pedsim_simulator/element/queueingwaypoint.h

	include/pedsim_simulator/force/force.h
	include/pedsim_simulator/force/randomforce.h
	include/pedsim_simulator/force/groupgazeforce.h
	include/pedsim_simulator/force/groupcoherenceforce.h
	include/pedsim_simulator/force/grouprepulsionforce.h
	include/pedsim_simulator/force/alongwallforce.h

	include/pedsim_simulator/waypointplanner/waypointplanner.h
	include/pedsim_simulator/waypointplanner/individualwaypointplanner.h
	include/pedsim_simulator/waypointplanner/groupwaypointplanner.h
	include/pedsim_simulator/waypointplanner/shoppingplanner.h
	include/pedsim_simulator/waypointplanner/queueingplanner.h
)
QT5_WRAP_CPP(MOC_SRCS_UI ${MOC_FILES})

add_executable(pedsim_simulator ${SOURCES} ${MOC_SRCS_UI})
add_dependencies(pedsim_simulator ${catkin_EXPORTED_TARGETS})
add_dependencies(pedsim_simulator ${PROJECT_NAME}_gencfg)
target_link_libraries(pedsim_simulator
		Qt5::Widgets ${BOOST_LIBRARIES} ${catkin_LIBRARIES}
)

add_executable(simulate_diff_drive_robot src/simulate_diff_drive_robot.cpp)
add_dependencies(simulate_diff_drive_robot ${catkin_EXPORTED_TARGETS})
target_link_libraries(simulate_diff_drive_robot ${BOOST_LIBRARIES} ${catkin_LIBRARIES})

install(
    TARGETS
        pedsim_simulator
        simulate_diff_drive_robot
    ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
    LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
    RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


## Unit Tests
