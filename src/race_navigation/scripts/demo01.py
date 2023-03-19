#!/usr/bin/env python
#-*-coding:utf-8-*-

import roslib
import rospy
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose,PoseWithCovarianceStamped,Point,Quaternion,Twist
from move_base_msgs.msg import MoveBaseAction,MoveBaseGoal

#节点初始化
rospy.init_node('nav_1',anonymous=True)

#订阅move_base服务器的消息
move_base = actionlib.SimpleActionClient("move_base",MoveBaseAction)
rospy.loginfo("hello, please waiting ……")

#等待连接服务器，限制等待时间
while move_base.wait_for_server(rospy.Duration(5.0))==0:
    rospy.loginfo("success to move")

#设定目标点
target = Pose(Point(2.3, -2.92, -0.00534), Quaternion(0.000, 0.000, 1.000, 0.000))
goal=MoveBaseGoal()
goal.target_pose.pose=target
goal.target_pose.header.frame_id='map'
goal.target_pose.header.stamp=rospy.Time.now()

rospy.loginfo("Going to:"+str(target))

start_time = rospy.Time.now()

#向目标进发
move_base.send_goal(goal)

#五分钟时间限制
finished_within_time = move_base.wait_for_result(rospy.Duration(300))

#运行所用时间
running_time = rospy.Time.now()-start_time
running_time = running_time.secs

#查看是否到达成功
if not finished_within_time:
    move_base.cancel_goal()
    rospy.loginfo("超时")
else:
    state = move_base.get_state()
    if state == GoalStatus.SUCCEEDED:
        rospy.loginfo("Get Goal! The Time: %f",running_time)
    else:
        rospy.loginfo("失败")
