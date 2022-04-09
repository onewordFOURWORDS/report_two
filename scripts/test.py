#!/usr/bin/env python3

import rospy
import math

# import the plan message
from ur5e_control.msg import Plan
from geometry_msgs.msg import Twist
from robot_vision_lectures.msg import XYZarray

def get_points(XYZ):
	print("?")
	global start_pos
	start_pos = XYZ.points

def main():
	rospy.init_node('sphere_fit', anonymous = True)

	toolpose = rospy.Subscriber('ur5e/toolpose', XYZarray, get_points)

	# set the loop frequency
	rate = rospy.Rate(10)

	rospy.spin()
	
	
	
if __name__ == '__main__':
	main()
