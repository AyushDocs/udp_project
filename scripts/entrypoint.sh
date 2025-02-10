#!/bin/bash
set -e

source /opt/ros/humble/setup.bash
source /app/workspace/install/setup.bash || echo "ROS 2 workspace not built yet"

exec "$@"