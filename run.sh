#!/bin/bash
source ~/catkin_ws/devel/setup.bash

roscore &
sleep 1

cd ~/Downloads/ 
sleep .5
./play_data.sh > /dev/null &

roslaunch ur_gazebo ur5e_bringup.launch &
sleep 10

# run manual initilization, stop it 10s later
rosrun ur5e_control manual_initialization.py &
sleep 10
kill $!

rosrun ur5e_control ur5e_controller &
sleep 1

rosrun ur5e_control task_space_traj &
sleep 1

roslaunch ur5e_control frame_publisher.launch &
sleep 1

rosrun rviz rviz &
sleep 5

rosrun robot_vision_lectures crop_visualize_3D &
sleep 1

cd ~/catkin_ws/src/robotics_lab6/scripts/
sleep .5
python3 detect_ball.py > /dev/null &
sleep 1

cd ~/catkin_ws/src/robotics_lab6/scripts/
sleep .5
python3 sphere_fit.py > /dev/null &

sleep 30

cd ~/catkin_ws/src/report_two/scripts
sleep .5
python3 report2_planner.py &

sleep 2d
