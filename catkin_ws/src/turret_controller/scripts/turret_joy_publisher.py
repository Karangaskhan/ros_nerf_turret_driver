#!/usr/bin/env python

import rospy
from std_msgs.msg import Int8, Bool
from sensor_msgs.msg import Joy

# This ROS Node converts Joystick inputs from the joy node
# into commands for turret_controller

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 0 aka left stick horizontal controls pan
# axis 4 aka right stick vertical controls angular speed

def joyCallback(data):
    panValue = data.axes[6]
    tiltValue = data.axes[7]
    fire = data.buttons[5]
    pubPan.publish(panValue)
    pubTilt.publish(tiltValue)
    pubFire.publish(fire)

# Intializes everything
def connectToTurret():
    global pubTilt, pubPan, pubFire

    pubTilt = rospy.Publisher('turret_tilt', Int8)
    pubPan = rospy.Publisher('turret_pan', Int8)
    pubFire = rospy.Publisher('turret_fire', Bool)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber("joy", Joy, joyCallback)
    # starts the node
    rospy.init_node('joy_turret_commander')
    rospy.spin()

if __name__ == '__main__':
    connectToTurret()
