from core.const.fields import *

DEFAULTS_SOCKET_ADAPTER = {
    KEY_IP: '0.0.0.0',
    KEY_PORT: 0,
    KEY_MSIZE: 10 ** 10,
    KEY_APP: None
}

DEFAULTS_CLIENT_SOCKET = {
    **DEFAULTS_SOCKET_ADAPTER,
    KEY_KNOWN_SERVER_HOSTS: list(),
}

DEFAULTS_SERVER_SOCKET = {
    **DEFAULTS_SOCKET_ADAPTER,
    KEY_PORT: 5000,
    KEY_MAX_CONN: 1
}
