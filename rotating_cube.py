#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Designed_by_Daseon_#

#rotating_cube.py

import rospy                                                                        # import ROS-python interface
from sensor_msgs.msg import Imu                                                     # import Imu type message 
from gazebo_msgs.msg import LinkState                                               # import Gazebo-LinkState type message

att_x = 0.                                                                          # Initializing attitude
att_y = 0.
att_z = 0.
att_w = 0.

def processing_fnc(msg):                                                            # Subscriber Call back

    global att_x                                                                    # globalization of variables
    global att_y
    global att_z
    global att_w

    att_x = msg.orientation.x                                                       # put received message into the corresponding axis
    att_y = msg.orientation.y                                                       
    att_z = msg.orientation.z                                                       
    att_w = msg.orientation.w                                                       # Quarternion type angle

rospy.init_node('show_window')                                                      # initializing ROS node

cube_att_dat = LinkState()                                                          # call the type class
cube_att_dat.link_name = 'cube::link_0'                                             # ****link name should be identical of the one of at gazibo****

cube_att_dat.pose.position.x = 0.0                                                  # Base position with catesian coordinate
cube_att_dat.pose.position.y = 0.0
cube_att_dat.pose.position.z = 5.0                                                  # levitate the model 5m so the model won't be dragged on the floor

cmd_cube_pub = rospy.Publisher('/gazebo/set_link_state', LinkState, queue_size=1)   # create publisher and advertise it. gazebo may subscribe

aquiz_px4_att_dat = rospy.Subscriber('/mavros/imu/data', Imu, processing_fnc)       # create subscriber which MAVROS gets imu data from

rate = rospy.Rate(30)                                                               # 30 loops/sec publish

while ~rospy.is_shutdown():                                                         # under rospy is running
    

    cube_att_dat.pose.orientation.x = att_x                                         # put the received data in a low at the buffer
    cube_att_dat.pose.orientation.y = att_y
    cube_att_dat.pose.orientation.z = att_z
    cube_att_dat.pose.orientation.w = att_w
    
    cmd_cube_pub.publish(cube_att_dat)                                              # publish the message in the buffer

    rate.sleep()                                                                    # corresponding delay to frequency

rospy.spin()                                                                        # give the authorization key back to the ros
