import socket


class TestClient:
    def __init__(self, ip='localhost', port=0):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.host)
        self.ip, self.port = self.socket.getsockname()
        self.socket.connect(('localhost', 5000))

    def send(self, msg):
        self.socket.send(msg.encode())
        ans = self.socket.recv(1024).decode()
        print(f'ans: {ans}')

    def __del__(self):
        self.socket.send('disconnect'.encode())

    @property
    def host(self):
        return self.ip, self.port


if __name__ == '__main__':
    server = TestClient()
    server.send('blabla')
