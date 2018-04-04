#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def detectObstacle():
	    rospy.loginfo("Detecting Obstacles in the path") #Printed a message on console

	    rospy.init_node('sensor_read_ttbot', anonymous=True) #Initialized a Node

	    sub = rospy.Subscriber('cmd_vel_mux/input/navi', LaserScan, queue_size=10) #Made a subscriber which subscribes on a topic which gets laser data of the turtlebot sensor

	    rospy.spin()
	

if __name__ == '__main__':
    try:
        forward()
    except rospy.ROSInterruptException:
        pass
