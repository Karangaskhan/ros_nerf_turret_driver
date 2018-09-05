#!/usr/bin/python

import rospy
from std_msgs.msg import Int8, Bool

import turret_controller


def tiltCallback(data):
    if(data.data > 0):
        turret.turretStop()
        turret.turretUp()
    elif(data.data < 0):
        turret.turretStop()
        turret.turretDown()
    elif(data.data == 0):
        turret.turretStop()
    
def panCallback(data):
    if(data.data > 0):
        turret.turretStop()
        turret.turretLeft()
    elif(data.data < 0):
        turret.turretStop()
        turret.turretRight()
    elif(data.data == 0):
        turret.turretStop()

def fireCallback(data):
    if(data.data):
        turret.turretStop()
        turret.turretFire()

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("turret_tilt", Int8, tiltCallback)
    rospy.Subscriber("turret_pan", Int8, panCallback)
    rospy.Subscriber("turret_fire", Bool, fireCallback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    turret = turret_controller.LaunchControl()
    listener()