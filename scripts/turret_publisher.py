#!/usr/bin/python

import rospy
from std_msgs.msg import Int8

def talker():
    pubTilt = rospy.Publisher('turret_tilt', Int8, queue_size=10)
    pubPan = rospy.Publisher('turret_pan', Int8, queue_size=10)
    rospy.init_node('turret_comander', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    commandList = [1,0,-1]
    pubList = [pubTilt, pubPan]
    while not rospy.is_shutdown():
        pubList[0].publish(commandList[0])
        commandList = rotate(commandList, 1)
        pubList = rotate(pubList, 1)
        rate.sleep()

def rotate(l, n):
    return l[n:] + l[:n]

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

