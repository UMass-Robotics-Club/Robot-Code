import grpc
from concurrent import futures
import robot_call_pb2
import robot_call_pb2_grpc
import struct
from datetime import datetime
import asyncio


# Asynchronous implementation of the RobotCallServicer
class RobotCallServicer(robot_call_pb2_grpc.RobotCallServicer):

    async def SendInstructions(self, request_iterator, context):
        print("Receiving streamed instructions:")
        async for request in request_iterator:
            # Get current time with milliseconds
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
            # Pack first six floats to binary
            packed = [struct.pack('f', val) for val in values]
            print(f"Packed bytes: {packed}")
        
        # Return response asynchronously
        return robot_call_pb2.Response(transmitted=True, message="Instructions received")


async def serve():
    # Create the gRPC server
    server = grpc.aio.server()
    # Register the servicer with the server
    robot_call_pb2_grpc.add_RobotCallServicer_to_server(RobotCallServicer(), server)
    # Add insecure port to listen on
    server.add_insecure_port('[::]:50051')

    # Start the server asynchronously
    await server.start()
    print("Server is running on port 50051...")
    # Wait for the server to finish
    await server.wait_for_termination()


if __name__ == "__main__":
    # Run the asynchronous server
    asyncio.run(serve())

