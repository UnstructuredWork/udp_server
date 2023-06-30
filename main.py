from threading import Thread
from src.server import Server, KinectServer

LEFT_PORT = 5001
RIGHT_PORT = 5002
KINECT_PORT = 5003

left = Server(LEFT_PORT)
right = Server(RIGHT_PORT)
kinect = KinectServer(KINECT_PORT)

l_thr = Thread(target=left.run, args=())
r_thr = Thread(target=right.run, args=())
k_thr = Thread(target=kinect.run, args=())

if __name__ == "__main__":
    l_thr.start()
    r_thr.start()
    k_thr.start()
