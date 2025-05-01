import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import math
import threading
import sys

class HumanoidJointController(Node):
    def __init__(self):
        super().__init__('humanoid_joint_controller')
        self.publisher_ = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.shutdown_flag = False
        self.lock = threading.Lock()

        self.joint_names = [
            "shoulder_roll_right_joint", "shoulder_pitch_right_joint",
            "bicep_right_joint", "forearm_roll_right_joint",
            "wrist_flexion_right_joint", "shoulder_roll_left_joint",
            "shoulder_pitch_left_joint", "bicep_left_joint",
            "forearm_roll_left_joint", "wrist_flexion_left_joint"
        ]
        self.joint_positions = {name: 0.0 for name in self.joint_names}

    def timer_callback(self):
        with self.lock:
            msg = JointState()
            msg.header.stamp = self.get_clock().now().to_msg()
            msg.name = self.joint_names
            msg.position = [self.joint_positions[name] for name in self.joint_names]
            self.publisher_.publish(msg)

    def set_joint_position(self, joint_name, degrees):
        with self.lock:
            if joint_name in self.joint_positions:
                radians = math.radians(degrees)
                self.joint_positions[joint_name] = radians
                self.get_logger().info(f"Set {joint_name} to {degrees}°")
                return True
            self.get_logger().warn(f"Joint '{joint_name}' not found")
            return False

def input_thread(controller):
    while not controller.shutdown_flag:
        try:
            user_input = input("\nEnter command (joint_name degrees) or 'exit': ")
            
            if user_input.lower().strip() == "exit":
                controller.shutdown_flag = True
                controller.get_logger().info("Shutting down...")
                rclpy.try_shutdown()
                break
                
            parts = user_input.strip().split()
            if len(parts) != 2:
                print("Invalid format. Example: shoulder_roll_right_joint 30")
                continue
                
            joint_name, degrees_str = parts
            try:
                degrees = float(degrees_str)
                if not controller.set_joint_position(joint_name, degrees):
                    print(f"Invalid joint name: {joint_name}")
            except ValueError:
                print("Please enter a valid number for degrees")
                
        except (EOFError, KeyboardInterrupt):
            controller.shutdown_flag = True
            rclpy.try_shutdown()
            break
        except Exception as e:
            print(f"Error: {e}")

def main(args=None):
    rclpy.init(args=args)
    controller = HumanoidJointController()
    
    # Start input thread
    thread = threading.Thread(target=input_thread, args=(controller,))
    thread.daemon = True
    thread.start()

    try:
        while rclpy.ok() and not controller.shutdown_flag:
            rclpy.spin_once(controller, timeout_sec=0.1)
    except KeyboardInterrupt:
        controller.shutdown_flag = True
    finally:
        thread.join(timeout=0.1)
        controller.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
        sys.exit(0)

if __name__ == '__main__':
    main()