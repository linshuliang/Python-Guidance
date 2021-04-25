# coding=utf-8
import multiprocessing as mp


def foo(s):
    for i in range(10):
        s.send((i, mp.current_process().name))
    s.close()


if __name__ == "__main__":
    readers = list()

    for i in range(4):
        r, s = mp.Pipe(duplex=False)
        readers.append(r)
        p = mp.Process(target=foo, args=(s, ))
        p.start()
        s.close()

    while readers:
        for r in mp.connection.wait(readers):
            try:
                msg = r.recv()
            except EOFError:
                readers.remove(r)
            else:
                print(msg)
