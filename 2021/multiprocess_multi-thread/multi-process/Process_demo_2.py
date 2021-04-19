# coding=utf-8
import time
import multiprocessing
import signal

# 创建 Process 对象
p = multiprocessing.Process(target=time.sleep, args=(1000, ))

# 当前进程并没有 start， is_alive() 返回 False
print(p, p.is_alive())

# 启动进程
p.start()

# 当前进程已经 start, 而且仍未终止， is_alive() 返回 True
print(p, p.is_alive())

# 终止进程
p.terminate()

# 间隔 0.1s
time.sleep(0.1)

# 进程已终止，is_alive() 返回 False
print(p, p.is_alive())

# 进程退出时，返回码为 p.exitcode
print(p.exitcode == -signal.SIGTERM)  # True
