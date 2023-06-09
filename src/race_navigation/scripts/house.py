#!/usr/bin/env python
# -*- coding: utf-8 -*-

import roslib
import rospy
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped, Point, Quaternion, Twist
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# 节点初始化
rospy.init_node('move_test', anonymous=True)

# 订阅move_base服务器的消息
move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)

rospy.loginfo("Waiting for move_base action server...")

# 等待连接服务器，5s等待时间限制
while move_base.wait_for_server(rospy.Duration(5.0)) == 0:
    rospy.loginfo("Connected to move base server")

# 设定目标点1
target = Pose(Point(9.81, -6.44, -0.00137), Quaternion(0.000, 0.000, 0.5746, 0.8184))
# target = Pose(Point(0.963, -1.038, 0.000), Quaternion(0.000, 0.000, 0.5746, 0.8184))
goal = MoveBaseGoal()
goal.target_pose.pose = target
goal.target_pose.header.frame_id = 'map'
goal.target_pose.header.stamp = rospy.Time.now()

rospy.loginfo("Going to: " + str(target))

start_time = rospy.Time.now()  

# 向目标进发
move_base.send_goal(goal)

# 五分钟时间限制
finished_within_time = move_base.wait_for_result(rospy.Duration(300))

# 运行所用时间  
running_time01 = rospy.Time.now() - start_time  
running_time01 = running_time01.secs

# 查看是否成功到达
if not finished_within_time:
    move_base.cancel_goal()
    rospy.loginfo("Timed out achieving goal")
else:
    state = move_base.get_state()
    if state == GoalStatus.SUCCEEDED:
        rospy.loginfo("Goal succeeded! Time Result: %f", running_time01)
    else:
        rospy.loginfo("Goal failed！ ")


# rospy.loginfo("Going to: " + str(target))

# start_time = rospy.Time.now()  

# 设定目标点2
target = Pose(Point(5.82, -6.69, -0.00137), Quaternion(0.000, 0.000,  0,  1))
goal = MoveBaseGoal()
goal.target_pose.pose = target
goal.target_pose.header.frame_id = 'map'
goal.target_pose.header.stamp = rospy.Time.now()

rospy.loginfo("Going to: " + str(target))

start_time = rospy.Time.now()  

# 向目标进发
move_base.send_goal(goal)

# 五分钟时间限制
finished_within_time = move_base.wait_for_result(rospy.Duration(300))

# 运行所用时间  
running_time02 = rospy.Time.now() - start_time  
running_time02= running_time02.secs

# 查看是否成功到达
if not finished_within_time:
    move_base.cancel_goal()
    rospy.loginfo("Timed out achieving goal")
else:
    state = move_base.get_state()
    if state == GoalStatus.SUCCEEDED:
        rospy.loginfo("Goal succeeded! Time Result: %f", running_time02)
    else:
        rospy.loginfo("Goal failed ! ")

    
# 设定目标点3
target = Pose(Point(2.86, -5.71, -0.00137), Quaternion(0.000, 0.000,  0,  1))
goal = MoveBaseGoal()
goal.target_pose.pose = target
goal.target_pose.header.frame_id = 'map'
goal.target_pose.header.stamp = rospy.Time.now()

rospy.loginfo("Going to: " + str(target))

start_time = rospy.Time.now()  

# 向目标进发
move_base.send_goal(goal)

# 五分钟时间限制
finished_within_time = move_base.wait_for_result(rospy.Duration(300))

# 运行所用时间  
running_time03 = rospy.Time.now() - start_time  
running_time03 = running_time03.secs

# 查看是否成功到达
if not finished_within_time:
    move_base.cancel_goal()
    rospy.loginfo("Timed out achieving goal")
else:
    state = move_base.get_state()
    if state == GoalStatus.SUCCEEDED:
        rospy.loginfo("Goal succeeded! Time Result: %f", running_time03)
    else:
        rospy.loginfo("Goal failed ! ")

# 设定目标点4
target = Pose(Point(-0.0296, -1.79, -0.00143), Quaternion(0.000, 0.000,  0,  1))
goal = MoveBaseGoal()
goal.target_pose.pose = target
goal.target_pose.header.frame_id = 'map'
goal.target_pose.header.stamp = rospy.Time.now()

rospy.loginfo("Going to: " + str(target))

start_time = rospy.Time.now()  

# 向目标进发
move_base.send_goal(goal)

# 五分钟时间限制
finished_within_time = move_base.wait_for_result(rospy.Duration(300))

# 运行所用时间  
running_time04 = rospy.Time.now() - start_time  
running_time04 = running_time04.secs
running_time_total = running_time01+running_time02+running_time03+running_time04
# 查看是否成功到达
if not finished_within_time:
    move_base.cancel_goal()
    rospy.loginfo("Timed out achieving goal")
else:
    state = move_base.get_state()
    if state == GoalStatus.SUCCEEDED:
        rospy.loginfo("Goal succeeded! Time Result: %f", running_time04)
        rospy.loginfo("The total time of taking is: %f",running_time_total)
    else:
        rospy.loginfo("Goal failed ! ")