#!/usr/bin/env python3

import rospy
import math

# import the plan message
from ur5e_control.msg import Plan
from geometry_msgs.msg import Twist 
from robot_vision_lectures.msg import SphereParams

start_pos_rec = False
ball_pos_rec = False

def get_points(XYZ):
	global start_pos_rec
	global start_pos
	start_pos = XYZ
	start_pos_rec = True
	print(1)


def get_ball(points):
	print(2)
	global ball_pos_rec
	global ball_pos
	ball_pos = points
	ball_pos_rec = True
	
	
	
def main():
	# initialize the node
	rospy.init_node('simple_planner', anonymous = True)
	
	# create subscriber for ur5e/toolpose coordinates
	# this is used for the starting point position to avoid jumps
	toolpose = rospy.Subscriber('ur5e/toolpose', Twist, get_points)
	# get the ball center coordinates
	ball = rospy.Subscriber('/sphere_params', SphereParams, get_ball)
	# add a publisher for sending joint position commands
	plan_pub = rospy.Publisher('/plan', Plan, queue_size = 10)
	
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		if start_pos_rec and ball_pos_rec:
			# define a plan variable
			plan = Plan()
			
			
			plan_point1 = Twist()
			# Use the current robot position coordinates as these points to avoid jumps
			plan_point1.linear.x = start_pos.linear.x
			plan_point1.linear.y = start_pos.linear.y
			plan_point1.linear.z = start_pos.linear.z
			plan_point1.angular.x = start_pos.angular.x
			plan_point1.angular.y = start_pos.angular.y
			plan_point1.angular.z = start_pos.angular.z
			# add this point to the plan
			plan.points.append(plan_point1)
			print(plan_point1)
			print(ball_pos)
			# use the ball center coordinates for this point
			plan_point2 = Twist()
			# define a point away from the initial position
			plan_point2.linear.x = 0
			plan_point2.linear.y = 0
			plan_point2.linear.z = 0
			plan_point2.angular.x = 0
			plan_point2.angular.y = 0
			plan_point2.angular.z = 0
			# add this point to the plan
			plan.points.append(plan_point2)
			
			
			plan_point3 = Twist()
			# This point can be anything (any point above the "drop" positon
			plan_point3.linear.x = -0.6
			plan_point3.linear.y = -0.6
			plan_point3.linear.z = 0.3
			plan_point3.angular.x = 3.14
			plan_point3.angular.y = 0.0
			plan_point3.angular.z = 0.0
			# add this point to the plan
			plan.points.append(plan_point3)
			
			
			plan_point4 = Twist()
			# this point can be anthing (the "drop" positon)
			plan_point4.linear.x = -0.6
			plan_point4.linear.y = -0.6
			plan_point4.linear.z = 0.05
			plan_point4.angular.x = 3.14
			plan_point4.angular.y = 0.0
			plan_point4.angular.z = 0.0
			# add this point to the plan
			plan.points.append(plan_point4)

	
	
	while not rospy.is_shutdown():
		# publish the plan
		plan_pub.publish(plan)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
		
if __name__ == '__main__':
	main()
