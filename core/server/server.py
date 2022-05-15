from core.const import KEY_APP
from core.network.server_socket import ServerSocket
from core.utils import Entity, start_thread


class Server(Entity):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.socket = ServerSocket(**kwargs, **{KEY_APP: self})

    def run(self):
        print(f'{self}:start')
        start_thread(self.socket.listen)

    def process_cmd(self, cmd, **kwargs):
        print(f'{self}:process_cmd: {cmd, kwargs}')
        return f'I GOT YOU: {cmd, kwargs}'
