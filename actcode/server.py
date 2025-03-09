import grpc
from concurrent import futures
import robot_call_pb2
import robot_call_pb2_grpc

class RobotCallServicer(robot_call_pb2_grpc.RobotCallServicer):
    def SendInstructions(self, request, context):
        print(f"Received command with FOLLOWING: {request}")
        for instruction in request.instructions:
            print(instruction)
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

