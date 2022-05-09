import socket

import threading
import time

SERVER_IP = '0.0.0.0'
SERVER_PORT = 5000


class TestServer:
    def __init__(self, ip=SERVER_IP, port=SERVER_PORT):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.host)
        self.ip, self.port = self.socket.getsockname()

    def run(self):
        print('SERVER RUNNING')
        self.socket.listen(1)
        while True:
            client_socket, *_ = self.socket.accept()
            thread = threading.Thread(target=self.communicate, args=(client_socket,))
            thread.start()
            time.sleep(1)

    def communicate(self, client_socket):
        to_stop = False
        while not to_stop:
            print(f'{self}:listening to {client_socket}')
            req = client_socket.recv(1024).decode()
            print(f'GOT REQUEST: {req}')
            if req == 'disconnect':
                break
            ans = f'I GOT YOU: {req}'
            client_socket.send(ans.encode())
            time.sleep(1)

    @property
    def host(self):
        return self.ip, self.port
