#!/usr/bin/python3
# license removed for brevity
import rospy
import math

from sensor_msgs.msg import JointState

def talker():
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz

    # set initial angle
    angle = 0

    # start
    js = JointState()
    js.header.stamp = rospy.get_rostime()
    js.header.frame_id="Torso"
    
    js.name.append("HeadYaw")
    js.position.append(math.radians(0))
    
    js.name.append("HeadPitch")
    js.position.append(math.radians(0))
    
    js.name.append("LHipYawPitch")
    js.position.append(math.radians(0))
    
    js.name.append("LHipRoll")
    js.position.append(math.radians(0))
    
    js.name.append("LHipPitch")
    js.position.append(math.radians(0))
    
    js.name.append("LKneePitch")
    js.position.append(math.radians(0))
    
    js.name.append("LAnklePitch")
    js.position.append(math.radians(0))
    
    js.name.append("LAnkleRoll")
    js.position.append(math.radians(0))
    
    js.name.append("RHipRoll")
    js.position.append(math.radians(0))
    
    js.name.append("RHipPitch")
    js.position.append(math.radians(0))
    
    js.name.append("RKneePitch")
    js.position.append(math.radians(0))
    
    js.name.append("RAnklePitch")
    js.position.append(math.radians(0))
    
    js.name.append("RAnkleRoll")
    js.position.append(math.radians(0))
    
    js.name.append("LShoulderPitch")
    js.position.append(math.radians(0))
    
    js.name.append("LShoulderRoll")
    js.position.append(math.radians(0))
    
    js.name.append("LElbowYaw")
    js.position.append(math.radians(0))
    
    js.name.append("LElbowRoll")
    js.position.append(math.radians(0))
    
    js.name.append("LWristYaw")
    js.position.append(math.radians(0))
    
    js.name.append("LHand")
    js.position.append(math.radians(0))
    
    js.name.append("RShoulderPitch")
    js.position.append(math.radians(0))
    
    js.name.append("RShoulderRoll")
    js.position.append(math.radians(0))
    
    js.name.append("RElbowYaw")
    js.position.append(math.radians(0))
    
    js.name.append("RElbowRoll")
    js.position.append(math.radians(0))
    
    js.name.append("RWristYaw")
    js.position.append(math.radians(0))
    
    js.name.append("RHand")
    js.position.append(math.radians(0))
    
    rospy.loginfo(js)
    
    pub.publish(js)

    rate.sleep()

    # wave hi: up
    js = JointState()
    js.header.stamp = rospy.get_rostime()
    js.header.frame_id="Torso"
    
    js.name.append("LShoulderPitch")
    js.position.append(math.radians(90))
    
    js.name.append("LShoulderRoll")
    js.position.append(math.radians(30))
    
    js.name.append("LElbowRoll")
    js.position.append(math.radians(-30))
    
    js.name.append("RShoulderPitch")
    js.position.append(math.radians(-70))
    
    js.name.append("RShoulderRoll")
    js.position.append(math.radians(-30))
    
    rospy.loginfo(js)
    
    pub.publish(js)

    rate.sleep()
    
    # wave hi: down
    js = JointState()
    js.header.stamp = rospy.get_rostime()
    js.header.frame_id="Torso"
    
    js.name.append("LShoulderPitch")
    js.position.append(math.radians(0))
    
    js.name.append("LShoulderRoll")
    js.position.append(math.radians(0))
    
    js.name.append("LElbowRoll")
    js.position.append(math.radians(0))
    
    js.name.append("RShoulderPitch")
    js.position.append(math.radians(0))
    
    js.name.append("RShoulderRoll")
    js.position.append(math.radians(0))
    
    rospy.loginfo(js)
    
    pub.publish(js)

    rate.sleep()
    
    # nod head: mid to top
    js = JointState()
    js.header.stamp = rospy.get_rostime()
    js.header.frame_id="Torso"
    
    js.name.append("HeadPitch")
    js.position.append(math.radians(-27))
    
    rospy.loginfo(js)
    
    pub.publish(js)

    rate.sleep()
    
    # nod head: top to bot
    js = JointState()
    js.header.stamp = rospy.get_rostime()
    js.header.frame_id="Torso"
    
    js.name.append("HeadPitch")
    js.position.append(math.radians(27))
    
    rospy.loginfo(js)
    
    pub.publish(js)

    rate.sleep()
    
    # nod head: bot to mid
    js = JointState()
    js.header.stamp = rospy.get_rostime()
    js.header.frame_id="Torso"
    
    js.name.append("HeadPitch")
    js.position.append(math.radians(0))
    
    rospy.loginfo(js)
    
    pub.publish(js)

    rate.sleep()
    
    # shake head: center to right
    js = JointState()
    js.header.stamp = rospy.get_rostime()
    js.header.frame_id="Torso"
    
    js.name.append("HeadYaw")
    js.position.append(math.radians(-27))
    
    rospy.loginfo(js)
    
    pub.publish(js)

    rate.sleep()
    
    # shake head: center to right
    js = JointState()
    js.header.stamp = rospy.get_rostime()
    js.header.frame_id="Torso"
    
    js.name.append("HeadYaw")
    js.position.append(math.radians(27))
    
    rospy.loginfo(js)
    
    pub.publish(js)

    rate.sleep()
    
    # shake head: center to right
    js = JointState()
    js.header.stamp = rospy.get_rostime()
    js.header.frame_id="Torso"
    
    js.name.append("HeadYaw")
    js.position.append(math.radians(0))
    
    rospy.loginfo(js)
    
    pub.publish(js)

    rate.sleep()
    
    '''
    while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        js = JointState()
        
        # header info
        js.header.stamp = rospy.get_rostime()
        js.header.frame_id="Torso"


        # put in some joints that we'll edit
        js.name.append("HeadYaw")
        js.name.append("HeadPitch")

        js.position.append(math.radians(angle))
        js.position.append(0)

        #comment this out once it gets noisy
        rospy.loginfo(js)
        
        pub.publish(js)
        angle = angle + 1
        rate.sleep()
    '''
    

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
