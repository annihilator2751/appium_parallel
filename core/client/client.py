from core.const import KEY_APP
from core.network.client_socket import ClientSocket
from core.utils import Entity


class Client(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.socket = ClientSocket(**kwargs, **{KEY_APP: self})

    def send(self, msg):
        return self.socket.send(msg)


if __name__ == '__main__':
    from config import SERVER_HOSTS
    from core.const import KEY_KNOWN_SERVER_HOSTS

    server = Client(**{KEY_KNOWN_SERVER_HOSTS: SERVER_HOSTS})
    server.send('lorem ipsum')
