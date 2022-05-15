from core.const import CMD_DISCONNECT, RESP_EMPTY, DEFAULTS_SERVER_SOCKET, KEY_MAX_CONN
from core.network.socket_adapter import SocketAdapter
from core.utils import start_thread


class ServerSocket(SocketAdapter):
    _defaults = DEFAULTS_SERVER_SOCKET

    def listen(self):
        self.socket.listen(getattr(self, KEY_MAX_CONN))
        while True:
            client_socket, *_ = self.socket.accept()
            start_thread(self.communicate, client_socket)

    def communicate(self, client_socket):
        to_stop = False
        while not to_stop:
            print(f'{self}:listening to {client_socket}')
            cmd, kwargs = self.recv(client_socket)
            to_stop, resp = self.process_cmd(cmd, **kwargs)
            self.send(resp, client_socket)

    def process_cmd(self, cmd, **kwargs):
        if cmd == CMD_DISCONNECT:
            return True, RESP_EMPTY
        return False, self.app.process_cmd(cmd, **kwargs)
