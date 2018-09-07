#!/usr/bin/env python

import rospy
from std_msgs.msg import Int8, Bool
from dnn_detect.msg import DetectedObjectArray

# This ROS Node converts Joystick inputs from the joy node
# into commands for turret_controller

# Receives joystick messages (subscribed to Joy topic)
# then converts the joysick inputs into Twist commands
# axis 0 aka left stick horizontal controls pan
# axis 4 aka right stick vertical controls angular speed

def callback(data):
    people = filter(lambda o : o.class_name == "person", data.objects)
    if(people):
        target = people[0]
        #if(target.class_name == "person" and target.confidence > 0.5):
        # if True:
        (x, y) = calculateCentroid(target)
        if(isTargetInCrosshair(x,y)):
            sendCommands(320,240)
        else:
            if(panRequired(x,y)):
                sendCommands(x, 240)
            else:
                sendCommands(320, y)
    else: 
        sendCommands(320,240)

def calculateCentroid(target):
    average_x = (target.x_max + target.x_min) / 2
    average_y = (target.y_max + target.y_min) / 2
    return (average_x, average_y)

def isTargetInCrosshair(x,y):
    return(x>240 and x<400)# and y>190 and y<290)

def panRequired(x,y):
    return(abs(x-320) > abs(y-240))

def sendCommands(x,y):
    if(x == 320):
        panValue = 0
    if(x - 320 < 0):
        panValue = 1
    elif(x - 320 > 0):
        panValue = -1
    pubPan.publish(panValue)

    # if(y == 240):
        # tiltValue = 0
    # if(x - 240 < 0):
        # tiltValue = 1
    # elif(x - 240 > 0):
        # tiltValue = -1
    # print(tiltValue)
    # pubTilt.publish(tiltValue)
    # fire = 0
    # print(x, y)
    # pubFire.publish(fire)

# Intializes everything
def connectToTurret():
    global pubTilt, pubPan, pubFire

    pubTilt = rospy.Publisher('turret_tilt', Int8, queue_size=1)
    pubPan = rospy.Publisher('turret_pan', Int8, queue_size=1)
    pubFire = rospy.Publisher('turret_fire', Bool, queue_size=1)
    # subscribed to /dnn_objects to find objects of person
    rospy.Subscriber("dnn_objects", DetectedObjectArray, callback)
    # starts the node
    rospy.init_node('human_tracker')
    rospy.spin()

if __name__ == '__main__':
    connectToTurret()
