from core.const import DEFAULTS_CLIENT_SOCKET, KEY_KNOWN_SERVER_HOSTS, CMD_DISCONNECT
from core.network.socket_adapter import SocketAdapter
from core.utils import ServerUnavailable


class ClientSocket(SocketAdapter):
    _defaults = DEFAULTS_CLIENT_SOCKET

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.server_host = self._get_server_host(getattr(self, KEY_KNOWN_SERVER_HOSTS))

    def __del__(self):
        self.send(CMD_DISCONNECT)

    def _get_server_host(self, hosts):
        print(f'{self}:getting server host')
        for host in hosts:
            print(f'{self}:trying {host}')
            if self.connect(host):
                return host
        raise ServerUnavailable('Failed to get response from any of servers.')
