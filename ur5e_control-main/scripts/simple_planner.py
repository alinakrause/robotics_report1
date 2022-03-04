#!/usr/bin/env python3

import rospy
import math

# import the plan message
from ur5e_control.msg import Plan
from geometry_msgs.msg import Twist

if __name__ == '__main__':
	# initialize the node
	rospy.init_node('simple_planner', anonymous = True)
	# add a publisher for sending joint position commands
	plan_pub = rospy.Publisher('/plan', Plan, queue_size = 10)
	# set a 10Hz frequency for this loop
	loop_rate = rospy.Rate(10)

	# define a plan variable
	plan = Plan()
	plan_point1 = Twist()
	# just a quick solution to send two target points
	# define a point close to the initial position
	plan_point1.linear.x = -0.7
	plan_point1.linear.y = -0.23
	plan_point1.linear.z = 0.363
	plan_point1.angular.x = 1.57
	plan_point1.angular.y = 1.24
	plan_point1.angular.z = 0.0
	# add this point to the plan
	plan.points.append(plan_point1)
	
	plan_point2 = Twist()
	# define a point away from the initial position
	plan_point2.linear.x = -0.6
	plan_point2.linear.y = -0.13
	plan_point2.linear.z = 0.36
	plan_point2.angular.x = 3.14
	plan_point2.angular.y = 0.0
	plan_point2.angular.z = 1.57
	# add this point to the plan
	plan.points.append(plan_point2)
	
	plan_point3 = Twist()
	# define a point away from the initial position
	plan_point3.linear.x = -0.9
	plan_point3.linear.y = -0.13
	plan_point3.linear.z = 0.05
	plan_point3.angular.x = 3.13
	plan_point3.angular.y = 0.0
	plan_point3.angular.z = 1.57
	# add this point to the plan
	plan.points.append(plan_point3)
	
	plan_point4 = Twist()
	# define a point away from the initial position
	plan_point4.linear.x = -0.6
	plan_point4.linear.y = -0.13
	plan_point4.linear.z = 0.36
	plan_point4.angular.x = 3.14
	plan_point4.angular.y = 0.0
	plan_point4.angular.z = 1.57
	# add this point to the plan
	plan.points.append(plan_point4)
	
	plan_point5 = Twist()
	# define a point away from the initial position
	plan_point5.linear.x = 0.13
	plan_point5.linear.y = -0.79
	plan_point5.linear.z = 0.36
	plan_point5.angular.x = 3.14
	plan_point5.angular.y = 0.0
	plan_point5.angular.z = 3.14
	# add this point to the plan
	plan.points.append(plan_point5)
	
	plan_point6 = Twist()
	# define a point away from the initial position
	plan_point6.linear.x = 0.13
	plan_point6.linear.y = -0.9
	plan_point6.linear.z = 0.05
	plan_point6.angular.x = 3.14
	plan_point6.angular.y = 0.0
	plan_point6.angular.z = 3.14
	# add this point to the plan
	plan.points.append(plan_point6)
	
	plan_point7 = Twist()
	# define a point away from the initial position
	plan_point7.linear.x = 0.13
	plan_point7.linear.y = -0.79
	plan_point7.linear.z = 0.36
	plan_point7.angular.x = 3.14
	plan_point7.angular.y = 0.0
	plan_point7.angular.z = 3.14
	# add this point to the plan
	plan.points.append(plan_point7)

	plan_point8 = Twist()
	# define a point away from the initial position
	plan_point8.linear.x = -0.6
	plan_point8.linear.y = -0.13
	plan_point8.linear.z = 0.36
	plan_point8.angular.x = 3.14
	plan_point8.angular.y = 0.0
	plan_point8.angular.z = 1.57
	# add this point to the plan
	plan.points.append(plan_point8)

	
	
	while not rospy.is_shutdown():
		# publish the plan
		plan_pub.publish(plan)
		# wait for 0.1 seconds until the next loop and repeat
		loop_rate.sleep()
