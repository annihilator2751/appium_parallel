from urllib.parse import urlencode, parse_qsl


def adapt(obj, defaults: dict, **kwargs):
    for field, default in defaults.items():
        value = kwargs.get(field, default)
        setattr(obj, field, value)


def cmd_encode(cmd, **kwargs):
    return '?'.join([cmd, ] + ([urlencode(kwargs), ] if kwargs else list()))


def cmd_decode(raw_cmd):
    cmd, *other = raw_cmd.split('?')
    kwargs = dict(parse_qsl(other[0])) if len(other) == 1 else dict()
    return cmd, kwargs
