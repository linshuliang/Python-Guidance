# coding=utf-8
from multiprocessing import Process, Pipe


def fn(conn: Pipe):
    conn.send([50, None, "Hello"])  # 发送信号
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=fn, args=(child_conn, ))
    p.start()  # 开始执行这个子进程
    p.join()  # 阻塞这个子进程以外的所有进程
    print(parent_conn.recv())  # 接收信号
