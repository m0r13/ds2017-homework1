
PKG_CREATE_SESSION = 42

def read_int(stream):
    return 0

def read_string(stream):
    length = read_int(stream)
    # ...
    return ""

def write_int(stream, value):
    # ...

def write_string(stream, value):
    write_int(stream, len(value))
    # ...

def write_create_session(stream, data):
    write_int(stream, PKG_CREATE_SESSION)
    write_int(data["num_players"])

def read_create_session(stream):
    data = {}
    data["num_players"] = read_string(stream)
    return data

def read_package(stream):
    pkg_type = 0
    data = {}

    pkg_type = read_int()
    if pkg_type == PKG_CREATE_SESSION:
        data = read_create_session(stream)

    return pkg_type, data
