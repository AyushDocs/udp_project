import rclpy
from rclpy.node import Node
import socket
from geometry_msgs.msg import Twist

class UdpPublisher(Node):
    def __init__(self):
        super().__init__('udp_publisher')

        self.declare_parameter('robot_ip', '192.168.1.100')
        self.declare_parameter('robot_port', 5005)
        self.robot_ip = self.get_parameter('robot_ip').value
        self.robot_port = self.get_parameter('robot_port').value

        # Setup UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Subscribe to /cmd_vel
        self.subscription = self.create_subscription(
            Twist, '/cmd_vel', self.cmd_vel_callback, 10)
    
    def cmd_vel_callback(self, msg):
        data = f"{msg.linear.x},{msg.angular.z}"
        self.sock.sendto(data.encode(), (self.robot_ip, self.robot_port))
        self.get_logger().info(f"Sent: {data}")

    def destroy_node(self):
        self.sock.close()
        super().destroy_node()

def main():
    rclpy.init()
    node = UdpPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
