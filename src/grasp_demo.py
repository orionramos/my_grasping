#! /usr/bin/env python
import sys
import rospy
import moveit_commander
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
robot = moveit_commander.RobotCommander()
arm_group = moveit_commander.MoveGroupCommander("arm")

# We can get the name of the reference frame for this robot:
planning_frame = arm_group.get_planning_frame()
print "============ Planning frame: %s" % planning_frame

# We can also print the name of the end-effector link for this group:
eef_link = arm_group.get_end_effector_link()
print "============ End effector link: %s" % eef_link

# We can get a list of all the groups in the robot:
group_names = robot.get_group_names()
print "============ Available Planning Groups:", robot.get_group_names()

# Sometimes for debugging it is useful to print the entire state of the
# robot:
print "============ Printing robot state"
print robot.get_current_state()
print ""


# Put the arm in the start position
arm_group.set_named_target("home")
plan1 = arm_group.go()

arm_group.set_named_target("test1")
#plan2 = arm_group.go()



hand_group = moveit_commander.MoveGroupCommander("hand")
# Open the gripper
hand_group.set_named_target("open")
#plan3 = hand_group.go()

# put the arm at the 1st grasping position
pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 1.0
pose_target.position.z = 1
arm_group.set_pose_target(pose_target)
plan = arm_group.go(wait=True)
# Calling `stop()` ensures that there is no residual movement
arm_group.stop()
# It is always good to clear your targets after planning with poses.
# Note: there is no equivalent function for clear_joint_value_targets()
arm_group.clear_pose_targets()



rospy.sleep(5)
moveit_commander.roscpp_shutdown()