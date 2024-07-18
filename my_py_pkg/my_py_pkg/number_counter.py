#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.counter = 0
        
        self.subscriber_ = self.create_subscription(Int64, "number", self.add_number, 10)
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.reset_counter_service_ = self.create_service(SetBool, 'reset_counter', self.service_callback )
        self.timer_ = self.create_timer(0.5, self.publish_number_count)
        
        self.get_logger().info("Number Counter has begun")


    def add_number(self, msg):
        self.counter += msg.data
        
        
    
    def publish_number_count(self):
        msg = Int64()
        msg.data = self.counter
        self.publisher_.publish(msg)
    
    def service_callback(self, request, response):
        if request.data:
            self.counter = 0
            response.success = True
            response.message = "Counter has been reset"
        else:
            response.success = False
            response.message = "Counter has not been reset"
        return response

        
def main(args = None):
    rclpy.init(args = args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()