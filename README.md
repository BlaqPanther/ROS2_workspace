I'm on an exciting journey to mastering building robotics applications using ROS2.
All the packages in this repository are what I have worked on so far with regards to learning ROS.
Much more amazing projects are yet to be added. Stay tuned!


ros2 topic pub -1 /set_joint_trajectory trajectory_msgs/msg/JointTrajectory '{header: {frame_id: arm_base_link}, joint_names: [arm_base_forearm_joint, forearm_hand_joint], points: [ {positions: {0.0, 0.0}} ]}'
