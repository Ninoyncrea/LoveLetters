from src.serfveurtest2 import Server

if __name__ == "__main__":
    SERVER_HOST = open("src/Master_ip.txt", "r").read().strip()
    SERVER_PORT = 5555
    server = Server(SERVER_HOST, SERVER_PORT)
    server.start()
