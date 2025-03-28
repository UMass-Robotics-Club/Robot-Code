import cv2
import socket
import numpy as np

UDP_IP = "0.0.0.0"  # Listen to all interfaces
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(65507)  # Max UDP Packet Size
    frame = np.frombuffer(data, dtype=np.uint8)
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    if frame is not None:
        cv2.imshow("Stream", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

sock.close()
cv2.destroyAllWindows()
