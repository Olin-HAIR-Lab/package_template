import rclpy
from rclpy.node import Node
from my_package_interfaces.msg import MyMessage
from .submodules.my_submodule import helper_function

# import any additional libraries below

class MyNode(Node):
    def __init__(self):
        super().__init__("my_node")  # type: ignore

        self.publisher = self.create_publisher(MyMessage, "my_message", 10)
        self.subscriber = self.create_subscription(MyMessage, "my_message", self.listener_callback, 10)  # type: ignore
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    
    def timer_callback(self):
        msg = MyMessage()
        msg.content = "Hello World!"
        self.publisher.publish(msg)


    def listener_callback(self, msg):
        helper_function()
        self.get_logger().info(f"[SUBSCRIBER] Received {msg.content}")


def main():
    rclpy.init()
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
