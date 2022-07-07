#!/usr/bin/env python

## Sets Gazebo Corin model to default world position in nominal standing up position

import rospy, sys, os, time
import string
import warnings
import tf
from math import pi

from gazebo_msgs.srv import *
from gazebo_ros import gazebo_interface
from std_srvs.srv import Empty
from gazebo_msgs.msg import ModelState
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState

def deg2rad(q):
	return (q*pi/180)

if __name__ == "__main__":

	rospy.init_node('initialise_node') 		#Initialises node

	model_name = 'corin'

	## publish to joint topics
	pub_01 = rospy.Publisher(model_name + '/lf_q1_joint/command', Float64, queue_size=1)
	pub_02 = rospy.Publisher(model_name + '/lf_q2_joint/command', Float64, queue_size=1)
	pub_03 = rospy.Publisher(model_name + '/lf_q3_joint/command', Float64, queue_size=1)
	pub_04 = rospy.Publisher(model_name + '/lm_q1_joint/command', Float64, queue_size=1)
	pub_05 = rospy.Publisher(model_name + '/lm_q2_joint/command', Float64, queue_size=1)
	pub_06 = rospy.Publisher(model_name + '/lm_q3_joint/command', Float64, queue_size=1)
	pub_07 = rospy.Publisher(model_name + '/lr_q1_joint/command', Float64, queue_size=1)
	pub_08 = rospy.Publisher(model_name + '/lr_q2_joint/command', Float64, queue_size=1)
	pub_09 = rospy.Publisher(model_name + '/lr_q3_joint/command', Float64, queue_size=1)
	pub_10 = rospy.Publisher(model_name + '/rf_q1_joint/command', Float64, queue_size=1)
	pub_11 = rospy.Publisher(model_name + '/rf_q2_joint/command', Float64, queue_size=1)
	pub_12 = rospy.Publisher(model_name + '/rf_q3_joint/command', Float64, queue_size=1)
	pub_13 = rospy.Publisher(model_name + '/rm_q1_joint/command', Float64, queue_size=1)
	pub_14 = rospy.Publisher(model_name + '/rm_q2_joint/command', Float64, queue_size=1)
	pub_15 = rospy.Publisher(model_name + '/rm_q3_joint/command', Float64, queue_size=1)
	pub_16 = rospy.Publisher(model_name + '/rr_q1_joint/command', Float64, queue_size=1)
	pub_17 = rospy.Publisher(model_name + '/rr_q2_joint/command', Float64, queue_size=1)
	pub_18 = rospy.Publisher(model_name + '/rr_q3_joint/command', Float64, queue_size=1)

	rospy.sleep(0.5)
	
	q1 = Float64()
	q2 = Float64()
	q3 = Float64()
	q1.data = 0.0
	q2.data = 0.34
	q3.data = -1.85
	
	for i in range(0,5):
		pub_01.publish(q1)
		pub_04.publish(q1)
		pub_07.publish(q1)
		pub_10.publish(q1)
		pub_13.publish(q1)
		pub_16.publish(q1)

		pub_02.publish(q2)
		pub_05.publish(q2)
		pub_08.publish(q2)
		pub_11.publish(q2)
		pub_14.publish(q2)
		pub_17.publish(q2)

		pub_03.publish(q3)
		pub_06.publish(q3)
		pub_09.publish(q3)
		pub_12.publish(q3)
		pub_15.publish(q3)
		pub_18.publish(q3)

		rospy.sleep(0.2) 	# small delay

	print 'Joint States Set Complete!'

	# Define variables
	model_state = ModelState()
	pose  		= Pose()
	twist 		= Twist()

	model_name 		= 'corin'
	reference_frame	= 'world'
	
	pose.position.x		= 0.0
	pose.position.y		= 0.0
	pose.position.z		= 0.15
	roll 				= 0.0
	pitch 				= 0.0
	yaw 				= 0.0
	quaternion 			= tf.transformations.quaternion_from_euler(deg2rad(roll), deg2rad(pitch), deg2rad(yaw))
	pose.orientation.x	= quaternion[0]
	pose.orientation.y	= quaternion[1]
	pose.orientation.z	= quaternion[2]
	pose.orientation.w	= quaternion[3]

	model_state.model_name 		= model_name
	model_state.pose 			= pose
	model_state.reference_frame = reference_frame

	gazebo_namespace = '/gazebo'

	try:
		rospy.wait_for_service('%s/set_model_state'%(gazebo_namespace), 2)
		set_model_state = rospy.ServiceProxy('%s/set_model_state'%(gazebo_namespace), SetModelState)
		rospy.loginfo("Calling service %s/set_model_state"%gazebo_namespace)
		resp = set_model_state(model_state)
		rospy.loginfo("Set model state status: %s"%resp.status_message)
		print resp.status_message

	except rospy.ServiceException as e:
		print("Service call failed: %s" % e)
	except rospy.ROSException as e:
		# Gazebo inactive
		print("Service call failed: %s" % e)

	for i in range(0,5):
		pub_01.publish(q1)
		pub_04.publish(q1)
		pub_07.publish(q1)
		pub_10.publish(q1)
		pub_13.publish(q1)
		pub_16.publish(q1)

		pub_02.publish(q2)
		pub_05.publish(q2)
		pub_08.publish(q2)
		pub_11.publish(q2)
		pub_14.publish(q2)
		pub_17.publish(q2)

		pub_03.publish(q3)
		pub_06.publish(q3)
		pub_09.publish(q3)
		pub_12.publish(q3)
		pub_15.publish(q3)
		pub_18.publish(q3)

		rospy.sleep(0.2) 	# small delay