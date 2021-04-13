# coding=utf-8


class Data(object):
    def __init__(self, id, addr):
        self._id = id
        self._addr = addr
        self._d = {"id": self._id, "addr": self._addr}

    def __setitem__(self, key, val):
        self._d[key] = val

    def __getitem__(self, key):
        if key in self._d.keys():
            return self._d[key]
        else:
            raise KeyError("KeyError: %s Not Exist" % key)

    def __delitem__(self, key):
        if key in self._d.keys():
            print("delete key : %s" % key)
            del self._d[key]


if __name__ == "__main__":
    d = Data("1", "192.168.1.1")
    d["port"] = 8088

    print(d["id"])
    print(d["addr"])
    print(d["port"])

    del d["port"]

    try:
        print(d["country"])
    except KeyError as e:
        print(e)
