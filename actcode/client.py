import grpc
import robot_call_pb2
import robot_call_pb2_grpc

def run():
    channel = grpc.insecure_channel("172.20.10.2:50051")
    stub = robot_call_pb2_grpc.RobotCallStub(channel)
    
    request = robot_call_pb2.RobotCalling(
    
        shoulder_pitch_left = 1,

        shoulder_pitch_right = 2,

        bicep_left = 3,

        bicep_right = 4,

        shoulder_roll_left = 5,

        shoulder_roll_right = 6,

        forearm_roll_left = 7,

        forearm_roll_right = 8,

        wrist_flexion_left = 9,

        wrist_flexion_right = 10,

        wrist_yaw_left = 11,

        wrist_yaw_right = 12,

        gripper_left = 13,

        gripper_right = 14,
    )
    
    response = stub.SendInstructions(request)
    print(f"Response: {response.message}")

if __name__ == "__main__":
    run()