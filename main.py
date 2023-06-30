from src.server import Server

LEFT_PORT = 5052

left = Server(LEFT_PORT)

if __name__ == "__main__":
    left.run()
