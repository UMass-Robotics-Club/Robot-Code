import cv2
import socket
import numpy as np

# Define UDP connection
UDP_IP = "172.20.10.3"  # Replace with receiver's IP (hotspot IP)
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

cap = cv2.VideoCapture(4)  # Change based on camera index
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    _, buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
    sock.sendto(buffer.tobytes(), (UDP_IP, UDP_PORT))

cap.release()
sock.close()

