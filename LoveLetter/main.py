from src.serfveurtest2 import Server

if __name__ == "__main__":
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 5555
    server = Server(SERVER_HOST, SERVER_PORT)
    server.start()
