#!/usr/bin/env python

# ROS Publisher Node talker.py from:
#    https://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29

import rospy

from counselors.msg import Counselor

#def picked_up():
#    global pub
#    pub_str = "PICKED UP %s" % rospy.get_time()
#    rospy.loginfo(pub_str)
#    pub.publish(Handset(stamp=rospy.Time.now(), picked_up=True))


def counselors_manager():
    # Set-up Publisher
    global pub
    # pub = rospy.Publisher('hook', Handset, queue_size=10)
    rospy.init_node('counselors_manager', anonymous=True)

if __name__ == '__main__':
    try:
        counselors_manager()
    except rospy.ROSInterruptException:
        pass
