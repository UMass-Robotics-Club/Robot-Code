#!/usr/bin/env python3

import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('humanoid_controller')
    urdf_path = os.path.join(pkg_share, 'resource', 'humanoid_meshes.urdf')
    rviz_config_path = os.path.join(pkg_share, 'rviz', 'humanoid.rviz')

    # Read the URDF into a string
    with open(urdf_path, 'r') as infp:
        robot_description_content = infp.read()

    return LaunchDescription([
        # Your joint controller node
        Node(
            package='humanoid_controller',
            executable='humanoid_controller',
            name='humanoid_joint_controller',
            output='screen'
        ),

        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_description_content,
                'publish_frequency': 50.0  # Higher frequency for smoother visualization
            }]
        ),

        # RViz2
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path],
            parameters=[{
                'robot_description': robot_description_content
            }]
        )
    ])