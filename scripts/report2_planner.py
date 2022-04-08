#!/usr/bin/env python3

import rospy
import math

# import the plan message
from ur5e_control.msg import Plan
from geometry_msgs.msg import Twist
from robot_vision_lectures.msg import XYZarray

if __name__ == '__main__':
	# initialize the node
	rospy.init_node('simple_planner', anonymous = True)
	# add a publisher for sending joint position commands
	plan_pub = rospy.Publisher('/plan', Plan, queue_size = 10)
	# create subscriber for ur5e/toolpose coordinates
	toolpose = rospy.Subscriber('ur5e/toolpose', XYZarray)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)

	tp = toolpose.toolpose

	# define a plan variable
	plan = Plan()
	plan_point1 = Twist()
	# just a quick solution to send two target points
	# define a point close to the initial position
	plan_point1.linear.x = print(tp.linear.x)
	plan_point1.linear.y = -0.23
	plan_point1.linear.z = 0.363
	plan_point1.angular.x = 1.157
	plan_point1.angular.y = 0.0
	plan_point1.angular.z = 0.0
	# add this point to the plan
	plan.points.append(plan_point1)
	
	# this point is the ball location 
	
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
	# define a point away from the initial position
	plan_point3.linear.x = -0.6
	plan_point3.linear.y = -0.6
	plan_point3.linear.z = 0.3
	plan_point3.angular.x = 3.14
	plan_point3.angular.y = 0.0
	plan_point3.angular.z = 0.0
	# add this point to the plan
	plan.points.append(plan_point3)
	
	plan_point4 = Twist()
	# define a point away from the initial position
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