import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description():
    teleop_launch = IncludeLaunchDescription(PythonLaunchDescriptionSource([
        os.path.join(get_package_share_directory('racecar_neo'), 'launch'),
        '/teleop.launch.py'
    ]))

    cartographer_node = Node(
        package='cartographer_ros',
        executable='cartographer_node',
    )

    display_node = Node(
        package='cartographer_slam',
        executable='display',
        emulate_tty=True,
        output='screen'
    )

    return LaunchDescription([
        teleop_launch,
        cartographer_node,
        display_node
    ])
