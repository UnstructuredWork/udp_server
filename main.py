from src.server import DeticServer

DETIC_PORT = 5054

detic = DeticServer(DETIC_PORT)

if __name__ == "__main__":
    detic.run()