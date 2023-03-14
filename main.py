from src.server import Server

PORT = 5001

server = Server(PORT)

if __name__ == "__main__":
    server.run()