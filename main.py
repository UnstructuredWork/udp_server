from src.server import Server
from threading import Thread

HOST = "10.252.101.174"

LEFT_PORT = 5001
RIGHT_PORT = 5002

left = Server(HOST, LEFT_PORT)
right = Server(HOST, RIGHT_PORT)

l_thr = Thread(target=left.run, args=())
r_thr = Thread(target=right.run, args=())

if __name__ == "__main__":
    l_thr.start()
    r_thr.start()
