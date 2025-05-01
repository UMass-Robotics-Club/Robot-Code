import grpc
from concurrent import futures
import robot_call_pb2
import robot_call_pb2_grpc
import struct
from datetime import datetime

class RobotCallServicer(robot_call_pb2_grpc.RobotCallServicer):
    def SendInstructions(self, request_iterator, context):
        print("Receiving streamed instructions:")
        for request in request_iterator:
            # ? Timestamp with milliseconds
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            print(f"\n[{now}] Received command:")
            print(request)

            # Extract selected fields
            values = [
                request.shoulder_pitch_left,
                request.shoulder_pitch_right,
                request.bicep_left,
                request.bicep_right,
                request.shoulder_roll_left,
                request.shoulder_roll_right
            ]
            packed = [struct.pack('f', val) for val in values]
            print(f"Packed bytes: {packed}")
        
        return robot_call_pb2.Response(transmitted=True, message="Instructions received")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    robot_call_pb2_grpc.add_RobotCallServicer_to_server(RobotCallServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

