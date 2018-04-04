#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def forward():
    rospy.init_node('forward_ttbot', anonymous=True) #Initialized a Node
    rospy.loginfo("Press Ctrl + C to Quit") #Printed a message on console
    pub = rospy.Publisher('cmd_vel_mux/input/navi', Twist, queue_size=10) #Made a publisher which publishes on a topic
    rate = rospy.Rate(10) # 10hz 
    
    #Initializing a variable which is of the Twist type(which TTBot uses)
    move_ttbot = Twist() 
    move_ttbot.linear.x = 0.2 #meter/sec
    move_ttbot.angular.x = 0  #radians/sec

    while not rospy.is_shutdown():
        pub.publish(move_ttbot)
        rate.sleep()

def stop(): #Function to stop the turtlebot
    rospy.loginfo("Stopping Turtlebot")
    pub.publish(Twist()) #Because default Twist is linear = angular = 0.0
    rospy.sleep(1)

if __name__ == '__main__':
    try:
        forward()
    except rospy.ROSInterruptException:
        pass
