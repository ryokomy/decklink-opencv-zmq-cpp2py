import struct
import zmq
import numpy as np
import cv2

print("Python: Camera subscriber!")
    
# Open ZMQ Connection
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt(zmq.SUBSCRIBE, "")

while True:
    # Receve Data from C++ Program
    data =  socket.recv()

    # Convert byte to integer
    rows = 1080
    cols = 1920
    mat_type = 16

    if mat_type == 0:
        # Gray Scale
        image = np.frombuffer(data, dtype=np.uint8).reshape((rows,cols));
    else:
        # BGR Color
        image = np.frombuffer(data, dtype=np.uint8).reshape((rows,cols,3));

    # Write BMP Image
    cv2.imshow("Python Subscriber", image)
    cv2.waitKey(16)