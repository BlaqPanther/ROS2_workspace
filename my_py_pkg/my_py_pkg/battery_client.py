#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed
import time, random


class BatteryStatusClient(Node):
    def __init__(self):
        super().__init__("battery")
        self.battery_state = "full"
        self.call_service()

    def call_service(self):
        client = self.create_client(SetLed, 'set_led')
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Set Led..")
        request = SetLed.Request()

        while True:
            if self.battery_state == "full":
                request.state = "off"
                client.call_async(request)
                time.sleep(6)
                self.battery_state = "empty"
                
                
            
            elif self.battery_state == "empty":
                request.state = "on"
                request.led_number = random.randint(1, 3)
                client.call_async(request)
                time.sleep(4)
                self.battery_state = "full"
                


            

def main(args=None):
    rclpy.init(args = args)
    node = BatteryStatusClient()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
