#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Something_goes_wrong_or_not.py  //threading version

import rospy

import numpy as np

from std_msgs.msg import Float32

from sensor_msgs.msg import Image

import threading

import time

# 640width 480 height
# left_limit = 150

# right_limit = 150

# ceiling_limit = 100

# floor_limit = 100

is_good = False

over1000per = 1.

global cnt

# threading

num = 80

def do_work_line(te,be,le,re):
    for r in range(te,be):
        for c in range(le,re):
            ir_level[r,c] = (reshaped_data[r,c,0])|((reshaped_data[r,c,1])<<8)
            if ir_level[r,c] > 1000:          
                cnt = cnt + 1
            print '=== %d'%count
    
def ir_dot_callback(msg):
    start = time.time()
    global reshaped_data
    global ir_level
    cnt = 0.
    threadss = [] 
    start = time.time() 

    ir_level = np.eye(480,640)

    lili = list(msg.data)

    lili = [ord(i) for i in lili]
    
    raw_data = np.array(lili)

    reshaped_data = (raw_data.reshape(480,640,2))

    for ber in range(num):
        thh = threading.Thread(target=do_work_line, args=((480/num)*ber,(480/num)*(ber+1),(640/num)*ber,(640/num)*(ber+1)))
        thh.start()
        threadss.append(thh)
  
    for thh in threadss:
        thh.join()
    print cnt
    over1000per = cnt/float((640)*(480))
    is_good = True
    print("time :", time.time() - start) 

    print over1000per

### end the threading part

rate = rospy.Rate(10)    

ir_white_pub = rospy.Publisher('/ir_white_per', Float32, queue_size=1)    

aquiz_dat = rospy.Subscriber('/camera/ir/image_raw', Image, ir_dot_callback)

rospy.init_node('ir_dot_parse')



while ~rospy.is_shutdown():
    findat = Float32()
    findat.data = over1000per
    ir_white_pub.publish(findat)
    rate.sleep()

rospy.spin()
