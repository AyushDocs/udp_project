from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='udp_teleop',
            executable='udp_publisher',
            parameters=['config/params.yaml']
        )
    ])
