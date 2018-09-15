#!/usr/bin/env python

# ROS Publisher Node talker.py from:
#    https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29

import rospy

from counselors.msg import Counselor, Available
from counselors.srv import Next

def next_counselor(req):
    rospy.loginfo("Next Counselor")
    # stub counselor
    c = Counselor(name="Person 1", loc="here", loc="+123456789")
    return Next(c)

def counselor_timeline(event):
    global pub
    rospy.loginfo("Updating Counselors %s" % rospy.get_time())

    # how many counselors are currently available
    pub.publish(Available(num_available=1))

def counselors_manager():
    global pub

    rospy.init_node('counselors_manager', anonymous=True)

    # availability publishing
    pub = rospy.Publisher('counselors/available', Available, queue_size=10)

    # next counselor service
    s = rospy.Service('next', Next, next_counselor)

    # monitor the counselor timeline every 30 seconds
    rospy.Timer(rospy.Duration(30), counselor_timeline)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        counselors_manager()
    except rospy.ROSInterruptException:
        pass
