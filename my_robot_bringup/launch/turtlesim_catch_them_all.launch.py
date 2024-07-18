
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    turtlesim_node_ = Node(package="turtlesim",
                     executable="turtlesim_node")
    
    turtlesim_spawner_node_ = Node(package="turtlesim_catch_them_all",
                                   executable="turtle_spawner",
                                   parameters=[{'spawn_frequency':2.0}]
                                )
    
    turtlesim_controller_node_ = Node(package="turtlesim_catch_them_all",
                                      executable="turtle_controller",
                                      parameters=[{'catch_closest_turtle_first': True}]
                                    )
    

    ld.add_action(turtlesim_node_)
    ld.add_action(turtlesim_spawner_node_)
    ld.add_action(turtlesim_controller_node_)
    return ld
