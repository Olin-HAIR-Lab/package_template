from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_package', 
            executable='run_my_node'
        )
        # Add more nodes/launch files if needed
    ])
