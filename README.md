# UDP Teleop

## Overview
`udp_project` is a ROS 2 package that subscribes to the `/cmd_vel` topic from the `teleop` package and transmits velocity commands via UDP to a remote robot. This implementation is minimalistic, backward-compatible, and suitable for production use.

## Features
- Subscribes to `/cmd_vel` (geometry_msgs/Twist)
- Extracts linear and angular velocity
- Sends velocity commands over UDP
- Configurable target IP and port via ROS parameters
- Proper error handling and socket management
- Supports ROS 2 Humble (and possibly Galactic/Foxy)

## Directory Structure
```
udp_project/
├── udp_project
│   ├── __init__.py
│   ├── udp_publisher.py  # Core ROS 2 node
├── config
│   ├── params.yaml       # Configurable target IP/port
├── launch
│   ├── udp_project.launch.py
├── package.xml
├── setup.py
├── setup.cfg
├── CMakeLists.txt
└── README.md
```

## Installation
### 1. Clone the Repository
```sh
cd ~/ros2_ws/src
git clone https://github.com/AyushDocs/udp_project.git
```

### 2. Build the Package
```sh
cd ~/ros2_ws
colcon build --packages-select udp_teleop
source install/setup.bash
```

## Configuration
The `params.yaml` file allows setting the target robot IP and port:
```yaml
robot_ip: "192.168.1.100"
robot_port: 5005
```

## Running the Node
### Using ros2 launch:
```sh
ros2 launch udp_teleop udp_teleop.launch.py
```

### Directly from the command line:
```sh
ros2 run udp_teleop udp_publisher
```

## Node Details
### **udp_publisher.py**
- Subscribes to `/cmd_vel`
- Reads `Twist` messages
- Sends UDP packets with `linear.x` and `angular.z`

## Shutdown & Cleanup
To safely stop the node:
```sh
Ctrl+C
```
The socket is properly closed upon shutdown.

## License
MIT License

## Author
Ayush Dubey

