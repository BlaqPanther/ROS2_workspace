#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.srv import SetLed
from my_robot_interfaces.msg import LedState

class LedPanelNode(Node):
    def __init__(self):
        super().__init__("led_panel")
        self.led_panel = [0,0,0]
        self.publisher_ = self.create_publisher(LedState, 'led_panel_state', 10)
        self.server_ = self.create_service(SetLed, 'set_led', self.service_callback)

    

    def service_callback(self, request, response):
        msg = LedState()
        if request.state == "on":
            self.led_panel[request.led_number - 1] = 1
        elif request.state == "off":
            self.led_panel = [0, 0, 0]
        response.success = True
        msg.led_panel_array = self.led_panel
        self.publisher_.publish(msg)
        return response
    

def main(args=None):
    rclpy.init(args = args)
    node = LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()