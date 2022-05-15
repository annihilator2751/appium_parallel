import socket

from core.const import DEFAULTS_SOCKET_ADAPTER, KEY_MSIZE
from core.utils import Entity, cmd_encode, cmd_decode


class SocketAdapter(Entity):
    _defaults = DEFAULTS_SOCKET_ADAPTER

    socket = None
    ip = port = app = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup()
        self.register(self.host)

    def setup(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.host)
        self.ip, self.port = self.socket.getsockname()

    def connect(self, host):
        try:
            self.socket.connect(host)
            return True
        except socket.error:
            return False

    def send(self, msg, sock=None, **kwargs):
        print(f'{self}:sending {msg}.')
        sock = sock or self.socket
        sock.send(cmd_encode(msg, **kwargs).encode())

    def recv(self, sock=None):
        print(f'{self}:receiving.')
        sock = sock or self.socket
        return cmd_decode(sock.recv(getattr(self, KEY_MSIZE)).decode())

    def __getattr__(self, item):
        return getattr(self.socket, item)

    @property
    def host(self):
        return self.ip, self.port
